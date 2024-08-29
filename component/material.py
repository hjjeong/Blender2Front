class Material(): #Our data no texture information so basic texture information is assigned as default
    def __init__(self, uid='', aid=[], jid=[], texture='', normaltexture='',
                 color=[250, 249, 243, 255], seamWidth=0, useColor='true',
                 normalUVTransform = [1, 0, 0, 0, 1, 0, 0, 0, 1],
                 contentType = ["material", "wall paint - artistic"]):
        self.uid = uid
        self.aid = aid
        self.jid = jid
        self.texture = texture
        self.normaltexture = normaltexture
        self.color = color
        self.seamWidth = seamWidth
        self.useColor = useColor
        self.normalUVTransform = normalUVTransform
        self.contentType = contentType

    def to_dict(self):
        output = {}
        output['uid'] = self.uid
        output['aid'] = self.aid
        output['jid'] = self.jid
        output['texture'] = self.texture
        output['normaltexture'] = self.normaltexture
        output['color'] = self.color
        output['seamWidth'] = self.seamWidth
        output['useColor'] = self.useColor
        output['normalUVTransform'] = self.normalUVTransform
        output['contentType'] = self.contentType

        return output
