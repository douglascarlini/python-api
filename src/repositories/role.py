from common.repository import Repository

class RoleRepository(Repository):

    def __init__(self):

        super().__init__()
        self.name = "roles"

    def getByName(self, value):

        return self.db.select(self.name, {"name": value}).run(True)
