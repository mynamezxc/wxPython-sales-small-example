import sqlite3

class Database():
    db_path = "D://wx_de_an/database/sale.sqlite"
    def __init__(self):
        self.con = sqlite3.connect(self.db_path)

    def getAll(self):
        query = "SELECT * FROM {}".format(self.table)
        cursor = self.con.execute(query)
        results = cursor.fetchall()
        self.disconnect()
        return results
    
    def getWhere(self, condition):
        query = "SELECT * FROM {} WHERE {} {} {}".format(self.table, condition[0], condition[1], condition[2])
        cursor = self.con.execute(query)
        results = cursor.fetchall()
        self.disconnect()
        return results

    def getOne(self, query):
        cursor = self.con.execute(query)
        result = cursor.fetchone()
        self.disconnect()
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
        self.disconnect()
        return cursor.lastrowid

    def execute(self, query):
        cursor = self.con.execute(query)
        self.con.commit()
        self.disconnect()
        return cursor.rowcount
    
    def disconnect(self):
        self.con.close()