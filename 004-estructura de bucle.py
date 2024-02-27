import bpy

mix = 1
miy = 2
miz = 3

for posicionx in range(0,20,3):
    bpy.ops.mesh.primitive_cube_add(
        size=2, 
        enter_editmode=False, 
        align='WORLD', 
        location=(posicionx, 0, 0), 
        scale=(mix, miy, miz)
    )
