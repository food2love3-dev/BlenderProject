"""Add a soft, three-point studio lighting rig around the desk.

This script only creates or updates lights whose names start with Desk_Light_.
Other scene objects, including Blender's original Light, are left intact.
"""

import bpy
from mathutils import Vector


TARGET = Vector((-3.0, 0.0, 0.55))


def area_light(name, location, energy, color, size, size_y):
    obj = bpy.data.objects.get(name)
    if obj is None:
        data = bpy.data.lights.new(name, type="AREA")
        obj = bpy.data.objects.new(name, data)
        bpy.context.scene.collection.objects.link(obj)
    elif obj.type != "LIGHT":
        raise RuntimeError(f"Object name {name} is already in use by a non-light")

    data = obj.data
    data.type = "AREA"
    data.energy = energy
    data.color = color
    data.shape = "RECTANGLE"
    data.size = size
    data.size_y = size_y
    obj.location = location
    direction = TARGET - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    return obj


area_light(
    "Desk_Light_Key",
    (-4.35, -2.0, 3.15),
    420,
    (1.0, 0.92, 0.82),
    2.4,
    1.7,
)
area_light(
    "Desk_Light_Fill",
    (-1.55, -1.45, 2.35),
    210,
    (0.82, 0.90, 1.0),
    2.0,
    1.5,
)
area_light(
    "Desk_Light_Rim",
    (-2.45, 1.65, 2.75),
    300,
    (1.0, 0.98, 0.93),
    1.8,
    1.0,
)

print("Desk studio lights:", [obj.name for obj in bpy.data.objects if obj.name.startswith("Desk_Light_")])
