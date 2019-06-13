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
## Class Panel1
###########################################################################

class Panel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 400,500 ), style = wx.TAB_TRAVERSAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"assets/images/bg.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_bitmap1, 0, wx.ALL, 5 )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_input_name = wx.TextCtrl( self, wx.ID_ANY, u"Nguyen Hoang Nguyen", wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer1.Add( self.m_input_name, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Code", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_input_code = wx.TextCtrl( self, wx.ID_ANY, u"C102", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_input_code, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Phone Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_input_phone = wx.TextCtrl( self, wx.ID_ANY, u"0832101231", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_input_phone, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_labelAddress = wx.StaticText( self, wx.ID_ANY, u"Address", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_labelAddress.Wrap( -1 )
		fgSizer1.Add( self.m_labelAddress, 0, wx.ALL, 5 )
		
		self.m_input_address = wx.TextCtrl( self, wx.ID_ANY, u"210/108A", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_input_address, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_input_email = wx.TextCtrl( self, wx.ID_ANY, u"nguyen.nh@ts24corp.com", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_input_email, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_input_hidden = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_input_hidden.Wrap( -1 )
		fgSizer1.Add( self.m_input_hidden, 0, wx.ALL, 5 )
		
		self.m_btn_update = wx.Button( self, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_btn_update, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		# self.m_btn_update.Bind( wx.EVT_BUTTON, self.changeText )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	

