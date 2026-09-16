import bpy
from pathlib import Path

destination = Path('C:/AI/Projects/BlenderProject/blend/simple_desk.blend')
assert not destination.exists(), 'Refusing to overwrite existing work'
bpy.ops.wm.save_as_mainfile(filepath=str(destination))
assert destination.is_file()
print('Saved:', bpy.data.filepath)
