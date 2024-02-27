import bpy 

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

#Aquí definimos una función
def creaCaja(px,py,pz):
    bpy.ops.mesh.primitive_cube_add(
        size=1, 
        enter_editmode=False, 
        align='WORLD', 
        location=(px, py, pz), 
        scale=(1, 1, 1)
    )
    
# Aquí utilizo la función
creaCaja(1,2,4)
creaCaja(3,2,4)
creaCaja(5,2,4)