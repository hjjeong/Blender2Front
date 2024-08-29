import pickle

def get_uid_from_obj(room_obj_name, furniture_list, mesh_list):
    uid = ''
    for furniture in furniture_list:
        fur_name = room_obj_name.split('_')[0]
        if fur_name in furniture.get_name():
            uid = furniture.get_uid()

    for mesh in mesh_list:
        if room_obj_name in mesh.get_name():
            uid = mesh.get_uid()

    return uid

def load_mesh_data(filename):
    mesh_data_list = []
    mesh_temp = {}
    cnt = 1
    f = open(filename, 'r')
    for line in f.readlines():
        data = line.split(':')
        key = data[0]
        value = data[1]

        if key == 'obj_name':
            mesh_temp['obj_name'] = value.split('\n')[0]
        if key=='type':
            mesh_temp['type'] = value.split('\n')[0]
        if key=='vertex':
            mesh_temp['vertex']=preprocessing_xyz(value)
        if key=='normals':
            mesh_temp['normal']=preprocessing_normal(value)
        if key=='uvs':
            mesh_temp['uvs']=preprocessing_uv(value)
        if key == 'faces':
            mesh_temp['faces'] = preprocessing_faces(value)

        if cnt != 1 and cnt % 6 == 0:
            if len(mesh_data_list) == 0:
                mesh_data_list= [mesh_temp]
            else:
                mesh_data_list.append(mesh_temp)
            mesh_temp = {}
        cnt+=1
    return mesh_data_list

def load_furniture_data(filename):
    f = open(filename, 'r')

    fur_data_list = []
    for line in f.readlines():
        fur_data = {}
        data = line.split(':')
        fur_name = data[0]
        fur_type = data[1]
        fur_bbox = [float(value) for value in data[2].split('\n')[0].split(',')]
        fur_data['fur_name']=fur_name
        fur_data['fur_type']=fur_type
        fur_data['fur_bbox']=fur_bbox
        fur_data_list.append(fur_data)

    return fur_data_list

def load_scene_obj_data(filename):
    f = open(filename,'rb')
    scene_obj_data = pickle.load(f)

    delete_key_list = []
    for key in scene_obj_data.keys():
        if 'room' in key.lower():
            delete_key_list.append(key)

    for key in delete_key_list:
        scene_obj_data.pop(key)

    return scene_obj_data

def load_ext_data(filename):
    ext_data_list = []
    ext_temp = {}
    cnt = 0
    try:
        f = open(filename, 'r')
    except IOError as e:
        return ext_data_list

    for line in f.readlines():
        data = line.split(':')
        key = data[0]
        value = data[1]
        if key == 'obj_name':
            ext_temp[key] = value

        if cnt % 6 == 0 and cnt != 0 :
            ext_data_list.append(ext_temp)
            ext_temp = {}

        cnt+=1

    return ext_data_list


def preprocessing_xyz(xyz):
    preprocessed_xyz = xyz.replace('[','').replace('(','').replace(')','').replace(']','')
    preprocessed_xyz_list = preprocessed_xyz.split(',')
    preprocessed_xyz_list = [float(value) for value in preprocessed_xyz_list]
    return preprocessed_xyz_list

def preprocessing_normal(normal):
    preprocessed_normal = normal.replace('[', '').replace('Vector','').replace('(', '').replace(')', '').replace(']', '')
    preprocessed_normal_list = preprocessed_normal.split(',')
    preprocessed_normal_list = [float(value) for value in preprocessed_normal_list]
    return preprocessed_normal_list

def preprocessing_uv(uv):
    preprocessed_uv = uv.replace('[', '').replace('Vector','').replace('(', '').replace(')', '').replace(']', '')
    preprocessed_uv_list = preprocessed_uv.split(',')
    preprocessed_uv_list = [float(value) for value in preprocessed_uv_list]
    return preprocessed_uv_list

def preprocessing_faces(faces):
    preprocessed_faces = faces.replace(', [...],','').replace('[', '').replace('Vector','').replace('(', '').replace(')', '').replace(']', '').replace('...','').replace(' ','').replace('\n','')

    preprocessed_faces_list = preprocessed_faces.split(',')
    preprocessed_faces_list = [int(value) for value in preprocessed_faces_list]
    return preprocessed_faces_list
