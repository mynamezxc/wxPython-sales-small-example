from models.database import *

class StaffModel(Database):
    # def __init__(self):
    #     Database.__init__(self)
    def DanhSach(self):
        chuoiSQL="select ID, staff_id,staff_name,date_of_birth,address,phone_number,email from staffs"
        cursor = Database.getALL(self,chuoiSQL)
        if cursor != None:    
            lstNhom=[]
            for row in cursor:
                TT = {'ID':row[0], 'staff_id': row[1], 'staff_name':row[2], 'date_of_birth':row[3],'address': row[4],'phone_number': row[5],'email': row[6]}
                lstNhom.append(TT)
        return lstNhom
    def Insert(self, Ma,Ten,date_of_birth,address,phone_number,email ):
        chuoiSQL="insert into staffs (staff_id,staff_name,date_of_birth,address,phone_number,email) values(?,?,?,?,?,?)"
        kq = Database.execute(self,chuoiSQL,(Ma,Ten,date_of_birth,address, phone_number,email))
        return kq
    def Update(self,Id, Ma,Ten,date_of_birth,address,phone_number,email ):
        chuoiSQL="update staffs set staff_id=?, staff_name=?,date_of_birth=?,address=?,phone_number=?,email=? where ID=?"
        kq = Database.execute(self,chuoiSQL,(Ma,Ten,date_of_birth,address,phone_number,email,Id))
        return kq
    def Delete(self,Id):
        chuoiSQL="delete from staffs where ID= ? " 
        kq = Database.execute(self,chuoiSQL,(Id,))
        return kq
