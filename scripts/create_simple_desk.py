import bpy

DESK_NAMES = ['Desk_Tabletop', 'Desk_Leg_FrontLeft', 'Desk_Leg_FrontRight',
              'Desk_Leg_BackLeft', 'Desk_Leg_BackRight']

def create_part(name, location, dimensions, color, bevel):
    assert name not in bpy.data.objects, name + ' already exists'
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + '_Mesh'
    obj.dimensions = dimensions
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.color = color
    material = bpy.data.materials.get('Desk_Wood')
    if material is None:
        material = bpy.data.materials.new('Desk_Wood')
        material.diffuse_color = color
        material.use_nodes = True
        bsdf = material.node_tree.nodes.get('Principled BSDF')
        bsdf.inputs['Base Color'].default_value = color
        bsdf.inputs['Roughness'].default_value = 0.45
    obj.data.materials.append(material)
    modifier = obj.modifiers.new('Soft_Edges', 'BEVEL')
    modifier.width = bevel
    modifier.segments = 3
    obj.modifiers.new('Corner_Normals', 'WEIGHTED_NORMAL')
    return obj

def make_top():
    assert all(name not in bpy.data.objects for name in DESK_NAMES)
    bpy.context.scene['desk_original_transforms'] = __import__('json').dumps({
        o.name: [list(row) for row in o.matrix_world] for o in bpy.context.scene.objects})
    create_part('Desk_Tabletop', (-3, 0, 0.72), (1.6, 0.8, 0.06),
                (0.48, 0.25, 0.10, 1), 0.012)

def make_legs():
    for name, x, y in [('FrontLeft', -3.68, -0.28), ('FrontRight', -2.32, -0.28),
                       ('BackLeft', -3.68, 0.28), ('BackRight', -2.32, 0.28)]:
        create_part('Desk_Leg_' + name, (x, y, 0.345), (0.08, 0.08, 0.69),
                    (0.48, 0.25, 0.10, 1), 0.004)

if __name__ == '__main__':
    make_top()
    make_legs()
