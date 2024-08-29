from constant import categories
from component.id_store import FIDStore, CIDStore

class Furniture:
    def __init__(self, fur_data, config_file, aid=[], cateid='', title=''):
        fid_store = FIDStore(config_file)
        self.uid = str(fid_store.generate_fid())
        self.jid = fur_data['fur_name'].split('-')[0]
        self.aid = aid
        self.cateid = cateid
        self.title = title

        for data in categories._CATEGORIES_3D:
            if data['id'] == int(fur_data['fur_type']):
                self.cateid = data['id']
                self.category = data['super-category'].lower()+'/'+data['category'].lower()
                break

        if self.cateid == '':
            print('id: ' + str(data['id']) + ' fur_type: ' + str(fur_data['fur_type']))
            raise

        self.size = fur_data['fur_bbox']

        cid_store = CIDStore()
        self.sourceCategoryId = cid_store.generate_cid(self.cateid)
        self.bbox = fur_data['fur_bbox']
        self.valid = True
        self.name = fur_data['fur_name']

    def get_uid(self):
        return self.uid

    def get_name(self):
        return self.name

    def get_jid(self):
        return self.jid

    def get_category(self):
        return self.category

    def to_dict(self):
        fur_dict = {}
        fur_dict['uid'] = self.uid
        fur_dict['jid'] = self.jid
        fur_dict['aid'] = self.aid
        fur_dict['size'] = self.size
        fur_dict['sourceCateogryId'] = self.sourceCategoryId
        fur_dict['title'] = self.title
        fur_dict['category'] = self.category
        fur_dict['bbox'] = self.bbox
        fur_dict['valid'] = self.valid

        return fur_dict
