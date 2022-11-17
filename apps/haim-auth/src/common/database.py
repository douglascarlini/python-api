from uuid import uuid4
import psycopg2.extras
import os

DIC = psycopg2.extras.RealDictCursor

class DB(object):

    def __init__(self, dbhost='localhost', dbport=5432, dbuser='root', dbpass='123456', dbname='app'):

        self.query = ""
        self.binds = []
        self.conn = None
        self.uuid = None
        self.cursor = None
        self.whereInit = False
        self.orderInit = False

        self.conn = psycopg2.connect(
            database=os.getenv('DB_NAME') or dbname,
            password=os.getenv('DB_PASS') or dbpass,
            host=os.getenv('DB_HOST') or dbhost,
            user=os.getenv('DB_USER') or dbuser,
            port=os.getenv('DB_PORT') or dbport
        )

    def run(self, one=False):

        self.execute()

        cmd = self.query[0:6]
        if cmd == "INSERT": return self.uuid
        elif cmd == "UPDATE": return self.rowcount()
        elif cmd == "DELETE": return self.rowcount()
        elif cmd == "SELECT": return self.fetchone() if one else self.fetchall()

    def rowcount(self): return self.cursor.rowcount
    def fetchone(self): return self.cursor.fetchone()
    def fetchall(self): return list(self.cursor.fetchall())

    def execute(self):

        cursor = self.conn.cursor(cursor_factory=DIC)
        cursor.execute(self.query, self.binds)
        self.cursor = cursor
        self.conn.commit()
        return self

    def insert(self, table, data, gen_uuid=True):

        if type(data) is not dict or data == {}: return

        if gen_uuid:

            self.uuid = str(uuid4())
            data['uuid'] = self.uuid

        for k, v in data.items():
            if v is not None: self.binds.append(v)
        fields = [k for k, v in data.items() if v is not None]
        tokens = ["%s" for k, v in data.items() if v is not None]

        self.query = f"INSERT INTO {table} ({', '.join(fields)}) VALUES ({', '.join(tokens)})"

        return self

    def update(self, table, data, conditions=None):

        if type(conditions) is not dict or conditions == {}: conditions = None

        for k, v in data.items():
            if v is not None: self.binds.append(v)
        fields = [f"{k} = %s" for k, v in data.items() if v is not None]

        self.query = f"UPDATE {table} SET {', '.join(fields)}"

        if conditions is not None:
            conditions = self._extract_conditions(conditions)
            self.query = f"{self.query} WHERE ({conditions})"

        return self

    def delete(self, table, conditions=None):

        if type(conditions) is not dict or conditions == {}: conditions = None

        self.query = f"DELETE FROM {table}"

        if conditions is not None:
            conditions = self._extract_conditions(conditions)
            self.query = f"{self.query} WHERE ({conditions})"

        return self

    def select(self, table, conditions=None, fields='*'):

        if type(conditions) is not dict or conditions == {}: conditions = None

        fields = self._extract_fields(fields)
        self.query = f"SELECT {fields} FROM {table}"

        if conditions is not None:
            conditions = self._extract_conditions(conditions)
            self.query = f"{self.query} WHERE ({conditions})"

        return self

    def join(self, table, conditions=None):

        if type(conditions) is not dict or conditions == {}: conditions = None

        self.query = f"{self.query} JOIN {table} ON ({self._extract_conditions(conditions)})"

        return self

    def cond(self, field, value=None, op="=", mode="AND"):

        if value is None:

            conditions = self._extract_conditions(field)
            self.query = f"{self.query} {mode.upper()} ({conditions})"

        else:

            self.binds.append(value)
            self.query = f"{self.query} {mode.upper()} ({field} {op.upper()} %s)"

        return self

    def where(self, field, value=None, op="=", mode="AND"):

        if value is None:

            conditions = self._extract_conditions(field)

            if self.whereInit:
                self.query = f"{self.query} AND ({conditions})"
            else:
                self.query = f"{self.query} WHERE ({conditions})"

        else:

            self.binds.append(value)

            if self.whereInit:
                self.query = f"{self.query} {mode.upper()} ({field} {op.upper()} %s)"
            else:
                self.query = f"{self.query} WHERE ({field} {op.upper()} %s)"

        self.whereInit = True

        return self

    def order(self, order=None):

        if order is None: return self

        order = self._extract_orders(order)

        if not self.orderInit:
            self.query = f"{self.query} ORDER BY {order}"
        else:
            self.query = f"{self.query}, {order}"

        self.orderInit = True

        return self

    def limit(self, limit=100, offset=0):

        self.query = f"{self.query} LIMIT {limit} OFFSET {offset}"

        return self

    def _extract_fields(self, fields):

        if type(fields) is str:
            return fields

        elif type(fields) is list:
            return ', '.join(fields)

        elif type(fields) is dict:
            return ', '.join([f"{b} AS {a}" for a, b in fields.items()])

    def _extract_orders(self, orders):

        if type(orders) is str:
            return orders

        elif type(orders) is list:
            return ', '.join(orders)

        elif type(orders) is dict:
            for mode, order in orders.items():
                result.append(f"{order} {mode.upper()}")
            return ', '.join(result)

    def _extract_conditions(self, conditions):

        result = []

        if type(conditions) is dict:

            for i, (field, value) in enumerate(conditions.items()):

                self.binds.append(value)

                parts = field.split(' ')
                op = parts[1] if len(parts) > 1 else "="
                result.append(f"{parts[0]} {op.upper()} %s")

        return ' AND '.join(result)

    def _valid_conditions(self, data):

        if type(conditions) is int or type(conditions) is float: conditions = None
        if type(conditions) is list and len(conditions) == 0: conditions = None
        if type(conditions) is dict and conditions == {}: conditions = None
        if type(conditions) is str and conditions == '': conditions = None

        return True if conditions is not None else False