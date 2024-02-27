import bpy 

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

def creaCaja():
    bpy.ops.mesh.primitive_cube_add(
        size=1, 
        enter_editmode=False, 
        align='WORLD', 
        location=(0, 0, anchura/2), 
        scale=(anchura, 0.1, anchura)
    )