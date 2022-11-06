from common.database import DB

class Repository(object):

    def __init__(self):

        self.db = DB()
        self.name = None

    def create(self, data):

        return self.db.insert(self.name, data).run()

    def search(self, data=None, pager=None):

        page = pager["page"] if pager is not None and "page" in pager else 0
        rows = pager["rows"] if pager is not None and "rows" in pager else 100

        return self.db.select(self.name, data).limit(limit=rows, offset=page * rows).run()

    def delete(self, where):

        return self.db.delete(self.name, where).run()

    def update(self, data, where):

        return self.db.update(self.name, data, where).run()

    def getByUUID(self, value):

        return self.db.select(self.name, {"uuid": value}).run(True)