---
layout: empty
title: Všechny epizody
slug: epizody
---
<div class="section"><div class="container" markdown="1">

# {{ page.title }}

Intro text.

</div></div>

{% assign sorted_episodes = site.episodes | sort: number | reverse %}
{% for episode in sorted_episodes %}
<div class="section"><div class="container" markdown="1">

{% include episode-preview.html episode=episode %}

</div></div>
{% endfor %}
