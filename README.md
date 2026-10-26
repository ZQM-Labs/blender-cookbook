# Blender Cookbook

<!-- ZQM-START -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <strong>ZQM Labs</strong><br>
  <a href="https://github.com/ZQM-Labs">ZQM Labs</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-END -->

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A **Blender cookbook** for game assets: modeling, scripting, materials, and render/export pipelines. Patterns are written for game developers preparing art in Blender for real-time games: low-poly models, baked textures, and exports that load cleanly in an engine or web client. It is intended for game developers and artists building game-ready assets. Validate each pattern against your own game, Blender version, and operating environment before adopting it.

## Repository role and status

**Status:** Active, public — first procedural asset generator implemented. Source-contract tests do not execute Blender; each generated asset still requires an engine-backed smoke test and visual review.

**What this repository is:** Blender patterns — modeling, scripting, materials, and render/export pipelines for game assets.

**What it contributes:** Part of the ZQM Labs game-development portfolio, and a sibling to the ZQM Computing geospatial cookbook series.

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

Game developers and artists building game-ready assets in Blender for real-time and web games.

## Prerequisites

- Blender 5.2.3 LTS (fleet-verified on Node-1; version pinned per pattern at fill time)
- A game engine or web client that can load the exported asset formats
- Synthetic reference art for the examples

## Patterns

| # | Example | Status | What it demonstrates |
|---|---------|--------|----------------------|
| 01 | `01-first-game-asset` | Implemented generator | Procedural low-poly lantern, named materials/components, and GLB export settings |
| 02 | `02-scripting-pipeline` | Planned | Blender Python scripting: batch operations and asset preparation without manual repetition |
| 03 | `03-materials-textures` | Planned | Materials and texture baking for real-time game rendering |
| 04 | `04-render-export` | Planned | Rendering turntables and sprites, and exporting assets for engine and web delivery |

## Quick start

Requires Blender for generation and Python 3.12+ for source-contract tests:

```sh
cd examples/01-first-game-asset
blender --background --python create_lantern.py -- --output ./build/zqm-lantern.glb
python -m unittest discover -s tests -v
```

The script deletes existing objects in its active scene, so use the background command or a disposable project. The automated tests do not launch Blender.

## Repository layout

```text
blender-cookbook/
├── .github/workflows/examples.yml
├── examples/01-first-game-asset/
│   ├── create_lantern.py
│   ├── README.md
│   └── tests/test_asset_script_contract.py
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: first game asset (01), then scripting pipeline (02)
- Second pass: materials and textures (03) and render/export (04)

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.
