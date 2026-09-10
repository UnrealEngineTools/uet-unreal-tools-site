# Unreal Tools — landing page

The hub at **unrealtools.com** — an entry point into Conduit, GeoScape and Ultimate
Deck Building Toolkit for Unreal Engine developers.

Static homepage plus the Ultimate Deck Building Toolkit documentation at
`/deck-toolkit/`. Generated HTML is committed, so serving the site needs no build step.
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
