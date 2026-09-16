import bpy
from pathlib import Path

root = Path(r"C:\AI\Projects\BlenderProject")
scene = bpy.context.scene
bpy.context.preferences.filepaths.save_version = 0
scene.render.engine = 'BLENDER_EEVEE'
scene.render.resolution_x = 1200
scene.render.resolution_y = 900
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = str(root / 'renders' / 'modern_desk.png')
bpy.ops.wm.save_as_mainfile(filepath=str(root / 'blend' / 'modern_desk_scene.blend'))
bpy.ops.render.render(write_still=True)
print(f"Saved: {bpy.data.filepath}; render: {scene.render.filepath}")
