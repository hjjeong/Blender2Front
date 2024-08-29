from component.room_object import Room

class SceneObject:
    def __init__(self, room_name, scene_room_info, scene_obj_info, furniture_list, mesh_list, config_file,
                 ref=-1, pos=[0,0,0], rot=[0,0,0,0],scale=[1,1,1],room_list=[]):
        self.ref = ref
        self.pos = pos
        self.rot = rot
        self.scale = scale
        self.room_list = room_list
        for scene_room in scene_room_info:
            room = Room(room_name, scene_room, scene_obj_info, furniture_list, mesh_list, config_file)
            self.room_list.append(room)

    def get_room_obj_list(self, idx):
        return self.room_list[idx]

    def to_dict(self):
        output = {}
        output['ref'] = self.ref
        output['pos'] = self.pos
        output['rot'] = self.rot
        output['scale'] = self.scale

        room_dict_list = []
        for room in self.room_list:
            room_dict_list.append(room.to_dict())
        output['room'] = room_dict_list

        return output