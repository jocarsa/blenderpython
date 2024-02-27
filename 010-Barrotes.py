# Importo librería
import bpy

# Selecciono todos los objetos
bpy.ops.object.select_all(action='SELECT')
# Borro los objetos
bpy.ops.object.delete(use_global=False)
# Declarar la anchura de la ventana
anchura = 32
# Defino el numero de barrotes que quiero
numbarrotes = 6

# balda inferior
bpy.ops.mesh.primitive_cube_add(
    size=1, 
    enter_editmode=False, 
    align='WORLD', 
    location=(0, 0, 0), 
    scale=(anchura, 1, 1)
)
# balda superior
bpy.ops.mesh.primitive_cube_add(
    size=1, 
    enter_editmode=False, 
    align='WORLD', 
    location=(0, 0, anchura), 
    scale=(anchura, 1, 1)
)
# balda izquierda
bpy.ops.mesh.primitive_cube_add(
    size=1, 
    enter_editmode=False, 
    align='WORLD', 
    location=(-anchura/2, 0, anchura/2), 
    scale=(1, 1, anchura)
)
# balda derecha
bpy.ops.mesh.primitive_cube_add(
    size=1, 
    enter_editmode=False, 
    align='WORLD', 
    location=(anchura/2, 0, anchura/2), 
    scale=(1, 1, anchura)
)
# cristal
bpy.ops.mesh.primitive_cube_add(
    size=1, 
    enter_editmode=False, 
    align='WORLD', 
    location=(0, 0, anchura/2), 
    scale=(anchura, 0.1, anchura)
)
for barrotex in range(int(-anchura/2),int(anchura/2),int(anchura/numbarrotes)):
    bpy.ops.mesh.primitive_cube_add(
        size=1, 
        enter_editmode=False, 
        align='WORLD', 
        location=(barrotex, 0, anchura/2), 
        scale=(0.2, 0.2, anchura)
    )
    bpy.ops.mesh.primitive_cube_add(
        size=1, 
        enter_editmode=False, 
        align='WORLD', 
        location=(0, 0, barrotex+anchura/2), 
        scale=(anchura, 0.2, 0.2)
    )