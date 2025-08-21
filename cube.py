import bpy
bpy.data.objects["Cube"].data.vertices[0].co.x += 1.0
bpy.data.objects["Cube"].data.vertices[0].co.y -= 3.0
bpy.data.objects["Cube"].data.vertices[4].co.x += 5.0

list(bpy.data.objects)
bpy.data.objects["Cube"]

bpy.data.objects[0]
bpy.data.objects[1]
bpy.data.objects[0].name

mesh = bpy.data.meshes.new(name="MyMesh")
bpy.data.meshes.remove(mesh)

# context is based on what object is currently selected
bpy.context.object["MyOwnProperty"] = 42
bpy.context.selected_objects
bpy.context.visible_bones

cube = bpy.data.objects["Cube"]
# Select the cube/make it the active context
bpy.context.view_layer.objects.active = cube
# bpy.context.active_object = cube # This raises an error