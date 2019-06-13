import sqlite3

class Database():
    db_path = "D://wx_de_an/database/sale.sqlite"
    def __init__(self):
        self.con = sqlite3.connect(self.db_path)

    def getAll(self):
        query = "SELECT * FROM {}".format(self.table)
        cursor = self.con.execute(query)
        results = cursor.fetchall()
        return results
    
    def getWhere(self, condition, cols="*"):
        query = "SELECT {} FROM {} WHERE {} {} {}".format(cols, self.table, str(condition[0]), str(condition[1]), str(condition[2]))
        cursor = self.con.execute(query)
        results = cursor.fetchall()
        return results

    def getOne(self, query):
        cursor = self.con.execute(query)
        result = cursor.fetchone()
        return result
    
    def create(self, data):
        cols = ""
        vals = ""
        count = 1
        for key in data.keys():
            if count == len(data):
                cols += key
                vals += "'{}'".format(str(data[key]))
            else:
                cols += "{},".format(key)
                vals += "'{}',".format(str(data[key]))
            count += 1
        query = "INSERT INTO {} ({}) VALUES ({})".format(self.table, cols, vals)
        cursor = self.con.execute(query)
        self.con.commit()
        return cursor.lastrowid
    
    def deleteWhere(self, condition):
        query = "SELECT * FROM {} WHERE {} {} {}".format(self.table, str(condition[0]), str(condition[1]), str(condition[2]))
        self.con.execute(query)
        self.con.commit()
        return True

    def execute(self, query):
        cursor = self.con.execute(query)
        self.con.commit()
        return cursor.rowcount
    
    def disconnect(self):
        self.con.close()