# blenderToolkit: selectedFacesArea v1.1
# © 2020 enzyme42.com

import bpy
import bmesh

if bpy.context.edit_object:

    mesh = bpy.context.edit_object.data
    bm = bmesh.from_edit_mesh(mesh)

    area_sum = 0
    face_count = 0

    for face in bm.faces:
        if face.select:
            area_sum += face.calc_area()
            face_count += 1

    output = ["SELECTED FACES: %s" % face_count,
    "AVERAGE FACE AREA: %s m2" % (area_sum/face_count if face_count > 0 else 0),
    "TOTAL SELECTED AREA: %s m2" % area_sum]

    def popup(self, context):
        row = self.layout.row()
        row2 = self.layout.row()
        row3 = self.layout.row()
        row.label(text = output[0])
        row2.label(text = output[1])
        row3.label(text = output[2])

    bpy.context.window_manager.popup_menu(popup, title="[e42] selectedFacesArea", icon='INFO')

    print("\n[> e42] selectedFacesArea:\n\n%s\n%s\n\n%s\n\n[<]" % (output[0], output[1], output[2]))

else:

    print("\n[> e42] selectedFacesArea:\n\nERROR: This script only works in 'Edit Mode'.\n\n[<]")
