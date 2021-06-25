---
layout: empty
title: Fakta o klimatu
slug: index
---
<div class="section intro">
    <div class="container">
        <h1 id="home">2050</h1>
        <p>Klimatický podcast o budoucnosti,<br/>ve které nám nepoteče do bot.<br/>
            <a href="#epizody" class="btn btn-primary">Poslechni si teaser <i class="fas fa-fw fa-arrow-down"></i></a>
        </p>
        <p>Chceš dát vědět,<br/>až vyjde první epizoda?<br/>
            <a href="#" class="btn btn-primary">To teda chci!</a>
        </p>
    </div>
</div>
<div class="section"><div class="container" markdown="1">

## Proč a jak točíme tenhle podcast

<div class="d-sm-flex mt-3 mb-3">
<div class="mr-sm-3" markdown="1">

{:.color-primary}
### Chceme

aby se lidé v otázce změny klimatu lépe orientovali. Aby věděli o řešeních, která jsou v současné době už k dispozici a můžeme je použít.

</div>
<div markdown="1">

{:.color-primary}
### Nechceme

prohlubovat "klimatickou depresi" a přinášet další zprávy o tom, jak je všechno špatně. Nechceme se ale ani tvářit, že svět spasí třídění odpadu.

</div>
</div>

Podcast 2050 má za cíl komunikovat o otázkách spojených se změnou klimatu věcně a konstruktivně a opírat se přitom o data a dosavadní vědecké poznatky. Nečekejte proto úhel pohledu, který je jednoduchý a černobílý. Zatímco v některých krocích k udržitelné budoucnosti má lidstvo už dnes jasno a stačí je jen realizovat, jinde ještě nevíme.

V podcastu 2050 prozkoumáváme cesty k takové budoucnosti, ve které nám nepoteče do bot.

## Epizody

{% assign sorted_episodes = site.episodes | sort: number | reverse %}
{% for episodee in sorted_episodes %}
{% include episode-preview.html episode=episodee %}
{% endfor %}

### [Zobraz všechny epizody](/epizody)

</div></div>
