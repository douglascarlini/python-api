from common.database import Database

class Repository(object):

    def __init__(self):

        self.name = None
        self.db = Database()

    def create(self, data):

        return self.db.insert(self.name, data)

    def search(self, data=None, pager=None):

        page = pager['page'] if pager is not None and 'page' in pager else 0
        rows = pager['rows'] if pager is not None and 'rows' in pager else 100
        return self.db.select(self.name, data, limit=rows, offset=page * rows)

    def delete(self, where):

        return self.db.delete(self.name, where)

    def update(self, data, where):

        return self.db.update(self.name, data, where)

    def getByUUID(self, value):

        result = self.search({'uuid': value})
        return result[0] if len(result) > 0 else None