"""Publish the released Road Tool guide inside the existing documentation shell."""
from pathlib import Path
import html
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'ultimate-road-tool'
R2 = 'https://pub-5f5c0d0b15df417e9653e1f4329e3269.r2.dev/ultimate-road-tool-builds/1.2.0/'
source = (ROOT / 'scripts/content/road-tool-guide-1.2.0.html').read_text(encoding='utf-8')
body = source[source.index('<h2>'):source.rindex('</html>')]
# Keep a single page title; retain the released guide's chapter hierarchy.
body = body.replace('<h2>', '<h3>').replace('</h2>', '</h3>')
body = body.replace('<h1>', '<h2>').replace('</h1>', '</h2>')
body = '<h2>Getting started</h2>' + body
topics = []
seen = set()
def heading(match):
    level, title = match.groups()
    slug = re.sub(r'[^a-z0-9]+', '-', html.unescape(title).lower()).strip('-')
    base = slug
    count = 2
    while slug in seen:
        slug = f'{base}-{count}'
        count += 1
    seen.add(slug)
    if level == '2':
        topics.append((slug, title))
    return f'<h{level} id="{slug}">{title}</h{level}>'
body = re.sub(r'<h([23])>(.*?)</h\1>', heading, body)
body = body.replace('<table>', '<div class="table-scroll" tabindex="0" role="region" aria-label="Road tool reference table"><table>').replace('</table>', '</table></div>')
# Turn references to the bundled Markdown files into useful website navigation.
for name, anchor in [('GISExample', 'ultimate-road-tool-1-2-0-experimental-gis-example'), ('EditorMode', 'road-editor-and-optional-surface-wear'), ('SurfaceKits', 'surface-modules-and-materials'), ('Markings', 'lane-layouts-and-road-paint')]:
    body = body.replace(f'<strong>Docs/{name}.md</strong>', f'<a href="#{anchor}">{name} guide</a>')
body = re.sub(r'(?<!["=])(https://[^\s<]+)(?=</p>)', lambda m: f'<a href="{m[1]}">{m[1]}</a>', body)
body = body.replace('<h2 id="lane-layouts-and-road-paint">', '<figure><img src="assets/markings.jpg" width="1920" height="1080" loading="lazy" alt="Road markings and crossings on editable Unreal roads"><figcaption>Painted lanes, arrows and crossing controls on the road surface.</figcaption></figure><h2 id="lane-layouts-and-road-paint">')
body = body.replace('<h2 id="ultimate-road-tool-1-2-0-experimental-gis-example">', '<figure><img src="assets/city.jpg" width="1920" height="1080" loading="lazy" alt="The experimental Cape Town network with 5,850 editable roads in Unreal"><figcaption>The separate geographic example: 5,850 editable roads. Experimental, flat-ground data interpretation.</figcaption></figure><h2 id="ultimate-road-tool-1-2-0-experimental-gis-example">')
toc = ''.join(f'<a href="#{slug}">{title.replace("Ultimate Road Tool 1.2.0 — experimental GIS example", "Geographic city example")}</a>' for slug, title in topics)
OUT.mkdir(exist_ok=True)
(OUT / 'index.html').write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ultimate Road Tool — Documentation | Unreal Tools</title>
<meta name="description" content="Build editable road networks in Unreal Engine 5.8. Ultimate Road Tool 1.2.0 installation, road editor, lanes, crossings, surface wear and experimental geographic city guide.">
<meta property="og:title" content="Ultimate Road Tool | Unreal Tools">
<meta property="og:description" content="Your city starts here. Editable roads, connected junctions, five surface styles and customizable road markings.">
<meta property="og:image" content="https://www.unrealtools.com/ultimate-road-tool/assets/cover.jpg">
<meta property="og:type" content="website"><meta name="theme-color" content="#09090c">
<link rel="canonical" href="https://www.unrealtools.com/ultimate-road-tool/">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="assets/docs.css"></head>
<body><a class="skip" href="#content">Skip to documentation</a>
<header class="site-header"><a class="brand" href="/">Unreal Tools</a><nav aria-label="Product navigation"><a href="/#tools">All tools</a><a href="#install-and-start">Get started</a><a href="#downloads">Downloads</a></nav></header>
<div class="layout"><aside class="contents"><details open><summary>On this page</summary><nav aria-label="Documentation sections"><a href="#content">Overview</a><a href="#downloads">Example &amp; downloads</a>{toc}<a href="#faq">Frequently asked questions</a></nav></details></aside>
<main id="content"><section class="hero"><p class="eyebrow">HUNGRY GHOST / ULTIMATE ROAD TOOL</p>
<h1>Your city starts here.</h1><p class="lead">Draw a street. Shape a network. Keep every road editable.</p>
<p>Ultimate Road Tool brings spline roads, connected junctions, independent sidewalks and configurable lane paint into a dedicated Unreal editor mode. Start from five surface styles, extend roads with successive clicks, and adjust widths, crossings and wear as your city takes shape.</p>
<div class="pills"><span>Version 1.2.0</span><span>Unreal Engine 5.8</span><span>Windows / Win64</span><span>Five surface styles</span></div>
<div class="actions"><a class="button" href="#install-and-start">Read the guide ↓</a><a class="button secondary" href="#ultimate-road-tool-1-2-0-experimental-gis-example">Explore the city example</a></div>
<p class="muted" id="fab-status">Coming soon to Fab. Version 1.2.0 has been submitted for review; documentation is available now.</p>
<figure><img src="assets/cover.jpg" width="1920" height="1080" fetchpriority="high" alt="Ultimate Road Tool: editable roads and a marked intersection rendered inside Unreal Engine"><figcaption>Actual Unreal Engine road imagery from the supplied tool and examples.</figcaption></figure>
<div class="feature-grid"><div><h2>Build continuously</h2><p>Extend from an anchor, keep clicking, then connect to another road. Switch between a full panel and compact toolbar.</p></div><div><h2>Make it yours</h2><p>One-way or two-way layouts, turn pockets, stop approaches, sidewalk widths and optional surface grime.</p></div><div><h2>Explore city scale</h2><p>A 1,200-road authored map and a separate experimental 5,850-road geographic example. Each street stays editable.</p></div></div>
<div class="downloads"><h2 id="downloads">Example &amp; downloads</h2><p><a href="{R2}UltimateRoadTool_Example_UE5.8.zip">Download the UE 5.8 example project ZIP · 760 MiB ↗</a></p><p>Requires Ultimate Road Tool installed separately. Open <code>UltimateRoadTool_Example.uproject</code>; it starts in the smaller Markings showcase. For the geographic network, open <code>/Game/GIS/Maps/L_CapeTown_Release_v120</code>.</p><p>The city loads as one map and requires substantial memory and several minutes to open. Begin with the smaller examples; see <a href="#experimental-scope">the geographic example's scope and performance notes</a>.</p><p><a href="{R2}UltimateRoadTool_UserGuide.html">Open the standalone 1.2.0 user guide ↗</a></p></div></section>
<article>{body}
<h2 id="faq">Frequently asked questions</h2>
<details class="faq"><summary>Can I edit every road in the city example?</summary><p>Yes. Each street is an editable StreetActor, with spline points, widths, sidewalks and paint settings. The separate Cape Town example is experimental and may need manual junction cleanup; it is not a finished city environment.</p></details>
<details class="faq"><summary>Does it include traffic, pedestrians or working signals?</summary><p>No. Road markings are visual authoring. ZoneGraph guides provide an integration starting point; vehicle simulation, Mass crowds, signal phases and pedestrian queues are not included.</p></details>
<details class="faq"><summary>Can I use one-way roads and more than two lanes?</summary><p>Yes. Each direction supports zero to twelve lanes. Set Along spline and Against spline, apply the lane counts and width, then customize individual lane uses, arrows and separators.</p></details>
<details class="faq"><summary>Does it work automatically with GeoScape?</summary><p>They are separate tools for complementary city workflows. This release does not include automatic GeoScape terrain fitting or a general GIS import interface.</p></details>
<details class="faq"><summary>What helps keep editing responsive?</summary><p>Local edits refresh affected roads and junction arms. Paint-only edits retain asphalt and sidewalk geometry, and shared materials avoid per-tile material instances. Whole-city loading still has substantial memory and component costs; World Partition integration and baked road LODs are not supplied.</p></details>
<details class="faq"><summary>Do I need Blender or an external subscription?</summary><p>No. The Unreal content is supplied. UE 5.8 on Windows is the validated editor target; Windows C++ tools are needed for source builds and packaging games. Other platforms have not been validated.</p></details>
</article><footer><p>Ultimate Road Tool 1.2.0 · Hungry Ghost</p><a href="/">Back to Unreal Tools</a><p class="muted">Independent third-party tools. Not affiliated with or endorsed by Epic Games.</p></footer></main></div></body></html>''', encoding='utf-8')
print(f'Built Ultimate Road Tool guide with {len(topics)} chapters and FAQ.')
