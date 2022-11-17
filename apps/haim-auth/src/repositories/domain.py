from common.repository import Repository

class DomainRepository(Repository):

    def __init__(self):

        super().__init__()
        self.name = "domains"

    def getByName(self, value):

        return self.db.select(self.name, {"name": value}).run(True)
