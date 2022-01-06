import sqlite3
import os
from sqlite3.dbapi2 import Connection

class ProfileSettingsDB:

    __connection = None

    def __init__(self, db_path: str, filename = "profile.settings") -> None:
        self.__connection = sqlite3.connect(os.path.join(db_path, filename))

    def commit(self) -> None:
        self.__connection.commit()

    def connection(self) -> Connection:
        return self.__connection()

    def close(self) -> None:
        print("Close profile settings DB...")
        self.__connection.close()