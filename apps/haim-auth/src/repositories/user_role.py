from common.repository import Repository

class UserRoleRepository(Repository):

    def __init__(self):

        super().__init__()
        self.gen_uuid = False
        self.name = "user_role"
