import bpy

bpy.ops.mesh.primitive_cube_add(
    size=1, 
    enter_editmode=False, 
    align='WORLD', 
    location=(0, 0, 0), 
    scale=(1, 1, 1)
)
# Coordenadas de transformacion
bpy.context.object.rotation_euler[0] = 0.174533
bpy.context.object.rotation_euler[1] = 0.24
bpy.context.object.rotation_euler[2] = 0.523599

# Coordenadas de ubicación
bpy.context.object.location[0] = 1
bpy.context.object.location[1] = 2
bpy.context.object.location[2] = 3

# Coordenadas de escala
bpy.context.object.scale[0] = 2
bpy.context.object.scale[1] = 3
bpy.context.object.scale[2] = 4
