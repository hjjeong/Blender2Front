import hashlib
import uuid
import os
import yaml
import json

class UIDStore: #scene uid
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(UIDStore, cls).__new__(cls)
            cls._instance._uids = {}
            cls._instance._next_id = 0
        return cls._instance

    def __init__(self, config_file):
        prev_uids = PreviousIDManager(config_file).get_prev_uids()

        for uid in prev_uids:
            if uid not in self._uids.values():
                self._uids[self._next_id] = uid
                self._next_id += 1

    def generate_uid(self, scene_folder_name):
        input = str('uid'+str(scene_folder_name))

        while True:
            uid = uuid.uuid4()
            if uid not in self._uids.values():
                self._uids[self._next_id] = uid
                self._next_id += 1
                break

        return uid

    def get_uid(self, idx):
        return self._uids.get(idx)

    def remove_uid(self, idx):
        if idx in self._uids.keys():
            del self._uids[idx]

class MaterialIDStore: #material id
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MaterialIDStore, cls).__new__(cls)
            cls._instance._material_uids = {}
            cls._instance._next_id = 0
        return cls._instance

    def __init__(self, config_file):
        prev_material_ids = PreviousIDManager(config_file).get_prev_material_uids()

        for material_uid in prev_material_ids:
            if material_uid not in self._material_uids.values():
                self._material_uids[self._next_id] = material_uid
                self._next_id += 1

    def generate_material_uid(self, data_type):
        input = data_type+str(self._next_id)
        while True:
            material_uid = uuid.uuid4()
            if material_uid not in self._material_uids.values():
                self._material_uids[self._next_id] = material_uid
                self._next_id +=1
                break

        return material_uid

    def get_material_uid(self, idx):
        return self._material_uids.get(idx)

    def remove_material_uid(self, idx):
        if idx in self._material_uids.keys():
            del self._material_uids[idx]

class MeshIDStore: #mesh id
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MeshIDStore, cls).__new__(cls)
            cls._instance._meshids = {}
            cls._instance._next_id = 0
        return cls._instance

    def __init__(self, config_file):
        prev_mesh_uids = PreviousIDManager(config_file).get_prev_mesh_uids()

        for mesh_uid in prev_mesh_uids:
            if mesh_uid not in self._meshids.values():
                self._uids[self._next_id] = mesh_uid
                self._next_id += 1

    def generate_mesh_uid(self, data_type):
        input = data_type + str(self._next_id)
        while True:
            mesh_uid = uuid.uuid4()
            if mesh_uid not in self._meshids.values():
                self._meshids[self._next_id] = mesh_uid
                self._next_id += 1
                break
        return mesh_uid

    def get_mesh_id(self, idx):
        return self._meshids.get(idx)

    def remove_mesh_id(self, idx):
        if idx in self._meshids.keys():
            del self._meshids[idx]


class RIDStore: #room id
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(RIDStore, cls).__new__(cls)
            cls._instance._rids = {}
            cls._instance._next_id = 0
        return cls._instance

    def __init__(self, config_file):
        prev_room_ids = PreviousIDManager(config_file).get_prev_room_instanceids()

        for rid in prev_room_ids:
            if rid not in self._rids.values():
                self._rids[self._next_id] = rid
                self._next_id += 1

    def generate_rid(self, room_type, room_name):
        rid = str(room_type)+str(room_name) #filename으로 변경
        if rid not in self._rids.values():
            self._rids[self._next_id] = rid
            self._next_id +=1
        else:
            print("room instanceid is already in use")
        return rid

    def get_rid(self, idx):
        return self._rids.get(idx)

    def remove_rid(self, idx):
        if idx in self._rids.keys():
            del self._rids[idx]


class ROIDStore: #room component instance id
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ROIDStore, cls).__new__(cls)
            cls._instance._roids = {}
            cls._instance._next_id = 0
        return cls._instance

    def __init__(self, config_file):
        prev_room_obj_ids = PreviousIDManager(config_file).get_room_obj_instanceid()

        for roid in prev_room_obj_ids:
            if roid not in self._roids.values():
                self._roids[self._next_id] = roid
                self._next_id += 1

    def generate_roid(self):
        roid = self._next_id # 새로 만든 데이터 10만부터 시작
        if roid not in self._roids.values():
            self._roids[self._next_id] = roid
            self._next_id +=1
        else:
            print("ROID instanceid is already in use")
        return roid

    def get_roid(self, idx):
        return self._roids.get(idx)

    def remove_roid(self, idx):
        if idx in self._roids.keys():
            del self._roids[idx]

class FIDStore: #furniture instance id
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(FIDStore, cls).__new__(cls)
            cls._instance._fids = {}
            cls._instance._next_id = 0
        return cls._instance

    def __init__(self, config_file):
        prev_fur_uids = PreviousIDManager(config_file).get_prev_fur_uids()
        for fur_uid in prev_fur_uids:
            if fur_uid not in self._fids.values():
                self._fids[self._next_id] = fur_uid
                self._next_id += 1

    def generate_fid(self):
        fid = str(self._next_id)+'/model'
        if fid not in self._fids.values():
            self._fids[self._next_id] = fid
            self._next_id +=1
        else:
            print("FID "+str(fid)+"instanceid is already in use")
        return fid

    def get_fid(self, idx):
        return self._fids.get(idx)

    def remove_fid(self, idx):
        if idx in self._fids.keys():
            del self._fids[idx]

class MIDStore: #room component instance id
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MIDStore, cls).__new__(cls)
            cls._instance._mids = {}
            cls._instance._next_id = 0
        return cls._instance

    def __init__(self, config_file):
        prev_material_uids = PreviousIDManager(config_file).get_prev_material_uids()
        for mid in prev_material_uids:
            if mid not in self._mids.values():
                self._mids[self._next_id] = mid
                self._next_id += 1

    def generate_mid(self):
        mid = uuid.uuid4() # 새로 만든 데이터 10만부터 시작
        if mid not in self._mids.values():
            self._mids[self._next_id] = mid
            self._next_id +=1
        else:
            print("MID "+str(mid)+" instanceid is already in use")
        return mid

    def get_mid(self, idx):
        return self._mids.get(idx)

    def remove_mid(self, idx):
        if idx in self._mids.keys():
            del self._mids[idx]

class CIDStore: #category id store
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CIDStore, cls).__new__(cls)
            cls._instance._cids = {}
            cls._instance._next_id = 0
        return cls._instance

    def generate_cid(self, cate_id):
        while True:
            cid = hashlib.sha256(str(cate_id).encode()).hexdigest()
            cate_id = str(cate_id) +'a'

            if cid not in self._cids.values():
                self._cids[self._next_id] = cid
                self._next_id +=1
                break

        return cid

    def get_cid(self, idx):
        return self._cids.get(idx)

    def remove_cid(self, idx):
        if idx in self._cids.keys():
            del self._cids[idx]


class PreviousIDManager:
    def __init__(self, config_file):
        self.config_path = config_file
        print('previous id manager: '+str(config_file))
        with open(self.config_path) as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)

        self.front_path = self.config['path']['front_path']
        self.furniture_path = self.config['path']['furniture_path']

        self.prev_uids = []
        self.prev_material_uids = []
        self.prev_material_jids = []
        self.prev_mesh_uids=[]
        self.prev_room_instanceids=[]
        self.prev_fur_uids=[]
        self.prev_fur_jids=[]
        self.prev_obj_ref_to_instanceid = {}

        self.store_prev_all_ids()

    def store_prev_uids(self):
        self.prev_uids = os.listdir(self.front_path)
    def load_front_instance(self, front_file_path):
        with open(front_file_path, 'r') as file:
            data = json.load(file)
            self.scene = data['scene']
            self.fur_list = data['furniture']
            self.mesh_list = data['mesh']
            self.materials = data['material']
            self.room = self.scene['room']

        for fur_info in self.fur_list:
            self.prev_fur_uids.append(fur_info['uid'])
            self.prev_fur_jids.append(fur_info['jid'])

        for mesh_info in self.mesh_list:
            self.prev_mesh_uids.append(mesh_info['uid'])

        for material_info in self.materials:
            self.prev_material_jids.append(material_info['jid'])
            self.prev_material_uids.append(material_info['uid'])

        for room_info in self.room:
            self.prev_room_instanceids.append(room_info['instanceid'])

            child_obj = room_info['children']
            for obj_info in child_obj:
                if obj_info['ref'] not in self.prev_obj_ref_to_instanceid:
                    self.prev_obj_ref_to_instanceid[obj_info['ref']] = obj_info['instanceid'].split('/')[0]


    def store_prev_all_ids(self):
        for front_file in self.prev_uids:
            self.load_front_instance(front_file)

    def get_prev_uids(self):
        return self.prev_uids

    def get_prev_material_uids(self):
        return self.prev_material_uids

    def get_prev_material_jids(self):
        return self.prev_material_jids

    def get_prev_mesh_uids(self):
         return self.prev_mesh_uids

    def get_prev_room_instanceids(self):
        return self.prev_room_instanceids

    def get_prev_fur_uids(self):
        return self.prev_fur_uids

    def get_prev_fur_jids(self):
        return self.prev_fur_jids

    def get_obj_ref_to_instanceid(self):
        return self.prev_obj_ref_to_instanceid

    def get_room_obj_instanceid(self):
        return self.prev_obj_ref_to_instanceid.values()
