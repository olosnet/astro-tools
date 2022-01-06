from modules.base.models import BaseTable

class ProfilesTable(BaseTable):

    __table_name = 'profiles'

    def __init__(self, connection):
        super().__init__(connection, self.__table_name)
        self.create()