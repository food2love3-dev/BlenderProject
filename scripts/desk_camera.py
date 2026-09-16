"""Create and activate a three-quarter camera for the modern desk scene."""
import bpy
from mathutils import Vector

name = "Desk_Camera_ThreeQuarter"
camera = bpy.data.objects.get(name)
if camera is None:
    camera_data = bpy.data.cameras.new(name)
    camera = bpy.data.objects.new(name, camera_data)
    bpy.context.scene.collection.objects.link(camera)

camera.location = (-0.9, -3.25, 2.05)
target = Vector((-3.0, 0.0, 0.62))
camera.rotation_euler = (target - camera.location).to_track_quat('-Z', 'Y').to_euler()
camera.data.type = 'PERSP'
camera.data.lens = 45.0
camera.data.clip_start = 0.05
camera.data.clip_end = 100.0
bpy.context.scene.camera = camera

for screen in bpy.data.screens:
    for area in screen.areas:
        if area.type == 'VIEW_3D':
            area.spaces.active.region_3d.view_perspective = 'CAMERA'

print('camera', camera.name, 'location', tuple(camera.location), 'lens', camera.data.lens)
