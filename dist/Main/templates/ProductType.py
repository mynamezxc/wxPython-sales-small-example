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
from models.ProductType import *
###########################################################################
## Class MyPanel4
###########################################################################

class ProductTypePanel ( wx.Panel ):



    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 585,325 ), style = wx.TAB_TRAVERSAL )
        
        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        gbSizer5 = wx.GridBagSizer( 0, 0 )
        gbSizer5.SetFlexibleDirection( wx.BOTH )
        gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticTextMA = wx.StaticText( self, wx.ID_ANY, u"Code:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextMA.Wrap( -1 )
        gbSizer5.Add( self.m_staticTextMA, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textproduct_type_code = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.m_textproduct_type_code, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_ErrorMA = wx.StaticText( self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_ErrorMA.Wrap( -1 )
        gbSizer5.Add( self.m_ErrorMA, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticTextTEN = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextTEN.Wrap( -1 )
        gbSizer5.Add( self.m_staticTextTEN, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textproduct_type_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
        gbSizer5.Add( self.m_textproduct_type_name, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )

        self.m_ErrorTEN = wx.StaticText( self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_ErrorTEN.Wrap( -1 )
        gbSizer5.Add( self.m_ErrorTEN, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        bSizer6.Add( gbSizer5, 1, wx.EXPAND, 5 )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

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
        self.m_gridSource.CreateGrid( 0, 3 )
        self.m_gridSource.EnableEditing( True )
        self.m_gridSource.EnableGridLines( True )
        self.m_gridSource.EnableDragGridSize( False )
        self.m_gridSource.SetMargins( 0, 0 )

        # Columns
        self.m_gridSource.SetColSize( 0, 35 )
        self.m_gridSource.SetColSize( 1, 80 )
        self.m_gridSource.SetColSize( 2, 350 )
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
                self.m_textproduct_type_code.SetFocus()
                return
        else:
            Ma = self.m_textproduct_type_code.GetValue()
            Ten = self.m_textproduct_type_name.GetValue()
            self.m_gridSource.AppendRows(1)
            xldb =  ProductTypeModel()
            kq = xldb.Insert(Ma,Ten)
        if kq>0:
            self.OnLoadData()
            wx.MessageBox("Record added successfully","Messages",wx.OK|wx.ICON_INFORMATION)
            self.m_textproduct_type_code.SetValue("")
            self.m_textproduct_type_name.SetValue("")
        else: 
            wx.MessageBox("Error when trying add record","Messages",wx.OK|wx.ICON_WARNING)


    def m_btnXoaOnButtonClick( self, event ):
        try:
            cell_value = []
            row_index = self.m_gridSource.GetSelectedRows()[0]
            for i in range(0,3):
                cell_value.append(self.m_gridSource.GetCellValue(row_index,i))
            
            xldb =  ProductTypeModel()
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
            for i in range(0,3):
                cell_value.append(self.m_gridSource.GetCellValue(row_index,i))
            
            xldb =  ProductTypeModel()
            Id =  str(cell_value[0])
            Ma =  str(cell_value[1])
            Ten =  str(cell_value[2])
            kq = xldb.Update(Id,Ma,Ten)
            if kq>0:
                self.OnLoadData()
                wx.MessageBox("Record added successfully","Messages",wx.OK|wx.ICON_INFORMATION)
            else: 
                wx.MessageBox("Error when trying add record","Messages",wx.OK|wx.ICON_WARNING)
        except :
            wx.MessageBox("Please select your record to update")
        event.Skip()


    def m_btnDongOnButtonClick( self, event ):
        frame = self.GetParent()
        frame.Close()


    def m_gridSourceOnGridRangeSelect( self, event ):
        try:
            cell_value = []
            row_index = self.m_gridSource.GetSelectedRows()[0]
            for i in range(0,3):
                cell_value.append(self.m_gridSource.GetCellValue(row_index,i))
            if(len(cell_value) >0):
                self.m_btnSua.Enable =  True
                self.m_btnXoa.Enable =  True
            else:
                self.m_btnSua.Enable =  False
                self.m_btnXoa.Enable =  False
        except :
            self.m_btnSua.Enable =  False
            self.m_btnXoa.Enable =  False


    def InsertFromGrid(self):
        try:
            cell_value = []
            row_index = self.m_gridSource.GetSelectedRows()[0]
            for i in range(0,3):
                cell_value.append(self.m_gridSource.GetCellValue(row_index,i))
            
            xldb =  ProductTypeModel()
            Id =  str(cell_value[0])
            Ma =  str(cell_value[1])
            Ten =  str(cell_value[2])
            if Ma == "" or Ten == "":
                return 0
            self.m_gridSource.AppendRows(1)
            kq = xldb.Insert(Ma,Ten)
            if kq>0:
                return 1
            else: 
                return 0
        except :
            return 0


    def GetCountRow(self):
        count = 1
        xldb =  ProductTypeModel()
        kq = xldb.DanhSach()
        if kq!=None:
            count = len(kq)

        return count

    def CheckValid(self):
        Ma = self.m_textproduct_type_code.GetValue().strip() 
        Ten = self.m_textproduct_type_name.GetValue().strip()
        valid = True
        if len(Ma)==0: 
            valid = False
            self.m_ErrorMA.SetLabel("*") 
        else: 
            self.m_ErrorMA.SetLabel("")
        return valid

    def InitData(self):
        self.m_gridSource.SetColLabelValue(0, "Id")
        self.m_gridSource.SetColLabelValue(1, "Code")
        self.m_gridSource.SetColLabelValue(2, "Name")
        row = self.GetCountRow()+1
        self.m_gridSource.AppendRows(row)
        self.OnLoadData()


    def OnLoadData(self):
        xldb =  ProductTypeModel()
        dsAll =  xldb.DanhSach()
        if dsAll!=None:
            self.m_gridSource.ClearGrid()
            for i in range (0,len(dsAll)):
                row = dsAll[i]
                self.m_gridSource.SetCellValue(i,0,str(row['ID']))
                self.m_gridSource.SetCellValue(i,1,str(row['product_type_code']))
                self.m_gridSource.SetCellValue(i,2,str(row['product_type_name']))

        return
