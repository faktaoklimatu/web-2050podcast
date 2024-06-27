EPISODE_IMAGES_FOLDER=assets/episodes
EPISODE_IMAGES_SRC=$(wildcard _episodes/*.jpg _episodes/*.png)
EPISODE_IMAGES_DST=$(addprefix $(EPISODE_IMAGES_FOLDER)/,$(notdir $(EPISODE_IMAGES_SRC)))

PODMAN=podman
CONTAINER_IMAGE=2050podcast/web
CONTAINER_NAME=2050podcast
# Set branch name (from Travis or locally)
BRANCH:=$(or $(TRAVIS_BRANCH),`git branch --show-current`)

all: build

# === Container management targets  ===

container:
	if $(PODMAN) inspect $(CONTAINER_NAME) >/dev/null 2>&1 ; \
		then $(PODMAN) start -a $(CONTAINER_NAME) ||: ; \
		else make build-container; fi

build-container:
	$(PODMAN) build --file Dockerfile --tag $(CONTAINER_IMAGE) .
	$(PODMAN) run --interactive --tty --name $(CONTAINER_NAME) \
		--volume $$PWD/..:/srv/jekyll --publish 4000:4000 $(CONTAINER_IMAGE) ||:

delete-container:
	$(PODMAN) rm --force $(CONTAINER_NAME)

# === Core build, test and deploy targets  ===

bundle-install:
	bundle install

build: generated-files bundle-install
	@echo "Building the website using Jekyll ..."
	@if [ "$(BRANCH)" = "master" ]; then echo "=== Production build ($(BRANCH)) ==="; else echo "=== Development build ($(BRANCH)) ==="; fi
	@if [ "$(BRANCH)" = "master" ]; then JEKYLL_ENV=production bundle exec jekyll build; else bundle exec jekyll build; fi

local: generated-files bundle-install
	bundle exec jekyll serve --trace

check: build
	@echo "Running internal tests on the generated site using html-proofer ..."
# Temporarily allow for tests to fail
	bundle exec ruby utils/test.rb
	@echo "Running tests on the external content using html-proofer ..."
	-bundle exec ruby utils/test.rb external

# To run lighthouse, you need Google Chrome and Lighthous CLI (npm install -g @lhci/cli@0.7.x)
lighthouse: build
	lhci autorun

deploy-preview:
	./firebase hosting:channel:deploy $(BRANCH) --only preview

deploy-production:
	./firebase deploy --only hosting:production

# === Targets for generating files  ===

generated-files: humans.txt $(EPISODE_IMAGES_DST)

humans.txt: CONTRIBUTORS.md
	@echo "Creating humans.txt file ..."
	cp CONTRIBUTORS.md humans.txt

$(EPISODE_IMAGES_FOLDER)/%: _episodes/%
	mkdir -p $(@D)
	cp $< $@

# === Cleaning targets  ===

clean:
	rm -rf _site

clean-build: clean
	rm -rf vendor
	rm -rf .cache

# === Target flags  ===

.PHONY: all build local clean clean-build bundle-install generated-files
.PHONY: container build-container delete-container
