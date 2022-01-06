from abc import abstractmethod
import sqlite3

from .common import eprint


class BaseModel:

    def to_arr(self, exclude: list):

        attribs = [attr for attr in dir(self) if not callable(
            getattr(self, attr)) and not attr.startswith("__") and attr not in exclude]
        values = [getattr(self, attr) for attr in attribs]
        return attribs, values


class BaseTable:

    _connection = None
    _cursor = None
    _table_name = None

    def __init__(self, connection, table_name: str) -> None:
        self._connection = connection
        self._cursor = self._connection.cursor()
        self._table_name = table_name

    @abstractmethod
    def create(self) -> None:
        pass

    def _run_query(self, query) -> None:

        try:
            self._cursor.execute(query)

        except sqlite3.Error as error:
            qerr_str = "Query execution error ({}) :".format(query)
            eprint(qerr_str, error)

    def _insert(self, model: BaseModel) -> None:

        attribs, values = model.to_arr()
        attrib_list = ','.join(attribs)
        values_el = ','.join(['?' for l in range(len(attribs))])

        query = ''' INSERT INTO {} ({})
                    VALUES ({});
                '''.format(self._table_name, attrib_list, values_el)

        self._insert_query(query, values)

    def _update_by_id(self, id: int, model: BaseModel):

        attribs, values = model.to_arr()
        attrib_list = (' = ? , '.join(attribs)) + ' = ?'
        values.append(id)

        query = ''' UPDATE {} SET {} WHERE id = ?'''.format(self._table_name, attrib_list)

        try:
            self._cursor.execute(query, values)

        except sqlite3.Error as error:
            qerr_str = "Update execution error ({}) :".format(query)
            eprint(qerr_str, error)

    def _delete_by_id(self, id: int):

        query = '''DELETE FROM {} WHERE id=?'''.format(self._table_name)

        try:
            self._cursor.execute(query, (id,))

        except sqlite3.Error as error:
            qerr_str = "Delete execution error ({}) :".format(query)
            eprint(qerr_str, error)



    def _insert_query(self, query, data) -> None:

        try:
            self._cursor.execute(query, data)

        except sqlite3.Error as error:
            qerr_str = "Insert execution error ({}) :".format(query)
            eprint(qerr_str, error)

    def _select_all(self, bmodel: BaseModel):

        model = bmodel()
        attribs, values = model.to_arr(exclude=())
        attrib_list = ','.join(attribs)
        query = ''' SELECT {} FROM {}'''.format(attrib_list, self._table_name)
        self._run_query(query)
        records = self._cursor.fetchall()

        res = []

        for row in records:
            curr_model = bmodel()
            i = 0
            for current in attribs:
                setattr(curr_model, current, row[i])
                res.append(curr_model)
                i += 1

        return res

    def exists(self) -> bool:
        result = False

        try:

            query = "SELECT name FROM sqlite_master WHERE type='table' AND name='{};".format(
                self._table_name)

            self._cursor.execute(query)
            result = len(self._cursor.fetchall()) >= 1

        except sqlite3.Error as error:
            eprint("Can't verify if table exists: ", error)

        return result

    def truncate(self) -> None:
        self.drop()
        self.create()

    def drop(self) -> None:
        query = "DROP TABLE {};".format(self._table_name)
