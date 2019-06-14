from models.database import *

class ProductTypeModel(Database):
    # def __init__(self):
    #     Database.__init__(self)
    def DanhSach(self):
        chuoiSQL="select ID, product_type_code,product_type_name from product_types"
        cursor = Database.getALL(self,chuoiSQL)
        if cursor != None:    
            lstNhom=[]
            for row in cursor:
                TT = {'ID':row[0], 'product_type_code': row[1], 'product_type_name':row[2]}
                lstNhom.append(TT)
        return lstNhom
    def Insert(self, Ma,Ten):
        chuoiSQL="insert into product_types (product_type_code,product_type_name) values(?,?)"
        kq = Database.execute(self,chuoiSQL,(Ma,Ten))
        return kq
    def Update(self,Id, Ma,Ten):
        chuoiSQL="update product_types set product_type_code=?, product_type_name=? where ID=?"
        kq = Database.execute(self,chuoiSQL,(Ma,Ten,Id))
        return kq
    def Delete(self,Id):
        chuoiSQL="delete from product_types where ID= ? " 
        kq = Database.execute(self,chuoiSQL,(Id,))
        return kq
