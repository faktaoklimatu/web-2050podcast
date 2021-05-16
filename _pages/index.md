---
layout: empty
title: Fakta o klimatu
slug: index
---
<div class="section intro">
    <div class="container">
        <h1 class="display-1" id="home">2050</h1>
        <p>Klimatický podcast o budoucnosti, ve které nám nepoteče do bot.<br/>
            <a href="{{ site.fundraising }}" class="btn btn-primary mt-3"><i class="fas fa-fw fa-heart"></i> Podpořte nás</a>
            <a href="https://open.spotify.com/show/4vhMfZxkN7iUGQMVqEvOO8" class="btn btn-secondary mt-3"><i class="fas fa-fw fa-headphones"></i> Poslechni si teaser!</a>
            <a href="https://instagram.com/{{ site.instagram }}" class="btn btn-secondary mt-3"><i class="fab fa-fw fa-instagram"></i> Instagram</a>
        </p>
    </div>
</div>
<div class="section"><div class="container" markdown="1">

{:.display-2}
## Epizody

{:.lead}
Zajímají vás naše novinky? V této sekci vždy najdete naše nejnovější infografiky, výtahy studií a datasety.

{% for episode in site.episodes %}

### [{{ episode.title }}]({{ episode.url }})

{{ episode.summary }}

{% endfor %}

</div></div>
<div class="section"><div class="container" markdown="1">
{:.display-2}
## Podpořte nás

{:.lead}
Zajímají vás naše novinky? V této sekci vždy najdete naše nejnovější infografiky, výtahy studií a datasety.

</div></div>
<div class="section"><div class="container" markdown="1">
{:.display-2}
## Kontakt?

Nejaky dalsi text...

</div></div>
