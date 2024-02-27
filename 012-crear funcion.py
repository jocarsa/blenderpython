import bpy 

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

#Aquí definimos una función
def creaCaja():
    bpy.ops.mesh.primitive_cube_add(
        size=1, 
        enter_editmode=False, 
        align='WORLD', 
        location=(0, 0, 0), 
        scale=(1, 1, 1)
    )
    
# Aquí utilizo la función
creaCaja()