<img src="https://raw.githubusercontent.com/UnrealEngineTools/.github/main/profile/assets/org-banner.svg" alt="Unreal Tools · Website & documentation" width="100%">

# Unreal Tools · Website & documentation

Native tools for people building in Unreal Engine. Explore the product family, read integration guides, and find examples for your next project.

**[Explore the website](https://www.unrealtools.com) · [Community](https://github.com/UnrealEngineTools/.github/discussions)**

## Explore the toolbox

| Tool | What it helps you do | Start here |
| :--- | :--- | :--- |
| Conduit | Connect an AI agent to the Unreal Editor through MCP | [Product & docs](https://conduit.unrealtools.com) |
| GeoScape | Build environments from real geographic data | [Product & docs](https://geoscape.unrealtools.com) |
| Ultimate Road Tool | Author connected roads, sidewalks, and crossings | [Guide](https://www.unrealtools.com/ultimate-road-tool/) |
| Ultimate Deck Building Toolkit | Author cards, assemble decks, and integrate a native workshop | [Guide](https://www.unrealtools.com/deck-toolkit/) |
| Save Compatibility Lab | Compare historical saves against approved baselines | [Guide](https://www.unrealtools.com/save-compatibility-lab/) |

Product pages describe current availability, supported engine versions, platforms, and licensing.

## Inside the repository

The static product hub and generated documentation live here. HTML output is committed, so local browsing needs no build step. Python scripts in `scripts/` generate and validate the documentation.

```bash
python -m http.server 8080
```

Open [localhost:8080](http://localhost:8080). For content changes, update the relevant generator and regenerate its output; see [Development & deployment](DEVELOPMENT.md).

```bash
python scripts/check_deck_docs.py
```


## Contribute or get help

- [Report a documentation or website issue](https://github.com/UnrealEngineTools/uet-unreal-tools-site/issues/new/choose).
- Read the [contribution guide](https://github.com/UnrealEngineTools/.github/blob/main/CONTRIBUTING.md) before proposing a change.
- Use [Support](https://github.com/UnrealEngineTools/.github/blob/main/SUPPORT.md) for product questions and purchase support.
- Report vulnerabilities privately using [Security](https://github.com/UnrealEngineTools/.github/blob/main/SECURITY.md).

Part of [Unreal Engine Tools](https://github.com/UnrealEngineTools). Independent of Epic Games; not affiliated with or endorsed by Epic Games. Public website source does not grant a license to the commercial plugins.
