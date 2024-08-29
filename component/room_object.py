from constant.type_constant import RoomTypeConstant
from constant.type_constant import TypeConstant
from component.id_store import RIDStore, ROIDStore
import util
import numpy as np

class RoomObject():
    def __init__(self, name, pos, rot, scale, furniture_list, mesh_list, config_file):
        self.pos = pos
        self.rot = rot
        self.scale = scale
        self.instance_id = ''
        self.ref = util.get_uid_from_obj(name, furniture_list, mesh_list)
        if self.ref == "":
            print(f'Room object ref is error: {name}')

        self.name = name
        if self.name.lower() in ['ceiling','floor','wall','door']:
            self.type = TypeConstant.MESH.value
        else:
            self.type = TypeConstant.FURNITURE.value

        print(f'Room object ref name: {self.name}, type: {self.type}')
        roid_store = ROIDStore(config_file)

        self.instance_id = str(self.type)+'/'+str(roid_store.generate_roid())

    def to_dict(self):
        output = {}
        output['ref'] = self.ref
        output['pos'] = self.pos
        output['rot'] = self.rot
        output['scale'] = self.scale
        output['instanceid'] = self.instance_id
        return output

class Room:
    def __init__(self, room_name, scene_room_info, scene_obj_info, furniture_list, mesh_list, config_file, pos=[0,0,0],rot=[0,0,0,0],scale=[1,1,1], size=6.12, ref=[0,0,1]):
        self.pos = pos
        self.rot = rot
        self.scale = scale
        self.size = size
        self.ref = ref
        self.room_obj_list = []

        self.furniture_list = furniture_list
        self.mesh_list = mesh_list
        self.config_file = config_file
        if scene_room_info['type']=='LivingDiningRoom':
            self.type = str(RoomTypeConstant.LIVING_ROOM.value)
        elif scene_room_info['type']=='BedRoom':
            self.type = str(RoomTypeConstant.BEDROOM.value)

        rid = RIDStore(config_file).generate_rid(self.type, room_name)
        self.instanceid = self.type+'-'+str(rid)

        for obj_name in scene_obj_info.keys():
            if 'door' in obj_name.lower():
                continue

            scene_obj_info_list = scene_obj_info[obj_name]
            for scene_obj in scene_obj_info_list:
                rot_data = scene_obj['rot']

                #check whether rot information is correct or not
                axis = np.cross(self.ref, scene_obj['rot'][1:])
                if np.dot(axis, [1,0,1]) != 0:
                    print(f'z axis error check: {room_name}, {obj_name}'+str(scene_obj['rot']))
                    rot_data[0] = scene_obj['rot'][0]
                    for idx in range(len(scene_obj['rot'][1:])):
                        if abs(scene_obj['rot'][1:][idx]) < 0.0001:
                            rot_data[idx+1] = 0
                    print(f'z axis modi check: {room_name}, {obj_name}' + str(rot_data))
                axis = np.cross(ref, rot_data[1:])
                if np.dot(axis, [1, 0, 1]) != 0:
                    print(f'z axis no fixed')
                roomobj = RoomObject(obj_name, scene_obj['pos'],rot_data,scene_obj['scale'], self.furniture_list,
                                     self.mesh_list, self.config_file)
                if roomobj.ref == "":
                    continue
                self.room_obj_list.append(roomobj)

    def get_room_obj_list(self):
        return self.room_obj_list

    def to_dict(self):
        output = {}
        output['type '] = self.type
        output['instanceid'] = self.instanceid
        output['size'] = self.size
        output['pos'] = self.pos
        output['rot'] = self.rot
        output['scale'] = self.scale

        room_obj_dict_list = []
        for room_obj in self.room_obj_list:
            room_obj_dict_list.append(room_obj.to_dict())

        output['children'] = room_obj_dict_list

        return output