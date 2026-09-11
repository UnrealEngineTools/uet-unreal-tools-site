"""Wrap the released 1.0.0 guide in the Unreal Tools documentation shell."""
from pathlib import Path
import html, re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'save-compatibility-lab'
R2 = 'https://pub-5f5c0d0b15df417e9653e1f4329e3269.r2.dev/save-compatibility-lab/1.0.0/'
source = (ROOT / 'scripts/content/save-lab-guide-1.0.0.html').read_text(encoding='utf-8')
body = source[source.index('<h2>'):source.rindex('</main>')]
topics = []
def heading(match):
    title = match.group(1)
    slug = re.sub(r'[^a-z0-9]+', '-', html.unescape(title).lower()).strip('-')
    topics.append((slug, title))
    return f'<h2 id="{slug}">{title}</h2>'
body = re.sub(r'<h2>(.*?)</h2>', heading, body)
body = body.replace('<table>', '<div class="table-scroll" tabindex="0" role="region" aria-label="Comparison rules"><table>').replace('</table>', '</table></div>')
toc = ''.join(f'<a href="#{slug}">{title}</a>' for slug, title in topics)
OUT.mkdir(exist_ok=True)
(OUT / 'index.html').write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Save Compatibility Lab — Documentation | Unreal Tools</title>
<meta name="description" content="Keep old saves working in Unreal Engine 5.8. Save Compatibility Lab installation, fixtures, baselines, Blueprint/C++ adapters, comparison rules and CI documentation.">
<meta property="og:title" content="Save Compatibility Lab | Unreal Tools">
<meta property="og:description" content="Protect the progress your players earned. Historical save fixtures, typed state comparisons and CI reports for Unreal Engine.">
<meta property="og:type" content="website"><meta name="theme-color" content="#080c0d">
<link rel="canonical" href="https://www.unrealtools.com/save-compatibility-lab/">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="assets/docs.css"></head>
<body><a class="skip" href="#content">Skip to documentation</a>
<header class="site-header"><a class="brand" href="/">Unreal Tools</a><nav aria-label="Product navigation"><a href="/#tools">All tools</a><a href="#install-and-try-the-example">Get started</a><span class="availability" aria-describedby="fab-status" style="display:inline-flex;align-items:center;padding:11px 18px;border:1px solid #4B4B53;border-radius:8px;background:#ffffff06;color:#B8B8C3;font-size:14px;font-weight:600">Coming soon</span></nav></header>
<div class="layout"><aside class="contents"><details open><summary>On this page</summary><nav aria-label="Documentation sections"><a href="#content">Overview &amp; downloads</a>{toc}</nav></details></aside>
<main id="content"><section class="hero"><p class="eyebrow">HUNGRY GHOST / PRODUCT DOCUMENTATION</p>
<h1>Save Compatibility Lab</h1><p class="lead">Protect the progress your players earned.</p>
<p>Keep historical saves, load them with current code, and compare the resulting state with an explicitly approved baseline. Catch missing inventory, changed quest state and broken migrations before a release.</p>
<div class="pills"><span>Version 1.0.0</span><span>Unreal Engine 5.8</span><span>Windows</span><span>Blueprint + C++ adapters</span></div>
<div class="actions"><span class="availability" aria-describedby="fab-status" style="display:inline-flex;align-items:center;padding:11px 18px;border:1px solid #4B4B53;border-radius:8px;background:#ffffff06;color:#B8B8C3;font-size:14px;font-weight:600">Coming soon</span><a class="button secondary" href="#install-and-try-the-example">Start here ↓</a></div>
<p class="muted" id="fab-status">Coming soon to Fab. Explore the documentation while the release is being prepared.</p>
<figure><a href="assets/workbench.png" aria-label="Open full-size Save Compatibility Lab workbench screenshot"><img src="assets/workbench.png" width="1920" height="1080" alt="Native Unreal workbench with save fixtures, compatibility results and field differences"></a><figcaption>The editor workbench. The example deliberately loses a potion to demonstrate a regression.</figcaption></figure>
<div class="downloads"><h2 id="downloads">Downloads</h2><p><a href="{R2}SaveCompatibilityLab_Example_UE5.8.zip">Download the UE 5.8 example project ZIP ↗</a></p><p>Install the plugin separately, open <code>SaveCompatibilityLabExample.uproject</code>, then use <strong>Tools → Save Compatibility Lab → Import suite</strong> and select <code>Fixtures/suite.json</code>. Expect three passing cases and one intentional failure. Use <code>Fixtures/passing-suite.json</code> for an all-passing suite.</p><p><a href="{R2}SaveCompatibilityLab_UserGuide.html">Open the standalone 1.0.0 user guide ↗</a></p></div></section>
<article>{body}</article>
<footer><p>Save Compatibility Lab 1.0.0 · Hungry Ghost</p><a href="/">Back to Unreal Tools</a><p class="muted">Independent third-party tools. Not affiliated with or endorsed by Epic Games.</p></footer></main></div></body></html>''', encoding='utf-8')
print(f'Built Save Compatibility Lab guide with {len(topics)} documentation sections.')
