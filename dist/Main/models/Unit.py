from models.database import *

class Unit(Database):

    def DanhSach(self):
        chuoiSQL = "select ID, unit_code,unit_name from units"
        cursor = Database.getALL(self,chuoiSQL)
        if cursor != None:    
            recordList = []
            for row in cursor:
                TT = {'ID':row[0], 'unit_code': row[1], 'unit_name':row[2]}
                recordList.append(TT)
        return recordList

    def Insert(self, Ma,Ten):
        chuoiSQL = "insert into units (unit_code,unit_name) values(?,?)"
        kq = Database.execute(self,chuoiSQL,(Ma,Ten))
        return kq

    def Update(self,Id, Ma,Ten):
        chuoiSQL = "update units set unit_code = ?, unit_name = ? where ID = ?"
        kq = Database.execute(self,chuoiSQL,(Ma,Ten,Id))
        return kq

    def Delete(self,Id):
        chuoiSQL = "delete from units where ID =  ? " 
        kq = Database.execute(self,chuoiSQL,(Id,))
        return kq
