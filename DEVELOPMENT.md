# Development & deployment notes

These existing operational notes are preserved from the previous README. Product pages are authoritative for current availability and purchase routes; older checkout or launch notes below may describe an earlier deployment.

# Unreal Tools — landing page

The hub at **unrealtools.com** — an entry point into Conduit, GeoScape and Ultimate
Deck Building Toolkit and Save Compatibility Lab for Unreal Engine developers.

Static homepage plus the Ultimate Deck Building Toolkit documentation at
`/deck-toolkit/` and Save Compatibility Lab at `/save-compatibility-lab/`.
Generated HTML is committed, so serving the site needs no build step.
Deployed via Cloudflare Pages.

## Local preview

```bash
python -m http.server 8080   # then visit http://localhost:8080
```

## Deck Toolkit documentation

Eleven pages cover overview, installation/example project, cards/decks, workbench,
reference session, rules/probability, native workshop integration, local persistence,
live tracing, public API and troubleshooting. The content is authored in
`scripts/build_deck_docs.py`; CSS/JS and original product screenshots are under
`deck-toolkit/assets/`. Update the source and regenerate the committed HTML:

```bash
python scripts/build_deck_docs.py
python scripts/check_deck_docs.py
node --check deck-toolkit/assets/docs.js
python scripts/stage_site.py
```

The checker validates local page/asset links, fragment IDs, unique IDs, main headings
and search-index completeness. Browser QA covered desktop/mobile layouts, search,
code copying and mobile menu behavior. Content was checked against the standalone
plugin's 0.3.0 public headers and implementations. Integration excerpts are not complete
host classes. Documentation does not publish the paid source archive.

Independent project, not affiliated with or endorsed by Epic Games or Unreal Engine.

## Deploy / update

Save Compatibility Lab documentation is built from the released 1.0.0 HTML guide
in `scripts/content/save-lab-guide-1.0.0.html`. Run
`python scripts/build_save_lab_docs.py` after changing its website shell. The
homepage features the original Fab cover, and the guide includes the actual editor
capture, section navigation, example project download and standalone guide link.
The Fab listing is pending approval; both entry points describe that status.
The paid source archive is not linked or included in the public site.

Run `python scripts/check_deck_docs.py` to check all 13 public HTML pages before staging.

Hosted on **Cloudflare Pages** (project `unrealtools-site`, domains `unrealtools.com` + `www`)
via **direct upload** — pushing this repo does NOT auto-deploy. The `.wrangler`
cache and staged public files are ignored by Git. From this repository:

```bash
python scripts/stage_site.py
npx wrangler pages deploy dist --project-name unrealtools-site --branch main
```

Alternatively, open the existing Cloudflare Pages project, Create deployment,
choose Production and upload the generated `site-upload.zip`. This archive contains
only the public homepage, favicon and documentation tree. Do not upload the repository
root: `.git`, scripts and local artifacts are not public site assets.

The existing CLI OAuth session may lack `pages:write`; the already signed-in Pages
dashboard supports direct upload without changing CLI access. Use the existing
`unrealtools-site` project, not a new Pages project.

### Verified production deployment

On September 11, 2026, Save Compatibility Lab was added at source commit `ae4815b`
and deployed through the existing Cloudflare dashboard (25 public files).
Production deployment: `d5c3d8c1-510e-4625-a550-1120e0454097`.

Live guide: https://www.unrealtools.com/save-compatibility-lab/

Verified the live homepage entry, guide navigation, correct Fab/download targets,
and loaded cover/workbench images in the browser. All 13 local HTML pages passed
the link/fragment checker; the archive matched the exact public file allowlist.

On September 10, 2026, site content at commit `7c2eb17` was deployed through the
existing Cloudflare dashboard (21 public files). Production deployment:
`064dd96b-9cba-4b6d-8b6b-26622bdc5ab7`.

Live documentation: https://www.unrealtools.com/deck-toolkit/

Production checks confirmed the homepage entry, documentation navigation, search,
loaded screenshots and correct UTF-8 text. Local checks covered all 12 HTML pages,
local links/fragments, all 11 search topics, and desktop/mobile interactions.

### Custom domain note (apex)

Cloudflare auto-creates DNS for **subdomains** added to a Pages project, but NOT for the
**apex**. For `unrealtools.com` add the records by hand in the Cloudflare dashboard, then the
cert provisions in a few minutes:

| Type | Name | Target | Proxy |
|---|---|---|---|
| CNAME | `@` | `unrealtools-site.pages.dev` | Proxied |
| CNAME | `www` | `unrealtools-site.pages.dev` | Proxied |

## Unreleased products

Save Compatibility Lab and Ultimate Deck Building Toolkit show a non-interactive Coming soon label on the hub and every documentation page. Keep their docs accessible. Add purchase links only after the public storefront page is live, using the actual public URL from Fab's View on Fab action, not the publisher portal ID. Update the documentation generators alongside their output.


## Ultimate Road Tool 1.2.0

The homepage features Ultimate Road Tool and its actual Unreal road artwork.
`/ultimate-road-tool/` contains the released guide in the site documentation shell,
with five navigable chapters, FAQ, installation, controls, materials, road paint,
turn pockets, geographic example instructions and data attribution.

The source guide is preserved in `scripts/content/road-tool-guide-1.2.0.html`.
Regenerate with `python scripts/build_road_docs.py`; run
`python scripts/check_deck_docs.py` and `python scripts/stage_site.py` before deploy.
The checker now covers all 14 HTML pages. The staging allowlist contains 30 public
files. Source scripts and the paid plugin archive are not deployed.

The page links the verified public 1.2.0 example and standalone guide on R2.
It describes the Fab submission as pending review; replace that status with the
verified public storefront URL after publication. Do not use a publisher portal ID.

Validated desktop and 390px mobile layout, documentation anchors, expandable FAQ,
and loaded cover images. Geographic limitations and plugin installation requirements
are explicit next to the example download.

### Road Tool deployment verification

September 11, 2026: deployed source commit `5203ce7` to the existing
`unrealtools-site` Cloudflare Pages production project through the signed-in
dashboard. Cloudflare confirmed 30/30 files uploaded and deployment success.

Verified the live homepage Road Tool entry and navigation to
https://www.unrealtools.com/ultimate-road-tool/ in a browser. All three product
images loaded, chapter anchors worked, and the R2 download URLs matched the
verified release artifacts. Desktop/mobile and FAQ checks passed locally.
