from common.repository import Repository
import bcrypt

class UserRepository(Repository):

    def __init__(self):

        super().__init__()
        self.name = 'users'

    def create(self, data):

        data['salt'] = bcrypt.gensalt()
        byte = data['password'].encode('utf-8')
        data['password'] = bcrypt.hashpw(byte, data['salt'])

        data['password'] = str(data['password'].decode())
        data['salt'] = str(data['salt'].decode())

        return super().create(data)

    def getByUsername(self, value):

        result = self.search({'username': value})
        return result[0] if len(result) > 0 else None
