from component.id_store import UIDStore
from component.scene_object import SceneObject

class Scene():
    def __init__(self, room_name, scene_room_info, scene_obj_info, furniture_list,
                 mesh_list, material, ext_data_list, config_file,
                 jobid='',
                 design_version='1587242486510_95bdbafd-a8aa-419f-ae20-c3f6b18288ef',
                 code_version='0.11',
                 north_vector=[0,0,1]):
        self.uid = str(UIDStore(config_file).generate_uid(room_name))
        self.jobid = jobid
        self.design_version = design_version
        self.code_version = code_version
        self.north_vector = north_vector

        self.furniture_list = furniture_list
        self.mesh_list = mesh_list
        self.extension_list = ext_data_list
        self.material = material
        self.scene_obj = SceneObject(room_name, scene_room_info, scene_obj_info, furniture_list, mesh_list, config_file)

    def get_scene_obj(self):
        return self.scene_obj

    def get_uid(self):
        return self.uid

    def to_dict(self):
        output = {}
        output['uid'] = self.uid
        output['jobid'] = self.jobid
        output['design_version'] = self.design_version
        output['code_version'] = self.code_version
        output['north_vector'] = self.north_vector

        fur_dict_list = []
        for furniture in self.furniture_list:
            fur_dict_list.append(furniture.to_dict())
        output['furniture'] = fur_dict_list

        mesh_dict_list = []
        for mesh in self.mesh_list:
            mesh_dict_list.append(mesh.to_dict())
        output['mesh'] = mesh_dict_list

        material_dict_list = []
        material_dict_list.append(self.material.to_dict())
        output['material'] = material_dict_list

        ext_dict_list = []
        for ext in self.extension_list:
            ext_dict_list.append(ext.to_dict())

        ext_dict ={}
        ext_dict['door'] = ext_dict_list
        ext_dict['outdoor']=''
        ext_dict['pano']=[]
        ext_dict['mini_map']=''
        perspective_view = {}
        perspective_view['link'] = []
        ext_dict['perspective_view']= perspective_view
        ext_dict['area']=[]
        ext_dict['snapshots']=[]
        ext_dict['temperature']=5500
        skybox_dict ={}
        skybox_dict['name']=''
        skybox_dict['intensity']=1
        skybox_dict['rotationY']=0
        ext_dict['skybox']=skybox_dict
        output['extension'] = ext_dict

        output['scene'] = self.scene_obj.to_dict()

        return output
