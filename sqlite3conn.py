from dbconnbase import DBConnBase

class Sqlite3Conn(DBConnBase):
    def connect(self):
        pass

    def get_cursor(self):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass

if __name__ == '__main__':
    s = Sqlite3Conn()
