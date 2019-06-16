import sqlite3
class Database():

    def __init__(self):
        self.file_db = "database\sale.db"
        self.con = sqlite3.connect(self.file_db)

    def getALL(self, chuoiSQL,btdk = ()):
        self.con = sqlite3.connect(self.file_db)
        cursor = self.con.execute(chuoiSQL,btdk)
        ds = cursor.fetchall()
        self.delConnect()
        return ds

    def getOne(self,chuoiSQL,btdk = ()):
        self.con = sqlite3.connect(self.file_db)
        cursor = self.con.execute(chuoiSQL,btdk)
        item = cursor.fetchone()
        self.delConnect()
        return item

    def execute(self, chuoiSQL,btdk = ()):
        self.con = sqlite3.connect(self.file_db)
        cursor = self.con.execute(chuoiSQL,btdk)
        self.con.commit()
        self.delConnect()
        return cursor.rowcount

    def execute1(self, chuoiSQL):
        self.con = sqlite3.connect(self.file_db)
        cursor = self.con.execute(chuoiSQL)
        self.con.commit()
        self.delConnect()
        return cursor.rowcount
        

    def execute2(self, chuoiSQL):
        self.con = sqlite3.connect(self.file_db)
        cursor = self.con.execute(chuoiSQL)
        item = cursor.fetchone()
        self.delConnect()
        return item

    def delConnect(self):
        self.con.close()