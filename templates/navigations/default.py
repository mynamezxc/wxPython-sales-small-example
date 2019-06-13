# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class OrderNavigation
###########################################################################

class Navigation ( wx.Frame ):
	
	def __init__( self, parent, width, height ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sale orders", pos = wx.DefaultPosition, size = wx.Size( width,height ), style = wx.DEFAULT_FRAME_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menubar1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		self.m_orders = wx.Menu()
		self.m_view_order_list = wx.MenuItem( self.m_orders, wx.ID_ANY, u"Order List", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_orders.AppendItem( self.m_view_order_list )
		
		self.m_menubar1.Append( self.m_orders, u"Orders" ) 
		
		self.m_customers = wx.Menu()
		self.m_view_customer_list = wx.MenuItem( self.m_customers, wx.ID_ANY, u"Customer list", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_customers.AppendItem( self.m_view_customer_list )
		
		self.m_create_customer = wx.MenuItem( self.m_customers, wx.ID_ANY, u"Create new customer", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_customers.AppendItem( self.m_create_customer )
		
		self.m_menubar1.Append( self.m_customers, u"Customers" ) 
		
		self.m_products = wx.Menu()
		self.m_view_product_list = wx.MenuItem( self.m_products, wx.ID_ANY, u"Product list", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_products.AppendItem( self.m_view_product_list )
		
		self.m_create_product = wx.MenuItem( self.m_products, wx.ID_ANY, u"Create new product", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_products.AppendItem( self.m_create_product )
		
		self.m_menubar1.Append( self.m_products, u"Products" ) 
		
		self.m_salers = wx.Menu()
		self.m_view_all_saler = wx.MenuItem( self.m_salers, wx.ID_ANY, u"Saler list", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_salers.AppendItem( self.m_view_all_saler )
		
		self.m_create_saler = wx.MenuItem( self.m_salers, wx.ID_ANY, u"Create new saler", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_salers.AppendItem( self.m_create_saler )
		
		self.m_menubar1.Append( self.m_salers, u"Salers" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

