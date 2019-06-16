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
from models.Product import *
from models.Unit import *
from models.ProductType import *
###########################################################################
## Class MyPanel4
###########################################################################

class ProductPanel ( wx.Panel ):
	


    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 992,462 ), style = wx.TAB_TRAVERSAL )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        gbSizer5 = wx.GridBagSizer( 0, 0 )
        gbSizer5.SetFlexibleDirection( wx.BOTH )
        gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Product type:*", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        gbSizer5.Add( self.m_staticText12, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        m_choiceproduct_type_idChoices = self.GetData(2)
        self.m_choiceproduct_type_id = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceproduct_type_idChoices, 0 )
        self.m_choiceproduct_type_id.SetSelection( 0 )
        gbSizer5.Add( self.m_choiceproduct_type_id, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Unit:*", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        gbSizer5.Add( self.m_staticText10, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        m_choiceunit_idChoices = self.GetData(1)
        self.m_choiceunit_id = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceunit_idChoices, 0, )
        self.m_choiceunit_id.SetSelection( 0 )
        gbSizer5.Add( self.m_choiceunit_id, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Product code:*", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )
        gbSizer5.Add( self.m_staticText13, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textMA = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
        gbSizer5.Add( self.m_textMA, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Product name:*", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        gbSizer5.Add( self.m_staticText11, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textTEN = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.m_textTEN, wx.GBPosition( 1, 5 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText111 = wx.StaticText( self, wx.ID_ANY, u"Tax:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText111.Wrap( -1 )
        gbSizer5.Add( self.m_staticText111, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_texttax = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.m_texttax, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Amount: ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )
        gbSizer5.Add( self.m_staticText20, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
        self.m_textamount = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.m_textamount, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText122 = wx.StaticText( self, wx.ID_ANY, u"Cost: ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText122.Wrap( -1 )
        gbSizer5.Add( self.m_staticText122, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textcost = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.m_textcost, wx.GBPosition( 2, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText131 = wx.StaticText( self, wx.ID_ANY, u"Price: ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText131.Wrap( -1 )
        gbSizer5.Add( self.m_staticText131, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textprice = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.m_textprice, wx.GBPosition( 2, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Made by: ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )
        gbSizer5.Add( self.m_staticText14, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textmade_in = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.m_textmade_in, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 7 ), wx.ALL|wx.EXPAND, 5 )

        self.m_staticText121 = wx.StaticText( self, wx.ID_ANY, u"Description:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText121.Wrap( -1 )
        gbSizer5.Add( self.m_staticText121, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textdescription = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 450,-1 ), 0 )
        gbSizer5.Add( self.m_textdescription, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 7 ), wx.ALL|wx.EXPAND, 5 )


        bSizer6.Add( gbSizer5, 1, wx.EXPAND, 5 )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticTRONG = wx.StaticText( self, wx.ID_ANY, u"                                                          ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTRONG.Wrap( -1 )
        bSizer9.Add( self.m_staticTRONG, 0, wx.ALL, 5 )

        self.m_btnThem = wx.Button( self, wx.ID_ANY, u"Add record", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_btnThem, 0, wx.ALL, 5 )

        self.m_btnXoa = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_btnXoa, 0, wx.ALL, 5 )

        self.m_btnSua = wx.Button( self, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_btnSua, 0, wx.ALL, 5 )

        self.m_btnDong = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_btnDong, 0, wx.ALL, 5 )


        bSizer6.Add( bSizer9, 1, wx.EXPAND, 5 )

        bSizer10 = wx.BoxSizer( wx.VERTICAL )

        self.m_gridSource = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,250 ), 0 )

        # Grid
        self.m_gridSource.CreateGrid(0, 11 )
        self.m_gridSource.EnableEditing( True )
        self.m_gridSource.EnableGridLines( True )
        self.m_gridSource.EnableDragGridSize( False )
        self.m_gridSource.SetMargins( 0, 0 )

        # Columns
        self.m_gridSource.SetColSize( 0, 67 )
        self.m_gridSource.SetColSize( 1, 155 )
        self.m_gridSource.SetColSize( 2, 80 )
        self.m_gridSource.SetColSize( 3, 69 )
        self.m_gridSource.SetColSize( 4, 82 )
        self.m_gridSource.SetColSize( 5, 80 )
        self.m_gridSource.SetColSize( 6, 80 )
        self.m_gridSource.SetColSize( 7, 80 )
        self.m_gridSource.SetColSize( 8, 80 )
        self.m_gridSource.SetColSize( 9, 150 )
        self.m_gridSource.SetColSize( 10, 150 )
        self.m_gridSource.EnableDragColMove( False )
        self.m_gridSource.EnableDragColSize( True )
        self.m_gridSource.SetColLabelSize( 35 )
        self.m_gridSource.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

        # Rows
        self.m_gridSource.EnableDragRowSize( True )
        self.m_gridSource.SetRowLabelSize( 40 )
        self.m_gridSource.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

        # Label Appearance

        # Cell Defaults
        self.m_gridSource.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer10.Add( self.m_gridSource, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer6.Add( bSizer10, 1, wx.EXPAND, 5 )


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
            if(kq == 0):
                wx.MessageBox("Please fill all required fields","Messages",wx.OK|wx.ICON_WARNING)
                self.m_textMA.SetFocus()
                return
        else :
         
            Ma = self.m_textMA.GetValue()
            Ten = self.m_textTEN.GetValue()
            idDVT = self.m_choiceunit_id.GetString(self.m_choiceunit_id.GetSelection())
            idloaihh = self.m_choiceproduct_type_id.GetString(self.m_choiceproduct_type_id.GetSelection())
            amount = self.m_textamount.GetValue()
            unit_pricevon = self.m_textcost.GetValue()
            unit_priceban = self.m_textprice.GetValue()
            tax = self.m_texttax.GetValue()
            made_in = self.m_textmade_in.GetValue()
            description = self.m_textdescription.GetValue()

            self.m_gridSource.AppendRows(1)
            xldb =  ProductModel()
            kq = xldb.Insert(Ma,Ten, idDVT,idloaihh,amount,unit_pricevon,unit_priceban,tax,made_in, description)
        if kq>0:
            self.OnLoadData()
            wx.MessageBox("Record added successfully","Messages",wx.OK|wx.ICON_INFORMATION)
            self.m_textMA.SetValue("")
            self.m_textTEN.SetValue("")
            self.m_texttax.SetValue("")
            self.m_textdescription.SetValue("")
            self.m_textcost.SetValue("")
            self.m_textamount.SetValue("")
            self.m_textprice.SetValue("")
            self.m_textmade_in.SetValue("")
            self.m_choiceunit_id.SetLabelText("")
            self.m_choiceproduct_type_id.SetLabelText("")
        else: 
            wx.MessageBox("Error when trying add record","Messages",wx.OK|wx.ICON_WARNING)


    def m_btnXoaOnButtonClick( self, event ):
        try:
            cell_value = []
            row_index = self.m_gridSource.GetSelectedRows()[0]
            for i in range(0,3):
                cell_value.append(self.m_gridSource.GetCellValue(row_index,i))
            
            xldb =  ProductModel()
            Id =  str(cell_value[0])
            kq = xldb.Delete(Id)
            if kq>0:
                self.OnLoadData()
            else: 
                wx.MessageBox("Error when trying delete this record","Messages",wx.OK|wx.ICON_WARNING)
        except :
            wx.MessageBox("Please select record to delete")

    def m_btnSuaOnButtonClick( self, event ):
        try:
            cell_value = []
            row_index = self.m_gridSource.GetSelectedRows()[0]
            for i in range(0,11):
                cell_value.append(self.m_gridSource.GetCellValue(row_index,i))
            Id =  str(cell_value[0])
            Ma =  str(cell_value[1])
            Ten =  str(cell_value[2])
            idDVT = str(cell_value[3])
            idloaihh = str(cell_value[4])
            amount = str(cell_value[5])
            unit_pricevon = str(cell_value[6])
            unit_priceban = str(cell_value[7])
            tax = str(cell_value[8])
            made_in = str(cell_value[9])
            description = str(cell_value[10])
            xldb =  ProductModel()

            kq = xldb.Update(Id,Ma,Ten,idDVT,idloaihh,amount,unit_pricevon,unit_priceban,tax,made_in,description)
            if kq>0:
                self.OnLoadData()
                wx.MessageBox("Record added successfully","Messages",wx.OK|wx.ICON_INFORMATION)
            else: 
                wx.MessageBox("Error when trying add record","Messages",wx.OK|wx.ICON_WARNING)
        except :
            wx.MessageBox("Please select your record to update")
        


    def m_btnDongOnButtonClick( self, event ):
        frame = self.GetParent()
        frame.Close()
  

    def InsertFromGrid(self):
        try:
            cell_value = []
            row_index = self.m_gridSource.GetSelectedRows()[0]
            for i in range(0,11):
                cell_value.append(self.m_gridSource.GetCellValue(row_index,i))
            
            xldb =  ProductModel()
            Id =  str(cell_value[0])
            Ma =  str(cell_value[1])
            Ten =  str(cell_value[2])
            idDVT = str(cell_value[3])
            idloaihh = str(cell_value[4])
            amount = str(cell_value[5])
            unit_pricevon = str(cell_value[6])
            unit_priceban = str(cell_value[7])
            tax = str(cell_value[8])
            made_in = str(cell_value[9])
            description = str(cell_value[10])
            if Ma == "":
                return 0
            self.m_gridSource.AppendRows(1)
            kq = xldb.Insert(Ma,Ten,idDVT,idloaihh,amount,unit_pricevon,unit_priceban,tax,made_in,description)
            if kq>0:
                return 1
            else: 
                return 0
        except :
            return 0


    def GetCountRow(self):
        count = 1
        xldb =  ProductModel()
        kq = xldb.DanhSach()
        if kq!=None:
            count = len(kq)
        return count

    def CheckValid(self):
        Ma = self.m_textMA.GetValue().strip() 
        Ten = self.m_textTEN.GetValue().strip()
        valid = True
        if len(Ma)==0: 
            valid = False
        return valid

    def GetData(self,loai):
        if loai == 1:
            xldb =  Unit()
            dsAll =  xldb.DanhSach()
        else:
            xldb =  ProductTypeModel()
            dsAll =  xldb.DanhSach()
        celldata = []
        if dsAll!=None:
            for i in range (0,len(dsAll)):
                cell = dsAll[i]
                if loai == 1 and str(cell['unit_name'])!="":
                    celldata.append(str(cell['unit_name']))
                elif loai == 2 and str(cell['product_type_name'])!="":
                    celldata.append(str(cell['product_type_name']))
        return celldata


    def InitData(self):
        self.m_gridSource.SetColLabelValue(0, "Id")
        self.m_gridSource.SetColLabelValue(1, "Product code")
        self.m_gridSource.SetColLabelValue(2, "Product name")
        self.m_gridSource.SetColLabelValue(3, "Unit")
        self.m_gridSource.SetColLabelValue(4, "Product type")
        self.m_gridSource.SetColLabelValue(5, "Amount")
        self.m_gridSource.SetColLabelValue(6, "Cost")
        self.m_gridSource.SetColLabelValue(7, "Price")
        self.m_gridSource.SetColLabelValue(8, "Tax")
        self.m_gridSource.SetColLabelValue(9, "Made by")
        self.m_gridSource.SetColLabelValue(10, "Description")
        row = self.GetCountRow()+1
        self.m_gridSource.AppendRows(row)
        self.OnLoadData()


    def OnLoadData(self):
        xldb =  ProductModel()
        dsAll =  xldb.DanhSach()
        if dsAll!=None:
            self.m_gridSource.ClearGrid()
            for i in range (0,len(dsAll)):
                cell = dsAll[i]
                self.m_gridSource.SetCellValue(i,0,str(cell['ID']))
                self.m_gridSource.SetCellValue(i,1,str(cell['product_code']))
                self.m_gridSource.SetCellValue(i,2,str(cell['product_name']))
                self.m_gridSource.SetCellValue(i,3,str(cell['unit_id']))
                self.m_gridSource.SetCellValue(i,4,str(cell['product_type_id']))
                self.m_gridSource.SetCellValue(i,5,str(cell['amount']))
                self.m_gridSource.SetCellValue(i,6,str(cell['cost']))
                self.m_gridSource.SetCellValue(i,7,str(cell['price']))
                self.m_gridSource.SetCellValue(i,8,str(cell['tax']))
                self.m_gridSource.SetCellValue(i,9,str(cell['made_in']))
                self.m_gridSource.SetCellValue(i,10,str(cell['description']))

        return
