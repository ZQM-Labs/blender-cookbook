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

**Status:** Active, public — seeding. Pattern passes land in follow-up work; the table below lists what is planned, not what is already written.

**What this repository is:** Blender patterns — modeling, scripting, materials, and render/export pipelines for game assets.

**What it contributes:** Part of the ZQM Labs game-development portfolio, and a sibling to the ZQM Computing geospatial cookbook series.

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

Game developers and artists building game-ready assets in Blender for real-time and web games.

## Prerequisites

- Blender 5.2.3 LTS (fleet-verified on Node-1; version pinned per pattern at fill time)
- A game engine or web client that can load the exported asset formats
- Synthetic reference art for the examples

## Patterns (planned)

| # | Example | What it will demonstrate |
|---|---------|--------------------------|
| 01 | `01-first-game-asset` | A first low-poly game asset: modeling, UVs, and export to a game-ready format |
| 02 | `02-scripting-pipeline` | Blender Python scripting: batch operations and asset preparation without manual repetition |
| 03 | `03-materials-textures` | Materials and texture baking for real-time game rendering |
| 04 | `04-render-export` | Rendering turntables and sprites, and exporting assets for engine and web delivery |

## Repository layout

```text
blender-cookbook/
├── examples/  # one directory per pattern
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: first game asset (01), then scripting pipeline (02)
- Second pass: materials and textures (03) and render/export (04)

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.
