from common.repository import Repository

class RoleRepository(Repository):

    def __init__(self):

        super().__init__()
        self.name = 'roles'

    def getByName(self, value):

        result = self.search({'name': value})
        return result[0] if len(result) > 0 else None
