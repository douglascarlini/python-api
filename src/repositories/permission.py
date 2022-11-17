from common.repository import Repository

class PermissionRepository(Repository):

    def __init__(self):

        super().__init__()
        self.name = "permissions"

    def getByName(self, value):

        return self.db.select(self.name, {"name": value}).run(True)
