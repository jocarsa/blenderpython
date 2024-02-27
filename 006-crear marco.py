# Importo librería
import bpy

# Selecciono todos los objetos
bpy.ops.object.select_all(action='SELECT')
# Borro los objetos
bpy.ops.object.delete(use_global=False)

# balda inferior
bpy.ops.mesh.primitive_cube_add(
    size=1, 
    enter_editmode=False, 
    align='WORLD', 
    location=(0, 0, 0), 
    scale=(10, 1, 1)
)
# balda superior
bpy.ops.mesh.primitive_cube_add(
    size=1, 
    enter_editmode=False, 
    align='WORLD', 
    location=(0, 0, 10), 
    scale=(10, 1, 1)
)
# balda izquierda
bpy.ops.mesh.primitive_cube_add(
    size=1, 
    enter_editmode=False, 
    align='WORLD', 
    location=(-5, 0, 5), 
    scale=(1, 1, 10)
)
# balda derecha
bpy.ops.mesh.primitive_cube_add(
    size=1, 
    enter_editmode=False, 
    align='WORLD', 
    location=(5, 0, 5), 
    scale=(1, 1, 10)
)
