# Podcast RSS → GitHub Pages

On-demand GitHub Actions workflow that fetches a podcast RSS feed, extracts the
`title` and `enclosure` of the 10 most recent episodes, and publishes them as an
HTML page with inline audio players to GitHub Pages.

## Running the action

1. In the repo, open the **Actions** tab.
2. Pick **Fetch RSS** in the left sidebar.
3. Click **Run workflow** (top right). You can accept the defaults or override:
   - `feed_url` — any RSS URL; defaults to the Fakta o klimatu podcast feed.
   - `limit` — number of episodes (default `10`).
4. When the run finishes (~30 s), you'll see:
   - A markdown table with every episode's title + enclosure link in the
     run's **Summary** tab.
   - The published site at
     `https://<your-user-or-org>.github.io/<your-repo>/` — listed as the
     `github-pages` environment URL on the `deploy` job.

Re-running the workflow overwrites the published page with the latest 10
episodes.
