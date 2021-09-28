# blenderToolkit: selectedFacesArea v1.1

import bpy
import bmesh

area_sum = 0
face_count = 0
result = []
error = ""

def resultPopup(self, context):
    self.layout.row().label(text = result[0])
    self.layout.row().label(text = result[1])
    self.layout.separator()
    self.layout.row().label(text = result[2])

def errorPopup(self, context):
    self.layout.label(text = error)

if bpy.context.edit_object:

    mesh = bpy.context.edit_object.data
    bm = bmesh.from_edit_mesh(mesh)

    for face in bm.faces:

        if face.select:
            
            area_sum += face.calc_area()
            face_count += 1

    result = ["SELECTED FACES: %s" % face_count,
    "AVERAGE FACE AREA: %s m2" % (area_sum/face_count if face_count > 0 else 0),
    "TOTAL SELECTED AREA: %s m2" % area_sum]

    bpy.context.window_manager.popup_menu(resultPopup, title="[NERDSTERN] selectedFacesArea", icon='INFO')

    print("\n[> NERDSTERN] selectedFacesArea:\n\n%s\n%s\n\n%s\n\n[<]" % (result[0], result[1], result[2]))

else:

    error = "ERROR: This script only works in 'Edit Mode'."

    bpy.context.window_manager.popup_menu(errorPopup, title="[NERDSTERN] selectedFacesArea", icon='ERROR')

    print("\n[> NERDSTERN] selectedFacesArea:\n\n%s\n\n[<]" % error)
