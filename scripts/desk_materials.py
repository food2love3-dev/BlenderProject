"""Apply a restrained modern palette to the desk and its accessories.

Run `apply_desk_materials()` in the active Blender scene after modeling.
Only named Desk_ meshes receive material assignments. Existing scene objects
and geometry are left in place.
"""

import bpy


def _material(name, color, roughness=0.5, metallic=0.0, emission=None):
    material = bpy.data.materials.get(name)
    if material is None:
        material = bpy.data.materials.new(name)
    material.use_nodes = True
    material.diffuse_color = (*color, 1.0)
    shader = material.node_tree.nodes.get('Principled BSDF')
    shader.inputs['Base Color'].default_value = (*color, 1.0)
    shader.inputs['Roughness'].default_value = roughness
    shader.inputs['Metallic'].default_value = metallic
    shader.inputs['Emission Color'].default_value = (*emission, 1.0) if emission else (0, 0, 0, 1)
    shader.inputs['Emission Strength'].default_value = 0.45 if emission else 0.0
    return material


def apply_desk_materials():
    palette = {
        'oak': _material('DeskMat_WarmOak', (0.60, 0.38, 0.20), 0.48),
        'metal': _material('DeskMat_CharcoalMetal', (0.075, 0.09, 0.105), 0.33, 0.75),
        'plastic': _material('DeskMat_GraphitePlastic', (0.13, 0.15, 0.17), 0.58),
        'keys': _material('DeskMat_SlateKeys', (0.29, 0.32, 0.34), 0.66),
        'screen': _material('DeskMat_QuietScreen', (0.025, 0.09, 0.12), 0.24,
                            emission=(0.035, 0.15, 0.18)),
        'ceramic': _material('DeskMat_CreamCeramic', (0.85, 0.81, 0.73), 0.22),
        'coffee': _material('DeskMat_Coffee', (0.11, 0.055, 0.028), 0.19),
        'cover': _material('DeskMat_SageCover', (0.23, 0.38, 0.32), 0.71),
        'paper': _material('DeskMat_IvoryPaper', (0.88, 0.85, 0.76), 0.84),
    }
    mapping = {
        'Desk_Tabletop': 'oak',
        'Desk_Leg_FrontLeft': 'metal',
        'Desk_Leg_FrontRight': 'metal',
        'Desk_Leg_BackLeft': 'metal',
        'Desk_Leg_BackRight': 'metal',
        'Desk_Monitor_Frame': 'plastic',
        'Desk_Monitor_Screen': 'screen',
        'Desk_Monitor_Stem': 'metal',
        'Desk_Monitor_Base': 'metal',
        'Desk_Keyboard_Body': 'plastic',
        'Desk_Keyboard_Keys': 'keys',
        'Desk_Mouse': 'plastic',
        'Desk_Notebook': 'cover',
        'Desk_Notebook_Page': 'paper',
        'Desk_Mug_Body': 'ceramic',
        'Desk_Mug_Interior': 'coffee',
        'Desk_Mug_Handle': 'ceramic',
    }
    assigned = []
    missing = []
    for name, key in mapping.items():
        obj = bpy.data.objects.get(name)
        if obj is None:
            missing.append(name)
            continue
        if obj.type != 'MESH':
            raise TypeError(f'{name} is not a mesh')
        obj.data.materials.clear()
        obj.data.materials.append(palette[key])
        assigned.append((name, palette[key].name))
    return {'assigned': assigned, 'missing': missing}
