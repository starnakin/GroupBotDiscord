class Group():

    def __init__(self, uuid, name, people, permissions, private=True):
        self.uuid=uuid
        self.name=name
        self.people=people
        self.permissions=permissions
        self.private=private
    
    def get_uuid(self):
        return self.uuid
    
    def set_uuid(self, uuid):
        self.uuid=uuid

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name=name

    def get_people(self):
        return self.people
    
    def set_people(self, people):
        self.people=people
    
    def get_permissions(self):
        return self.permissions
    
    def set_permissions(self, permissions):
        self.permission=permissions
    
    def is_private(self):
        return self.private

    def set_private(self, private):
        self.private=private

    def to_dictionnary(self):
        dictionnary={
            "uuid": self.uuid,
            "name": self.name,
            "people": self.people,
            "permissions": self.permissions,
            "private": self.private
        }
        return dictionnary

    def to_string(self):
        return str(self.to_dictionnary())

    @staticmethod
    def dictionnary_to_group(dictionnary):
        return Group(dictionnary.get("uuid"), dictionnary.get("name"), dictionnary.get("people"), dictionnary.get("permissions"), dictionnary.get("private"))