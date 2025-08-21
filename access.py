import bpy

bpy.data.objects # get the collection of library objects
bpy.data.scenes # get the scenes
bpy.data.meterials # get the materials

# accessing these objects
list(bpy.data.objects)
# Both index based and key-based accessing
bpy.data.objects['Cube']
bpy.data.objects[0]

# Accessing attributes
bpy.data.objects[0].name
bpy.data.scenes['Scene']
bpy.data.materials.new("MyMaterial")