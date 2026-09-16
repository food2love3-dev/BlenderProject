import bpy
import json
from mathutils import Vector

original = json.loads(bpy.context.scene['desk_original_transforms'])
for name, matrix in original.items():
    assert name in bpy.context.scene.objects, name
    assert all(abs(bpy.data.objects[name].matrix_world[i][j] - matrix[i][j]) < 1e-6
               for i in range(4) for j in range(4)), name

parts = [o for o in bpy.context.scene.objects if o.name.startswith('Desk_')]
assert len(parts) == 5
def bounds(obj):
    points = [obj.matrix_world @ Vector(c) for c in obj.bound_box]
    return ([min(p[i] for p in points) for i in range(3)],
            [max(p[i] for p in points) for i in range(3)])

for part in parts:
    assert all(abs(s - 1) < 1e-6 for s in part.scale)
    assert all(abs(r) < 1e-6 for r in part.rotation_euler)
    a, b = bounds(part)
    for name in original:
        other = bpy.data.objects[name]
        if other.type != 'MESH':
            continue
        c, d = bounds(other)
        assert any(b[i] <= c[i] or a[i] >= d[i] for i in range(3)), (part.name, name)
    if part.name != 'Desk_Tabletop':
        assert abs(a[2]) < 1e-6
        assert abs(b[2] - 0.69) < 1e-6

bpy.ops.object.select_all(action='DESELECT')
for part in parts:
    part.select_set(True)
bpy.context.view_layer.objects.active = bpy.data.objects['Desk_Tabletop']
for screen in bpy.data.screens:
    for area in screen.areas:
        if area.type == 'VIEW_3D':
            space = area.spaces.active
            space.shading.type = 'SOLID'
            space.shading.color_type = 'MATERIAL'
            region = space.region_3d
            region.view_location = Vector((-2.1, 0, 0.35))
            region.view_distance = 6.2
            region.view_rotation = Vector((3, -6, 3.5)).to_track_quat('Z', 'Y')
            region.view_perspective = 'PERSP'
            area.tag_redraw()
print(json.dumps({'original_objects_preserved': list(original),
                  'desk_parts': [{'name':o.name, 'location':list(o.location),
                                  'dimensions':list(o.dimensions), 'scale':list(o.scale)} for o in parts],
                  'collision_check':'passed', 'leg_contacts':'passed'}, indent=2))
