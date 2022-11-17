from common.repository import Repository

class RolePermissionRepository(Repository):

    def __init__(self):

        super().__init__()
        self.gen_uuid = False
        self.name = "role_permission"
