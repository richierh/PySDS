# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 29 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
# 
import wx
# import wx.xrc
# from work_excel import Work_excel

###########################################################################
## Class Listbox1
###########################################################################

class Listbox1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour(wx.Colour(4,109,64))
		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.AddGrowableCol( 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.AddGrowableRow( 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.cancel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.ok = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.ok, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( fgSizer1, 0, wx.EXPAND|wx.ALIGN_RIGHT, 5 )
		from AppsSDS.db import db
		self.listprofesiona = db.QueryList()
		self.listprofesiona.query()
		print (list(self.listprofesiona.query().keys()))
		m_listBox1Choices = list(self.listprofesiona.query().keys())
		print(type(m_listBox1Choices))
		self.m_listBox1 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, wx.LB_NEEDED_SB|wx.LB_SORT )
		bSizer1.Add( self.m_listBox1, 1, wx.ALL|wx.EXPAND, 5 )
		self.m_staticText205 = wx.StaticText( self, wx.ID_ANY, u"Tekan \"Ctrl+F\" untuk pencarian cepat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText205.Wrap( -1 )

		bSizer1.Add( self.m_staticText205, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.cancel.Bind( wx.EVT_BUTTON, self.m_tombolcancel_lb )
		self.ok.Bind( wx.EVT_BUTTON, self.tombolok_lb )
		self.m_listBox1.Bind( wx.EVT_LISTBOX_DCLICK, self.m_listboxselect )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_tombolcancel_lb( self, event ):
		event.Skip()

	def tombolok_lb( self, event ):
		event.Skip()

	def m_listboxselect( self, event ):
		event.Skip()

