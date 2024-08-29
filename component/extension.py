class Extension:
    def __init__(self, extension, room_id, type='interiorDoor', dir='outerRight', ref=['34577/model']):
        self.obj_name = extension['obj_name']
        self.type = type
        self.room_id = room_id
        self.dir = dir
        self.ref = ref

    def to_dict(self):
        instance = {}
        instance['type'] = self.type
        instance['roomId'] = self.room_id
        instance['dir'] = self.dir
        instance['ref'] = self.ref
        return instance