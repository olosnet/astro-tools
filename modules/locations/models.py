from modules.base.models import BaseModel, BaseTable


class UserLocationsModel(BaseModel):

    id: int = None
    alias: str = None
    description: str = None
    longitude: str = None
    longitude_side: int = None  # 0 = E, 1 = W
    latitude: str = None
    latitude_side: int = None  # 0 = N, 1 = S
    altitude: float = None
    timezone: str = None
    city: str = None
    province: str = None
    state: str = None

    def to_arr(self, exclude=('id',)):
        return super().to_arr(exclude)


class UserLocationsTable(BaseTable):

    __table_name = 'user_locations'

    def __init__(self, connection):
        super().__init__(connection, self.__table_name)
        self.create()

    def create(self) -> None:
        query = '''CREATE TABLE IF NOT EXISTS "{}" (
	            "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                "alias"	TEXT NOT NULL,
	            "description"	TEXT,
	            "longitude"	TEXT NOT NULL,
                "longitude_side" INTEGER NOT NULL,
	            "latitude"	TEXT NOT NULL,
                "latitude_side" INTEGER NOT NULL,
	            "altitude"	REAL NOT NULL,
	            "city"	TEXT NOT NULL,
	            "province"	TEXT NOT NULL,
	            "state"	TEXT NOT NULL);'''. format(self.__table_name)

        self._run_query(query)

    def insert(self, data: UserLocationsModel) -> int:
        super()._insert(data)
        return self._cursor.lastrowid

    def update(self, id: int, data: UserLocationsModel) -> None:
        super()._update_by_id(id, data)

    def delete(self, id: int) -> None:
        super()._delete_by_id(id)

    def select_all(self) -> 'list[UserLocationsModel]':
        return super()._select_all(UserLocationsModel)
