from component.id_store import MeshIDStore
from component.object import Object

class Mesh(Object):
    def __init__(self, mesh_data, config_file, aid=[], jid='',
                 material='sge/a2d21b8d-50d4-408a-9982-5036982b8c6d/4850'):
        self.aid = aid
        self.jid = jid
        mesh_id_store = MeshIDStore(config_file)
        self.uid = str(mesh_id_store.generate_mesh_uid('mesh'))
        self.xyz = [round(float(vertex),3) for vertex in mesh_data['vertex']]
        self.normal = [round(float(normal), 3) for normal in mesh_data['normal']]
        self.uv = [round(float(uv),3) for uv in mesh_data['uvs']]
        self.faces = mesh_data['faces']
        self.material = material
        self.type = mesh_data['type']
        self.name = mesh_data['obj_name']

    def get_uid(self):
        return self.uid

    def get_name(self):
        return self.name

    def to_dict(self):
        mesh_dict = {}
        mesh_dict['aid'] = self.aid
        mesh_dict['jid'] = self.jid
        mesh_dict['uid'] = self.uid
        mesh_dict['xyz'] = self.xyz
        mesh_dict['normal']=self.normal
        mesh_dict['uv']=self.uv
        mesh_dict['faces']=self.faces
        mesh_dict['material']=self.material
        mesh_dict['type']=self.type

        return mesh_dict