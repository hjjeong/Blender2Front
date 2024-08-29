import json
import yaml
from util import load_furniture_data
import os
from constant import categories
import argparse
import sys

class ModelInfo:
    def __init__(self, model_id, super_cate, cate):
        self.model_id = model_id
        self.super_category = super_cate
        self.category = cate
        self.style = "Office"
        self.theme = None
        self.material = None

    def to_dict(self):
        model_info_dict = {}
        model_info_dict['model_id']=self.model_id
        model_info_dict['super-category']=self.super_category
        model_info_dict['category']=self.category
        model_info_dict['style']=self.style
        model_info_dict['theme']=self.theme
        model_info_dict['material']=self.material
        return model_info_dict

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

    fur_model_info = []
    fur_model_key = []

    for room_name in room_name_list:
        print('Room name: ' + room_name)
        fur_info_file = scene_info_path + room_name + '\\furdata_'+room_name+'.txt'

        fur_data_list = load_furniture_data(fur_info_file)

        for fur_data in fur_data_list:
            fur_jid = fur_data['fur_name'].split('-')[0]
            fur_cate = ''
            fur_supercate = ''
            cnt = 0
            for data in categories._CATEGORIES_3D:
                try:
                    if data['id'] == int(fur_data['fur_type']):
                        fur_supercate = data['super-category']
                        fur_cate = data['category'].lower()
                        break
                    elif cnt==len(categories._CATEGORIES_3D):
                        raise Exception('id: ' + str(data['id']) + ' fur_type: ' + str(fur_data['fur_type']))
                except Exception as e:
                    print('fur cate no exist', e)

                cnt += 1
            print(f'fur_jid: {fur_jid}, fur_cate:{fur_cate},fur_supercate:{fur_supercate}')
            model_info_data = ModelInfo(fur_jid, fur_cate, fur_supercate)
            fur_model_info.append(model_info_data.to_dict())
            fur_model_key.append(fur_jid)


    model_info_path = config['path']['model_info_path']
    with open(model_info_path, 'r') as model_info_json:
        model_info = json.load(model_info_json)

    print(f'fur_model_info: {fur_model_info}, len:{len(fur_model_info)}')
    model_info.extend(fur_model_info)

    model_info_modi_path = config['path']['model_info_modi_path']
    with open(model_info_modi_path, 'w') as f:
        json.dump(model_info, f)

if __name__ == "__main__":
    main(sys.argv[1:])