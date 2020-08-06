# blenderToolkit: selectedFacesArea v1.0
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

    print("\n[> e42] selectedFacesArea:\n\nSELECTED FACES: %s\nAVERAGE FACE AREA: %s m2\n\nTOTAL SELECTED AREA: %s m2\n\n[<]" % (face_count, area_sum/face_count if face_count > 0 else 0, area_sum))

else:

    print("\n[> e42] selectedFacesArea:\n\nERROR: This script only works in 'Edit Mode'.\n\n[<]")
