import psycopg2.extras
import uuid
import os

DIC = psycopg2.extras.RealDictCursor

class Database(object):

    def __init__(self):

        self.conn = psycopg2.connect(
            database=os.getenv('DB_NAME'),
            password=os.getenv('DB_PASS'),
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            port=os.getenv('DB_PORT')
        )
        self.cursor = None

    def insert(self, table, data):

        data = { k: v for k, v in data.items() if v is not None }

        data['uuid'] = str(uuid.uuid4())
        fields, values, tokens = self.extract_insert(data)
        sql = f"INSERT INTO {table} ({fields}) VALUES ({tokens})"
        self.execute(sql, values)
        return data['uuid']

    def update(self, table, data, where=None):

        if where is None: where = {'1': '1'}
        data = { k: v for k, v in data.items() if v is not None }
        where = { k: v for k, v in where.items() if v is not None }
        changes, filters, values = self.extract_update(data, where)
        where = f" WHERE {filters}" if len(filters) > 0 else ""
        sql = f"UPDATE {table} SET {changes}{where}"
        return self.execute(sql, values).cursor.rowcount

    def delete(self, table, where=None):

        if where is None: where = {'1': '1'}
        filters, values = self.extract_delete(where)
        where = f" WHERE {filters}" if len(filters) > 0 else ""
        sql = f"DELETE FROM {table}{where}"
        return self.execute(sql, values).cursor.rowcount

    def select(self, table, where=None, fields='*', limit=100, offset=0):

        if where is None: where = {'1': '1'}
        pg = f"LIMIT {limit} OFFSET {offset}"
        filters, values = self.extract_select(where)
        where = f" WHERE {filters}" if len(filters) > 0 else ""
        sql = f"SELECT {fields} FROM {table}{where} {pg}"
        return self.execute(sql, values).cursor.fetchall()

    def execute(self, sql, binds):

        cursor = self.conn.cursor(cursor_factory=DIC)
        cursor.execute(sql, binds)
        self.cursor = cursor
        self.conn.commit()
        return self

    def extract_insert(self, data):

        fields = [k for k, v in data.items()]
        values = [v for k, v in data.items()]
        tokens = ["%s" for k, v in data.items()]

        return ','.join(fields), values, ','.join(tokens)

    def extract_update(self, data, where):

        values = []

        for k, v in data.items(): values.append(v)
        for k, v in where.items(): values.append(v)

        changes = [f"{k} = %s" for k, v in data.items()]
        filters = [f"{k} = %s" for k, v in where.items()]

        return ','.join(changes), ' AND '.join(filters), values

    def extract_select(self, where):

        filters = []
        for k, v in where.items():
            if v is str and v.find('%') > -1:
                filters.append(f"{k} LIKE %s")
            else: filters.append(f"{k} =  %s")

        values = [v for k, v in where.items()]

        return ' AND '.join(filters), values

    def extract_delete(self, where):

        filters = [f"{k} = %s" for k, v in where.items()]
        values = [v for k, v in where.items()]

        return ' AND '.join(filters), values