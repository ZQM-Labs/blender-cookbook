"""Generate a small, stylized low-poly lantern and export it as glTF binary.

Run with Blender:
  blender --background --python create_lantern.py -- --output /tmp/zqm-lantern.glb

This script is intended for Blender's bundled Python API; it is not a regular
standalone Python program.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import bpy


def parse_output_path() -> Path:
    """Read the optional output path after Blender's '--' separator."""
    args = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="zqm-lantern.glb", help="Output GLB path")
    return Path(parser.parse_args(args).output).expanduser().resolve()


def make_material(name: str, color: tuple[float, float, float, float], emission: float = 0.0):
    material = bpy.data.materials.new(name=name)
    material.diffuse_color = color
    material.use_nodes = True
    principled = material.node_tree.nodes.get("Principled BSDF")
    if principled:
        principled.inputs["Base Color"].default_value = color
        if "Emission Color" in principled.inputs:
            principled.inputs["Emission Color"].default_value = color
            principled.inputs["Emission Strength"].default_value = emission
    return material


def add_cube(name: str, location: tuple[float, float, float],
             scale: tuple[float, float, float], material, bevel: float = 0.0):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(material)
    if bevel > 0:
        modifier = obj.modifiers.new(name="Soft edges", type="BEVEL")
        modifier.width = bevel
        modifier.segments = 2
        obj.modifiers.new(name="Weighted corner normals", type="WEIGHTED_NORMAL")
    return obj


def build_lantern() -> None:
    """Replace the scene with a low-poly lantern made from simple primitives."""
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)

    metal = make_material("Midnight enamel", (0.055, 0.09, 0.15, 1.0))
    brass = make_material("Warm brass", (0.95, 0.55, 0.12, 1.0))
    glow = make_material("Lantern glow", (1.0, 0.78, 0.28, 1.0), emission=1.5)

    # Main base and roof; dimensions are authored in meters.
    add_cube("Lantern_Base", (0.0, 0.0, 0.12), (1.15, 1.15, 0.24), metal, 0.07)
    add_cube("Lantern_Base_Trim", (0.0, 0.0, 0.27), (0.98, 0.98, 0.08), brass, 0.025)
    add_cube("Lantern_Roof_Trim", (0.0, 0.0, 1.48), (1.0, 1.0, 0.09), brass, 0.025)
    add_cube("Lantern_Roof", (0.0, 0.0, 1.62), (1.12, 1.12, 0.22), metal, 0.06)
    add_cube("Lantern_Glow_Core", (0.0, 0.0, 0.88), (0.52, 0.52, 0.95), glow, 0.06)

    # Four vertical frame posts.
    for x in (-0.43, 0.43):
        for y in (-0.43, 0.43):
            add_cube(f"Lantern_Post_{'L' if x < 0 else 'R'}_{'B' if y < 0 else 'F'}",
                     (x, y, 0.88), (0.09, 0.09, 1.18), brass, 0.018)

    # Ring handle above the roof. Keep polygon count modest for web delivery.
    bpy.ops.mesh.primitive_torus_add(
        major_radius=0.25, minor_radius=0.045, major_segments=16,
        minor_segments=6, location=(0.0, 0.0, 1.94), rotation=(1.5708, 0.0, 0.0),
    )
    handle = bpy.context.object
    handle.name = "Lantern_Handle"
    handle.data.materials.append(brass)

    for obj in bpy.context.scene.objects:
        if obj.type == "MESH":
            obj.select_set(True)
        else:
            obj.select_set(False)
    bpy.context.view_layer.objects.active = bpy.context.scene.objects.get("Lantern_Base")
    bpy.context.scene.unit_settings.system = "METRIC"


def export_glb(output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.export_scene.gltf(
        filepath=str(output_path),
        export_format="GLB",
        export_apply=True,
        export_yup=True,
        export_materials="EXPORT",
    )


def main() -> None:
    output_path = parse_output_path()
    build_lantern()
    export_glb(output_path)
    print(f"Exported lantern asset: {output_path}")


if __name__ == "__main__":
    main()
