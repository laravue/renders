

import bpy
bpy.ops.wm.open_mainfile(filepath="/var/render/avatar.blend")


hatpath = "/var/render/models/hats/blackfedora.obj"
import_hat = bpy.ops.import_scene.obj(filepath=hatpath)
hat = bpy.context.selected_objects[0]
bpy.context.selected_objects[0].data.name = "hat"
hatImg = bpy.data.images.load(filepath="/var/render/textures/hats/blackfedora.png")
hatTex = bpy.data.textures.new("ColorTex", type = "IMAGE")
hatTex.image = hatImg
hatMat = bpy.data.materials.new("MaterialName")
hatMat.diffuse_shader = "LAMBERT"
hatSlot = hatMat.texture_slots.add()
hatSlot.texture = hatTex
hat.active_material = hatMat



hat2path = "/var/render/models/hats/pothead.obj"
import_hat2 = bpy.ops.import_scene.obj(filepath=hat2path)
hat2 = bpy.context.selected_objects[0]
bpy.context.selected_objects[0].data.name = "hat2"
hat2Img = bpy.data.images.load(filepath="/var/render/textures/hats/pothead.png")
hat2Tex = bpy.data.textures.new("ColorTex", type = "IMAGE")
hat2Tex.image = hat2Img
hat2Mat = bpy.data.materials.new("MaterialName")
hat2Mat.diffuse_shader = "LAMBERT"
hat2Slot = hat2Mat.texture_slots.add()
hat2Slot.texture = hat2Tex
hat2.active_material = hat2Mat


HeadImg = bpy.data.images.load(filepath="/var/render/textures/faces/face.png")
HeadTex = bpy.data.textures.new("ColorTex", type = "IMAGE")
HeadTex.image = HeadImg
Headslot = bpy.data.objects["Head"].active_material.texture_slots.add()
Headslot.texture = HeadTex


LeftArmImg = bpy.data.images.load(filepath="/var/www/html/storage/store_storage/shirts/test.png")
LeftArmTex = bpy.data.textures.new("ColorTex", type = "IMAGE")
LeftArmTex.image = LeftArmImg
LeftArmslot = bpy.data.objects["LeftArm"].active_material.texture_slots.add()
LeftArmslot.texture = LeftArmTex

RightArmImg = bpy.data.images.load(filepath="/var/www/html/storage/store_storage/shirts/test.png")
RightArmTex = bpy.data.textures.new("ColorTex", type = "IMAGE")
RightArmTex.image = RightArmImg
RightArmslot = bpy.data.objects["RightArm"].active_material.texture_slots.add()
RightArmslot.texture = RightArmTex


TorsoImg = bpy.data.images.load(filepath="/var/www/html/storage/store_storage/shirts/test.png")
TorsoTex = bpy.data.textures.new("ColorTex", type = "IMAGE")
TorsoTex.image = TorsoImg
Torsolot = bpy.data.objects["Torso"].active_material.texture_slots.add()
Torsolot.texture = TorsoTex


bpy.data.objects["Torso"].select = True
bpy.data.objects["Torso"].active_material.diffuse_color = (16/255,113/255,184/255)

bpy.data.objects["Head"].select = True
bpy.data.objects["Head"].active_material.diffuse_color = (225/255,221/255,56/255)

bpy.data.objects["RightArm"].select = True
bpy.data.objects["RightArm"].active_material.diffuse_color = (225/255,221/255,56/255)

bpy.data.objects["LeftArm"].select = True
bpy.data.objects["LeftArm"].active_material.diffuse_color = (225/255,221/255,56/255)

bpy.data.objects["LeftLeg"].select = True
bpy.data.objects["LeftLeg"].active_material.diffuse_color = (225/255,221/255,56/255)

bpy.data.objects["RightLeg"].select = True
bpy.data.objects["RightLeg"].active_material.diffuse_color = (225/255,221/255,56/255)


for ob in bpy.context.scene.objects:
    if ob.type == "MESH":
        ob.select = True
        bpy.context.scene.objects.active = ob
    else:
        ob.select = False
bpy.ops.object.join()

bpy.ops.view3d.camera_to_view_selected()

origAlphaMode = bpy.data.scenes["Scene"].render.alpha_mode
bpy.data.scenes["Scene"].render.alpha_mode = "TRANSPARENT"
bpy.data.scenes["Scene"].render.alpha_mode = origAlphaMode
bpy.data.scenes["Scene"].render.filepath = "/var/www/html/images/4.png"
bpy.ops.render.render( write_still=True )

