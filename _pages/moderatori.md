---
layout: empty
title: Moderátoři
slug: moderatori
moderators:
- name: "Petr Holík"
  story: |
    Základem přírodovědec, který si svůj vztah k vědě vytvářel během práce na výzkumech v Arktidě i na jižní Moravě. Už při studiu Fyzické geografie se začal věnovat také tématu komunikace. Dnes kromě tvorby podcastů (2050, Nenásilný podcast, Science slam MUNI) školí popularizaci vědy a učí vědce efektivně mluvit o jejich výzkumech. Věnuje se též vzdělávání a mediaci konfliktů metodou nenásilné komunikace. Díky zkušenostem s improvizačním a fyzickým divadlem a performance se v jeho osobě ojedinělým způsobem setkává svět vědy a svět umění.
  img: "petr-holik.jpeg"
  email: "petr.holik@faktaoklimatu.cz"
  linkedin: "https://www.linkedin.com/in/petrholik/"
  twitter: "https://twitter.com/holik_petr"
- name: "Hana Vrtalová"
  story: |
     Hanka se věnuje produkci vědecko-popularizačních akcí, zejména v projektu Science slam. Ve Faktech o klimatu se specializuje na téma transformace dopravy a spoluvytváří podcast 2050. Kromě toho také lektoruje širokou škálu workshopů pro firemní klienty nebo studenty na Přírodovědecké fakultě Masarykovy univerzity v Brně, kde zároveň řídí lektorské pracoviště zaměřené na vzdělávání a trénink budoucích učitelů. Posledních devět let se aktivně věnuje divadelní improvizaci.
  img: "hanka-vrtalova.jpeg"
  email: "hana.vrtalova@faktaoklimatu.cz"
  linkedin: "https://www.linkedin.com/in/hana-vrtalová/"
  twitter: "https://twitter.com/HVrtalova"
references:
- author: "Petr Škyřík"
  affiliation: "Masarykova univerzita"
  quote: |
    Moderátory podcastu jsem pozval na Letní školu našeho pracoviště. Jejich přednášky i workshopy k tématu *komunikace změn klimatu* byly bohaté na aktuální datové podklady. Velmi si cením didaktické zručnosti obou lektorů.
- author: "Denisa Hobžová"
  affiliation: "Biskupské gymnázium Brno"
  quote: |
    Skvělá beseda, podpořená grafikou projektu Fakta o klimatu. Petr živě reagoval na dotazy studentů, kteří oceňovali zejména otevřený a věcný přístup k tématu. Pro velký úspěch jsme jej pozvali i na další akci, tentokrát specificky zaměřenou na dílčí problematiku.
- author: "David Uhlíř"
  affiliation: "Jihomoravské inovační centrum"
  quote: |
    Hanu jsme oslovili při přípravě doprovodného vědecko-popularizačního programu ve formátu Science slam pro naši akci Velvet Innovation MeetUp. Ukázalo se, že se jedná o skvělé doplnění naší události. Diváci se nejen pobavili, ale něco nového se i dozvěděli.
- author: "Karolína Břinková"
  affiliation: "Iniciativa Slow Femme"
  quote: |
    S Petrem jako moderátorem jsem se poprvé setkala při natáčení podcastu 2050. Vyhovoval mi jeho styl vedení rozhovoru, proto jsme ho přizvali i k moderování debaty *Móda a klimatická změna*, která proběhla v rámci hudebního festivalu Rock for People. Musím vyzdvihnout jeho orientaci v tématu, pokládání spontánních doplňkových otázek, schopnost informačně propojovat problematiku klimatu a fungování módního průmyslu. A samozřejmě nesmím zapomenout na úvod před začátkem vlastní diskuze, kdy svým projevem a energií vtáhl posluchače do tématu.
---
<div class="section moderators"><div class="container">
<h1>{{ page.title }}</h1>
</div></div>

<div class="section claim"><div class="container"><div class="claim-text">
Moderátoři podcastu Petr Holík a Hana Vrtalová, s mnohaletými zkušenostmi s komunikací vědy a performance.
</div></div></div>

<div class="section"><div class="container">
<h2>Můžeme moderovat i vaši akci</h2>

<div class="row my-3 my-sm-5">

<div class="col-12 col-sm-12 col-md-5">
<div class="moderators-callout" markdown="1">
**S čím nás můžete oslovit**:
- Moderování konferencí, debat a panelových diskuzí
- Přednášky, workshopy a vzdělávání o změně klimatu – pro firmy, školy nebo veřejnost
- Online i prezenční akce nebo live streamy

Napište nám na [podcast@2050podcast.cz](mailto:podcast@2050podcast.cz).
</div>
</div>

<div class="col-12 col-sm-12 col-md-7">
<div class="my-4 m-sm-4" markdown="1">
Diskuze na témata klimatické změny &amp; transformace je vždy mnohem zajímavější, když ji moderuje člověk, který má sám do tématu vhled.

Moderátoři podcastu 2050 jsou zkušení lektoři komunikačních dovedností, vysokoškolští vyučující a zároveň herci se zkušenostmi z improvizačního a pohybového divadla. Jejich hlasy a styl si můžete poslechnout v našem podcastu.
</div>
</div>

</div>
</div></div>

<div class="section"><div class="container">
  <div class="row">
    {%- for item in page.moderators %}
    <div class="col-12 col-sm-12 col-md-6 mt-3">
        <div class="card bg-transparent border-0 m-md-1 m-lg-3">
            <div class="text-center mb-3">
                <img class="card-img-top p-2 moderator-photo" src="/assets/img/{{item.img}}" alt="{{item.name}}">
            </div>
            <div class="card-body d-flex flex-column">
                <h5 class="card-title text-center">
                    <span class="pr-2">{{ item.name }}</span>
                    {% if item.linkedin %}<a class="no-ext-link-icon" href="{{ item.linkedin }}"><span class="fab fa-fw fa-linkedin"></span></a>{% endif %}
                    {%- if item.twitter %}<a class="no-ext-link-icon" href="{{ item.twitter }}"><span class="fab fa-fw fa-twitter"></span></a>{% endif %}

                </h5>
                <div class="card-text mb-3 text-center">{{ item.story | markdownify }}</div>
                {%- if item.email %}
                <div class="mt-auto text-center">
                    <a class="align-self-end" href="mailto:{{ item.email }}">{{ item.email }}</a>
                </div>
                {% endif -%}
            </div>
        </div>
    </div>
    {%- endfor %}
  </div>
</div></div>

<div class="section"><div class="container" markdown="1">

## Reference

<div class="row mt-2">
  {%- for item in page.references %}
    <div class="col-12 col-md-6">
      <div class="card bg-transparent border-0 m-md-3 m-lg-4">
        <blockquote class="m-3">
          {{ item.quote | markdownify }}
        </blockquote>
        <div class="quote-author m-3">
          {{ item.author }}<span>{{ item.affiliation }}</span>
        </div>
      </div>
    </div>
  {%- endfor %}
</div>

</div></div>
