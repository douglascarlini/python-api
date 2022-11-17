from common.repository import Repository
import bcrypt

class UserRepository(Repository):

    def __init__(self):

        super().__init__()
        self.name = "users"

    def create(self, data):

        data["salt"] = bcrypt.gensalt()
        byte = data["password"].encode("utf-8")
        data["password"] = bcrypt.hashpw(byte, data["salt"])

        data["password"] = str(data["password"].decode())
        data["salt"] = str(data["salt"].decode())

        return super().create(data)

    def update(self, data, where):

        data["salt"] = bcrypt.gensalt()
        byte = data["password"].encode("utf-8")
        data["password"] = bcrypt.hashpw(byte, data["salt"])

        data["password"] = str(data["password"].decode())
        data["salt"] = str(data["salt"].decode())

        return super().update(data, where)

    def getByUsername(self, value):

        return self.db.select(self.name, {"username": value}).run(True)
