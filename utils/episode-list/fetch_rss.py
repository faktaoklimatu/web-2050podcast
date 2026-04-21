#!/usr/bin/env python3
"""Fetch a podcast RSS feed and render the last N episodes as a static HTML page.

Env vars:
  FEED_URL    RSS feed URL (default: the Fakta o klimatu podcast feed)
  LIMIT       Number of episodes to keep (default: 10)
  OUTPUT_DIR  Directory to write index.html into (default: site)

Also appends a markdown summary to $GITHUB_STEP_SUMMARY when present.
"""
from __future__ import annotations

import html
import os
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

FEED_URL = os.environ.get("FEED_URL") or "https://anchor.fm/s/1039e0eb8/podcast/rss"
LIMIT = int(os.environ.get("LIMIT") or "10")
OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR") or "site")


def fetch_feed(url: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "rss-fetcher/1.0 (+github-actions)"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def parse_episodes(xml_bytes: bytes, limit: int) -> list[dict]:
    root = ET.fromstring(xml_bytes)
    channel = root.find("channel")
    if channel is None:
        raise RuntimeError("Feed has no <channel> element")

    episodes: list[dict] = []
    for item in channel.findall("item")[:limit]:
        title_el = item.find("title")
        enclosure_el = item.find("enclosure")
        title = (title_el.text or "").strip() if title_el is not None else ""
        enclosure = {
            "url": enclosure_el.get("url", "") if enclosure_el is not None else "",
            "type": enclosure_el.get("type", "") if enclosure_el is not None else "",
            "length": enclosure_el.get("length", "") if enclosure_el is not None else "",
        }
        episodes.append({"title": title, "enclosure": enclosure})
    return episodes


HTML_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Latest {limit} episodes</title>
<style>
  :root {{ color-scheme: light dark; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    max-width: 1000px; margin: 2rem auto; padding: 0 1rem;
    color: #1f2328; background: #fff;
  }}
  @media (prefers-color-scheme: dark) {{
    body {{ color: #e6edf3; background: #0d1117; }}
    th {{ background: #161b22 !important; color: #8b949e !important; }}
    tr:hover td {{ background: #161b22 !important; }}
    th, td {{ border-bottom-color: #30363d !important; }}
    .meta, .num {{ color: #8b949e !important; }}
  }}
  h1 {{ margin-bottom: 0.25rem; }}
  .meta {{ color: #656d76; font-size: 0.9rem; margin-bottom: 2rem; }}
  .meta a {{ color: inherit; }}
  table {{ width: 100%; border-collapse: collapse; }}
  th, td {{
    text-align: left; padding: 0.75rem;
    border-bottom: 1px solid #d0d7de; vertical-align: top;
  }}
  th {{
    font-size: 0.75rem; text-transform: uppercase;
    letter-spacing: 0.05em; color: #656d76; background: #f6f8fa;
  }}
  tr:hover td {{ background: #f6f8fa; }}
  .num {{ width: 2.5rem; color: #656d76; font-variant-numeric: tabular-nums; }}
  .title {{ font-weight: 600; }}
  .download {{
    display: block;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size: 0.85rem; word-break: break-all; white-space: pre-wrap;
  }}
</style>
</head>
<body>
<h1>Latest {limit} episodes</h1>
<p class="meta">
  Source: <a href="{feed_url}">{feed_url}</a>
  &middot; Generated {generated_at}
</p>
<table>
  <thead>
    <tr><th class="num">#</th><th>Title</th><th>Enclosure</th></tr>
  </thead>
  <tbody>
{rows}
  </tbody>
</table>
</body>
</html>
"""

ROW_TEMPLATE = """    <tr>
      <td class="num">{i}</td>
      <td class="title">{title}</td>
      <td><code class="download">download:   "{url}"</code></td>
    </tr>"""


def render_html(episodes: list[dict], feed_url: str, generated_at: str) -> str:
    rows = "\n".join(
        ROW_TEMPLATE.format(
            i=i,
            title=html.escape(ep["title"]) or "<em>(no title)</em>",
            url=html.escape(ep["enclosure"]["url"], quote=True),
        )
        for i, ep in enumerate(episodes, 1)
    )
    return HTML_PAGE.format(
        limit=len(episodes),
        feed_url=html.escape(feed_url, quote=True),
        generated_at=html.escape(generated_at),
        rows=rows,
    )


def write_step_summary(episodes: list[dict], feed_url: str) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    lines = [
        f"# Latest {len(episodes)} episodes",
        "",
        f"Source: <{feed_url}>",
        "",
        "```yaml",
    ]
    for i, ep in enumerate(episodes, 1):
        lines.append(f"# {i}. {ep['title'] or '(no title)'}")
        lines.append(f'download:   "{ep["enclosure"]["url"]}"')
        lines.append("")
    lines.append("```")
    with open(summary_path, "a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main() -> int:
    print(f"Fetching: {FEED_URL}", flush=True)
    xml_bytes = fetch_feed(FEED_URL)
    episodes = parse_episodes(xml_bytes, LIMIT)
    print(f"Parsed {len(episodes)} episodes", flush=True)
    for i, ep in enumerate(episodes, 1):
        print(f"  {i:2d}. {ep['title']}")
        print(f'      download:   "{ep["enclosure"]["url"]}"')

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    (OUTPUT_DIR / "index.html").write_text(
        render_html(episodes, FEED_URL, generated_at),
        encoding="utf-8",
    )
    print(f"Wrote {OUTPUT_DIR / 'index.html'}")

    write_step_summary(episodes, FEED_URL)
    return 0


if __name__ == "__main__":
    sys.exit(main())