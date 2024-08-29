import argparse
import json
import os
import sys

from component.mesh import Mesh
from component.furniture import Furniture
from component.material import Material
from component.extension import Extension
from component.scene import Scene
from util import load_furniture_data, load_mesh_data, load_ext_data, load_scene_obj_data

import yaml

def main(argv):
    parser = argparse.ArgumentParser(
        description=("convert blender to 3D-FRONT file")
    )
    parser.add_argument(
        "--config_file",
        help="Path to a config file"
    )
    args = parser.parse_args(argv)
    config_file = args.config_file
    print(f'Loading config from {config_file}')
    with open(config_file) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    front_path = config['path']['front_path']
    furniture_path = config['path']['furniture_path']
    scene_info_path = config['path']['scene_info_path']

    print(f'front_path: {front_path}')
    print(f'furniture_path: {furniture_path}')
    print(f'scene_info_path: {scene_info_path}')

    room_name_list = os.listdir(scene_info_path)

    for room_name in room_name_list:
        print(f'room_name: {room_name}')
        scene_room_info = [{'room': room_name, 'type': 'LivingDiningRoom'}]

        #path for output files of the blender script
        fur_info_file = scene_info_path + room_name + '\\furdata_'+room_name+'.txt'
        mesh_info_file = scene_info_path + room_name + '\\meshdata_' + room_name + '.txt'
        ext_info_file = scene_info_path + room_name + '\\extensiondata_' + room_name + '.txt'
        scene_obj_info_file = scene_info_path + room_name + '\\sceneobjdata' + room_name + '.pickle'

        #load furniture data
        fur_data_list = load_furniture_data(fur_info_file)
        furniture_list = []
        for fur_data in fur_data_list:
            furniture = Furniture(fur_data, config_file)
            furniture_list.append(furniture)

        #load mesh data
        mesh_data_list = load_mesh_data(mesh_info_file)
        mesh_list = []
        for i in range(len(mesh_data_list)):
            mesh_data = mesh_data_list[i]
            mesh = Mesh(mesh_data, config_file)
            mesh_list.append(mesh)

        #set default values for material
        material = Material()

        #load extension data
        ext_data_list = load_ext_data(ext_info_file)
        ext_list = []
        if len(ext_data_list) > 0:
            for ext_data in ext_data_list:
                extension = Extension(ext_data, scene_room_info[0]['room'])
                ext_list.append(extension)

        #load scene component information
        scene_obj_info = load_scene_obj_data(scene_obj_info_file)

        #generate scene data
        scene = Scene(room_name, scene_room_info, scene_obj_info, furniture_list, mesh_list, material, ext_list, config_file)
        total_dict = scene.to_dict()
        with open(front_path + str(scene.get_uid()) + ".json", 'w') as f:
            json.dump(total_dict, f)

if __name__ == "__main__":
    main(sys.argv[1:])