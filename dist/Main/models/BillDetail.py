from models.database import *

class BillModelct(Database):

    def DanhSach(self):
        chuoiSQL = "select ID, product_id,unit_id,product_nameHOA,unit_code,amount,unit_price,sub_total,tax,tax_amount,note,bill_id from bill_detail"
        cursor = Database.getALL(self,chuoiSQL)
        if cursor != None:    
            recordList = []
            for row in cursor:
                TT = {'ID':row[0], 'product_id':row[1],'unit_id':row[2],'product_nameHOA':row[3],'unit_code':row[4],'amount':row[5],'unit_price':row[6],'sub_total':row[7],'tax':row[8],'tax_amount':row[9],'note':row[10],',bill_id':row[11]}
                recordList.append(TT)
        return recordList


    def GetDetailPX(self, ID_PX):
        chuoiSQL = "select ID, product_id,unit_id,product_nameHOA,unit_code,amount,unit_price,sub_total,tax,tax_amount,note,bill_id from bill_detail where bill_id = "+ID_PX+""
        cursor = Database.getALL(self,chuoiSQL)
        if cursor != None:    
            recordList = []
            for row in cursor:
                TT = {'ID':row[0], 'product_id':row[1],'unit_id':row[2],'product_nameHOA':row[3],'unit_code':row[4],'amount':row[5],'unit_price':row[6],'sub_total':row[7],'tax':row[8],'tax_amount':row[9],'note':row[10],',bill_id':row[11]}
                recordList.append(TT)
        return recordList


    def Insert(self,product_id,unit_id,product_nameHOA,unit_code,amount,unit_price,sub_total,tax,tax_amount,note,bill_id):
        chuoiSQL = "insert into bill_detail (product_id,unit_id,product_nameHOA,unit_code,amount,unit_price,sub_total,tax,tax_amount,note,bill_id) values(?,?,?,?,?,?,?,?,?,?,?)"
        kq = Database.execute(self,chuoiSQL,(product_id,unit_id,product_nameHOA,unit_code,amount,unit_price,sub_total,tax,tax_amount,note,bill_id))
        return kq

    def Update(self,Id, product_id,unit_id,product_nameHOA,unit_code,amount,unit_price,sub_total,tax,tax_amount,note,bill_id):
        chuoiSQL = "update bill_detail set product_id,unit_id,product_nameHOA,unit_code,amount,unit_price,sub_total,tax,tax_amount,note,bill_id where ID = ?"
        kq = Database.execute(self,chuoiSQL,(product_id,unit_id,product_nameHOA,unit_code,amount,unit_price,sub_total,tax,tax_amount,note,bill_id,Id))
        return kq

    def Delete(self,Id):
        chuoiSQL = "delete from bill_detail where ID =  ? " 
        kq = Database.execute(self,chuoiSQL,(Id,))
        return kq
