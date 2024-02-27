import bpy

mix = 1
miy = 2
miz = 3

bpy.ops.mesh.primitive_cube_add(
    size=2, 
    enter_editmode=False, 
    align='WORLD', 
    location=(0, 0, 0), 
    scale=(mix, miy, miz)
)
