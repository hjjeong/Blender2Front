class Object:
    def __init__(self, uid, jid, aid):
        self.uid = uid
        self.jid = jid
        self.aid = aid

    def to_dict(self):
        output = {}
        output['uid'] = self.uid
        output['jid'] = self.jid
        return output

    def __repr__(self):
        return f'Object(uid={self.uid},jid={self.jid},aid={self.aid})'
