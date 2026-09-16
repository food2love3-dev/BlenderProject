"""Add simple modern desk accessories to the currently open Blender scene.

Run in two small steps from the Blender bridge:
    exec(compile(open(PATH, encoding='utf-8').read(), PATH, 'exec'))
    add_monitor()
    add_small_accessories()
Existing objects are never changed or removed. Re-running skips named objects.
"""

import bpy
import math


def _cube(name, location, dimensions, bevel=0.0):
    if name in bpy.data.objects:
        return bpy.data.objects[name]
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = dimensions
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if bevel:
        mod = obj.modifiers.new('Soft edges', 'BEVEL')
        mod.width = bevel
        mod.segments = 3
        obj.modifiers.new('Weighted normals', 'WEIGHTED_NORMAL')
    return obj


def _cylinder(name, location, radius, depth, vertices=48):
    if name in bpy.data.objects:
        return bpy.data.objects[name]
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=location)
    obj = bpy.context.object
    obj.name = name
    for polygon in obj.data.polygons:
        polygon.use_smooth = True
    return obj


def add_monitor():
    # Screen faces toward the front of the desk (-Y).
    _cube('Desk_Monitor_Frame', (-3.08, 0.205, 1.095), (0.68, 0.038, 0.39), 0.012)
    _cube('Desk_Monitor_Screen', (-3.08, 0.183, 1.095), (0.635, 0.005, 0.345), 0.003)
    _cylinder('Desk_Monitor_Stem', (-3.08, 0.235, 0.835), 0.012, 0.17)
    _cube('Desk_Monitor_Base', (-3.08, 0.225, 0.758), (0.28, 0.17, 0.016), 0.012)


def add_small_accessories():
    _cube('Desk_Keyboard_Body', (-3.03, -0.205, 0.772), (0.51, 0.15, 0.028), 0.014)
    _cube('Desk_Keyboard_Keys', (-3.03, -0.207, 0.789), (0.47, 0.115, 0.008), 0.004)
    _cube('Desk_Mouse', (-2.59, -0.215, 0.77), (0.065, 0.105, 0.035), 0.024)
    _cube('Desk_Notebook', (-3.59, -0.135, 0.762), (0.18, 0.255, 0.024), 0.005)
    _cube('Desk_Notebook_Page', (-3.59, -0.135, 0.776), (0.168, 0.242, 0.005), 0.002)
    _cylinder('Desk_Mug_Body', (-2.43, 0.18, 0.804), 0.052, 0.108)
    _cylinder('Desk_Mug_Interior', (-2.43, 0.18, 0.857), 0.039, 0.002)
    # A torus handle reads clearly at the scale of the composition.
    if 'Desk_Mug_Handle' not in bpy.data.objects:
        bpy.ops.mesh.primitive_torus_add(major_segments=36, minor_segments=12,
                                        location=(-2.375, 0.18, 0.81),
                                        rotation=(math.pi / 2, 0, 0),
                                        major_radius=0.042, minor_radius=0.009)
        bpy.context.object.name = 'Desk_Mug_Handle'

