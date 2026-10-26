# 01 — First game asset: low-poly lantern

This recipe generates a small stylized lantern from Blender mesh primitives and exports a glTF binary (.glb) for a game engine or browser client.

## Requirements

- Blender with its bundled Python API and glTF 2.0 exporter enabled.
- Python 3.12+ only for the source-contract tests (not for running the Blender script).

## Generate the asset

Run from a terminal with Blender installed:

```sh
blender --background --python create_lantern.py -- --output ./build/zqm-lantern.glb
```

The script clears the current scene, creates a base, trim, frame posts, emissive core, roof, and ring handle, assigns materials, then exports a GLB. **Run this only in a disposable Blender scene or background process**: it intentionally deletes existing scene objects before generating the sample.

Review the exported asset in the target engine. The sample uses simple primitive geometry and a modest torus; it is a starting point, not a production-optimized or visually approved asset. Check dimensions, face normals, material appearance, scale, and draw calls before shipping.

## Source-contract tests

From this directory, run:

```sh
python -m unittest discover -s tests -v
```

These tests validate Python syntax and source-level expectations for named components, material roles, and GLB export settings. They do **not** run Blender or prove that the installed Blender version successfully executes the script. Run the generation command above to perform the actual integration smoke test.

## Files

- create_lantern.py — procedural asset generator.
- tests/test_asset_script_contract.py — dependency-free source-contract tests.

## Pipeline notes

- Prefer GLB for a single-file handoff when the target runtime supports glTF 2.0.
- Keep the editable Blender project in your normal asset source-control workflow; the exported GLB is a build artifact.
- Keep textures and mesh complexity within the target platform's budget.
- Record licenses for external meshes, textures, and reference art. This recipe creates geometry procedurally and fetches no remote assets.
