# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
from models.Staff import *
###########################################################################
## Class MyPanel5
###########################################################################

class StaffPanel ( wx.Panel ):


    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 932,501 ), style = wx.TAB_TRAVERSAL )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        gbSizer4 = wx.GridBagSizer( 0, 0 )
        gbSizer4.SetFlexibleDirection( wx.BOTH )
        gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Mã NV:*", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )
        gbSizer4.Add( self.m_staticText15, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textMA = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer4.Add( self.m_textMA, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Tên NV:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )
        gbSizer4.Add( self.m_staticText16, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textTEN = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
        gbSizer4.Add( self.m_textTEN, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Ngày sinh:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )
        gbSizer4.Add( self.m_staticText17, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textdate_of_birth = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer4.Add( self.m_textdate_of_birth, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Số đt:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )
        gbSizer4.Add( self.m_staticText18, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textphone_number = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer4.Add( self.m_textphone_number, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"email:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )
        gbSizer4.Add( self.m_staticText20, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textemail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer4.Add( self.m_textemail, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 5 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Địa chỉ:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )
        gbSizer4.Add( self.m_staticText19, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textaddress = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer4.Add( self.m_textaddress, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 5 ), wx.ALL|wx.EXPAND, 5 )


        bSizer6.Add( gbSizer4, 1, wx.EXPAND, 5 )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_btnThem = wx.Button( self, wx.ID_ANY, u"Thêm", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_btnThem, 0, wx.ALL, 5 )

        self.m_btnXoa = wx.Button( self, wx.ID_ANY, u"Xóa", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_btnXoa, 0, wx.ALL, 5 )

        self.m_btnSua = wx.Button( self, wx.ID_ANY, u"Cập nhật", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_btnSua, 0, wx.ALL, 5 )

        self.m_btnDong = wx.Button( self, wx.ID_ANY, u"Đóng", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_btnDong, 0, wx.ALL, 5 )


        bSizer6.Add( bSizer9, 1, wx.EXPAND, 5 )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_gridSource = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,250 ), 0 )

        # Grid
        self.m_gridSource.CreateGrid( 0, 7 )
        self.m_gridSource.EnableEditing( True )
        self.m_gridSource.EnableGridLines( True )
        self.m_gridSource.EnableDragGridSize( False )
        self.m_gridSource.SetMargins( 0, 0 )

        # Columns
        self.m_gridSource.SetColSize( 0, 80 )
        self.m_gridSource.SetColSize( 1, 188 )
        self.m_gridSource.SetColSize( 2, 80 )
        self.m_gridSource.SetColSize( 3, 80 )
        self.m_gridSource.SetColSize( 4, 80 )
        self.m_gridSource.SetColSize( 5, 175 )
        self.m_gridSource.SetColSize( 6, 253 )
        self.m_gridSource.EnableDragColMove( False )
        self.m_gridSource.EnableDragColSize( True )
        self.m_gridSource.SetColLabelSize( 30 )
        self.m_gridSource.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

        # Rows
        self.m_gridSource.EnableDragRowSize( True )
        self.m_gridSource.SetRowLabelSize( 1 )
        self.m_gridSource.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

        # Label Appearance

        # Cell Defaults
        self.m_gridSource.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer11.Add( self.m_gridSource, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer6.Add( bSizer11, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer6 )
        self.Layout()

        # Connect Events
        self.m_btnThem.Bind( wx.EVT_BUTTON, self.m_btnThemOnButtonClick )
        self.m_btnXoa.Bind( wx.EVT_BUTTON, self.m_btnXoaOnButtonClick )
        self.m_btnSua.Bind( wx.EVT_BUTTON, self.m_btnSuaOnButtonClick )
        self.m_btnDong.Bind( wx.EVT_BUTTON, self.m_btnDongOnButtonClick )
	
    def __del__( self ):
        pass
	
	
	# Virtual event handlers, overide them in your derived class
    def m_btnThemOnButtonClick( self, event):
        kq = 0
        if self.CheckValid()==False:
            kq = self.InsertFromGrid()
            if(kq==0):
                wx.MessageBox("Vui lòng không để trống dữ liệu","Thông báo",wx.OK|wx.ICON_WARNING)
                self.m_textMA.SetFocus()
                return
        else :
            Ma = self.m_textMA.GetValue()
            Ten = self.m_textTEN.GetValue()
            date_of_birth= self.m_textdate_of_birth.GetValue()
            address = self.m_textaddress.GetValue()
            phone_number= self.m_textphone_number.GetValue()
            email= self.m_textemail.GetValue()

            # if(self.GetCountRow()>14):
            self.m_gridSource.AppendRows(1)
            xldb= StaffModel()
            kq = xldb.Insert(Ma,Ten,date_of_birth,address,phone_number,email)
        if kq>0:
            self.OnLoadData()
            wx.MessageBox("Thêm dữ liệu thành công","Thông báo",wx.OK|wx.ICON_INFORMATION)
            self.m_textMA.SetValue("")
            self.m_textTEN.SetValue("")
            self.m_textdate_of_birth.SetValue("")
            self.m_textaddress.SetValue("")
            self.m_textphone_number.SetValue("")
            self.m_textemail.SetValue("")
        else: 
            wx.MessageBox("Thêm dữ liệu không thành công","Thông báo",wx.OK|wx.ICON_WARNING)

    def m_btnXoaOnButtonClick( self, event ):
        try:
            cell_value=[]
            row_index = self.m_gridSource.GetSelectedRows()[0]
            for i in range(0,1):
                cell_value.append(self.m_gridSource.GetCellValue(row_index,i))
            
            xldb= StaffModel()
            Id= str(cell_value[0])
            kq = xldb.Delete(Id)
            if kq>0:
                self.OnLoadData()
            else: 
                wx.MessageBox("Xóa dữ liệu không thành công","Thông báo",wx.OK|wx.ICON_WARNING)
        except :
            wx.MessageBox("Vui lòng chọn dòng để xóa")
    def m_btnSuaOnButtonClick( self, event ):
        try:
            cell_value=[]
            row_index = self.m_gridSource.GetSelectedRows()[0]
            for i in range(0,7):
                cell_value.append(self.m_gridSource.GetCellValue(row_index,i))
            
            xldb= StaffModel()
            Id= str(cell_value[0])
            Ma= str(cell_value[1])
            Ten= str(cell_value[2])
            date_of_birth= str(cell_value[3])
            phone_number= str(cell_value[4])
            address= str(cell_value[5])
            email= str(cell_value[6])

            kq = xldb.Update(Id,Ma,Ten,date_of_birth,address,phone_number,email)
            if kq>0:
                self.OnLoadData()
                wx.MessageBox("Cập nhật dữ liệu thành công","Thông báo",wx.OK|wx.ICON_INFORMATION)
            else: 
                wx.MessageBox("Cập nhật dữ liệu không thành công","Thông báo",wx.OK|wx.ICON_WARNING)
        except :
            wx.MessageBox("Vui lòng chọn dòng để cập nhật")
        event.Skip()

    def m_btnDongOnButtonClick( self, event ):
        frame = self.GetParent()
        frame.Close()
        # event.Skip()
#https://tutorial101.blogspot.com/2016/05/wxpython-phone-book-using-data-grid.html
    def m_gridSourceOnGridSelectCell( self, event ):
        event.Skip()

    # def m_gridSourceOnGridLabelLeftDClick( self, event ):
    #     try:
    #         row_index = self.m_gridSource.GetSelectedRows()[0]
    #         # row_index = self.m_gridSource.GetSelectedCells()
    #         cell_value=[]
    #         for i in range(0,2):
    #             cell_value.append(self.m_gridSource.GetCellValue(row_index,i))
    #         self.m_textunit_code.Value= str(cell_value[0])
    #         self.m_textunit_name.Value= str(cell_value[1])
    #     except:
    #         wx.MessageBox("Error selected index")
    def InsertFromGrid(self):
        try:
            cell_value=[]
            row_index = self.m_gridSource.GetSelectedRows()[0]
            for i in range(0,7):
                cell_value.append(self.m_gridSource.GetCellValue(row_index,i))
            
            xldb= StaffModel()
            Id= str(cell_value[0])
            Ma= str(cell_value[1])
            Ten= str(cell_value[2])
            date_of_birth= str(cell_value[3])
            phone_number= str(cell_value[4])
            address= str(cell_value[5])
            email= str(cell_value[6])

            if Ma=="":
                return 0
            # if(self.GetCountRow()>14):
            self.m_gridSource.AppendRows(1)
            kq = xldb.Insert(Ma,Ten,date_of_birth,address,phone_number,email)
            if kq>0:
                return 1
            else: 
                return 0
        except :
            #wx.MessageBox("Vui lòng chọn dòng để cập nhật")
            return 0

    def GetCountRow(self):
        count = 1
        xldb= StaffModel()
        kq = xldb.DanhSach()
        if kq!=None:
            count = len(kq)

        return count
    def CheckValid(self):
        Ma = self.m_textMA.GetValue().strip() 
        valid = True
        if len(Ma)==0: 
            valid = False
            self.m_textMA.SetFocus() 
        # else: 
        #     self.m_ErrorMA.SetLabel("")
        return valid
    def InitData(self):
        self.m_gridSource.SetColLabelValue(0, "Id")
        self.m_gridSource.SetColLabelValue(1, "Mã NV")
        self.m_gridSource.SetColLabelValue(2, "Tên NV")
        self.m_gridSource.SetColLabelValue(3, "Ngày sinh")
        self.m_gridSource.SetColLabelValue(4, "Số điện thoại")
        self.m_gridSource.SetColLabelValue(5, "Địa chỉ")
        self.m_gridSource.SetColLabelValue(6, "email")
        row = self.GetCountRow()+1
        self.m_gridSource.AppendRows(row)
        self.OnLoadData()
    def OnLoadData(self):
        # path_DB= 'database\BanHang.db'
        xldb= StaffModel()
        dsAll= xldb.DanhSach()
        if dsAll!=None:
            self.m_gridSource.ClearGrid()
            for i in range (0,len(dsAll)):
                cell = dsAll[i]
                self.m_gridSource.SetCellValue(i,0,str(cell['ID']))
                self.m_gridSource.SetCellValue(i,1,str(cell['staff_id']))
                self.m_gridSource.SetCellValue(i,2,str(cell['staff_name']))
                self.m_gridSource.SetCellValue(i,3,str(cell['date_of_birth']))
                self.m_gridSource.SetCellValue(i,4,str(cell['phone_number']))
                self.m_gridSource.SetCellValue(i,5,str(cell['address']))
                self.m_gridSource.SetCellValue(i,6,str(cell['email']))
        return

	

