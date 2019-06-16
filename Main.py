# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import re
import wx
import wx.xrc
from templates.Unit import *
from templates.ProductType import *
from templates.Product import *
from templates.Customer import *
from templates.Staff import *
from templates.SaleOrder import *
###########################################################################
## Class MAIN
###########################################################################

class Frame ( wx.MDIParentFrame ):
	

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 646,371 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_categories = wx.Menu()
        self.m_menu_unit = wx.MenuItem( self.m_categories, wx.ID_ANY, u"Unit", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_categories.AppendItem( self.m_menu_unit )

        self.m_menuLHH = wx.MenuItem( self.m_categories, wx.ID_ANY, u"Product type", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_categories.AppendItem( self.m_menuLHH )

        self.m_menuHH = wx.MenuItem( self.m_categories, wx.ID_ANY, u"Product", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_categories.AppendItem( self.m_menuHH )

        self.m_menuKH = wx.MenuItem( self.m_categories, wx.ID_ANY, u"Customer", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_categories.AppendItem( self.m_menuKH )

        self.m_menuNV = wx.MenuItem( self.m_categories, wx.ID_ANY, u"Staff", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_categories.AppendItem( self.m_menuNV )

        self.m_categories.AppendSeparator()

        self.m_menuThoat = wx.MenuItem( self.m_categories, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_categories.AppendItem( self.m_menuThoat )

        self.m_menubar1.Append( self.m_categories, u"Categories" ) 

        self.m_menu2 = wx.Menu()
        self.m_menuBH_DHB = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Sale Order", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.AppendItem( self.m_menuBH_DHB )

        self.m_menuBH_DSBH = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Filter sale order", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.AppendItem( self.m_menuBH_DSBH )

        self.m_menu2.AppendSeparator()

        self.m_menubar1.Append( self.m_menu2, u"Sell" ) 

        self.m_menu3 = wx.Menu()
        self.m_menuBC_DoanhSo = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Sales", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.AppendItem( self.m_menuBC_DoanhSo )

        self.m_menubar1.Append( self.m_menu3, u"Report" ) 

        self.SetMenuBar( self.m_menubar1 )

        # self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.m_menuDM_OnMenuSelection, id = self.m_menu_unit.GetId() )
        self.Bind( wx.EVT_MENU, self.m_menuLHHOnMenuSelection, id = self.m_menuLHH.GetId() )
        self.Bind( wx.EVT_MENU, self.m_menuHHOnMenuSelection, id = self.m_menuHH.GetId() )
        self.Bind( wx.EVT_MENU, self.m_menuKHOnMenuSelection, id = self.m_menuKH.GetId() )
        self.Bind( wx.EVT_MENU, self.m_menuNVOnMenuSelection, id = self.m_menuNV.GetId() )
        self.Bind( wx.EVT_MENU, self.m_menuThoatOnMenuSelection, id = self.m_menuThoat.GetId() )
        self.Bind( wx.EVT_MENU, self.m_menuBH_DHBOnMenuSelection, id = self.m_menuBH_DHB.GetId() )
        self.Bind( wx.EVT_MENU, self.m_menuBH_DSBHOnMenuSelection, id = self.m_menuBH_DSBH.GetId() )
        self.Bind( wx.EVT_MENU, self.m_menuBC_DoanhSoOnMenuSelection, id = self.m_menuBC_DoanhSo.GetId() )
	

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class

    def callActiveFrame(self, strTitle):
        frameChilds = self.GetChildren()
        bActive = False
        for item in frameChilds:
            if item.GetTitle()==strTitle:
                item.Activate()
                bActive = True
                break
        return bActive
    

    def m_menuDM_OnMenuSelection( self, event ):
        if self.callActiveFrame(u'Categories Unit')==False:
            frame = wx.MDIChildFrame(self,id = wx.ID_ANY, title = u'Categories Unit',size = (550,400))
            _p =  UnitPanel(frame)
            _p.InitData()
            frame.CenterOnParent(wx.BOTH)
            frame.Show(True)


    def m_menuLHHOnMenuSelection( self, event ):
        if self.callActiveFrame(u'Categories Product type')==False:
            frame = wx.MDIChildFrame(self,id = wx.ID_ANY, title = u'Categories Product type',size = (550,400))
            _p =  ProductTypePanel(frame)
            _p.InitData()
            frame.CenterOnParent(wx.BOTH)
            frame.Show(True)



    def m_menuHHOnMenuSelection( self, event ):
        if self.callActiveFrame(u'Categories Product')==False:
            frame = wx.MDIChildFrame(self,id = wx.ID_ANY, title = u'Categories Product',size = (838,418 ))
            _p =  ProductPanel(frame)
            _p.InitData()
            frame.CenterOnParent(wx.BOTH)
            frame.Show(True)


    def m_menuKHOnMenuSelection( self, event ):
        if self.callActiveFrame(u'Categories Customer')==False:
            frame = wx.MDIChildFrame(self,id = wx.ID_ANY, title = u'Categories Customer',size = (838,418))
            _p =  CustomerPanel(frame)
            _p.InitData()
            frame.CenterOnParent(wx.BOTH)
            frame.Show(True)


    def m_menuNVOnMenuSelection( self, event ):
        if self.callActiveFrame(u'Categories Staff')==False:
            frame = wx.MDIChildFrame(self,id = wx.ID_ANY, title = u'Categories Staff',size = (838,418))
            _p =  StaffPanel(frame)
            _p.InitData()
            frame.CenterOnParent(wx.BOTH)
            frame.Show(True)


    def m_menuThoatOnMenuSelection( self, event ):
        self.Close()


    def m_menuBH_DHBOnMenuSelection( self, event ):
        if self.callActiveFrame(u'Sale Order')==False:
            frame = wx.MDIChildFrame(self,id = wx.ID_ANY, title = u'Sale Order',size = (940,600))
            _p =  SaleOrderPanel(frame)
            _p.InitData()
            frame.CenterOnParent(wx.BOTH)
            frame.Show(True)


    def m_menuBH_DSBHOnMenuSelection( self, event ):
        event.Skip()


    def m_menuBC_DoanhSoOnMenuSelection( self, event ):
        event.Skip()

if __name__ == "__main__":
    app = wx.App()
    frame = Frame(None)
    frame.Maximize(True)
    frame.m_menuBH_DHBOnMenuSelection(event = None)
    frame.Show(True)
    app.MainLoop()