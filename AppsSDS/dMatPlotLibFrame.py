"""Subclass of MatPlotLibFrame, which is generated by wxFormBuilder."""

import wx
import AppsSDS.sds as sds


# Implementing MatPlotLibFrame
class dMatPlotLibFrame( sds.MatPlotLibFrame ):
	def __init__( self, parent ):
		sds.MatPlotLibFrame.__init__( self, parent )
		self.Layout()
		self.Refresh()
		


if __name__ == '__main__':
	root = wx.App()
	bukajendela=dMatPlotLibFrame(None)
	bukajendela.Show()
	root.MainLoop()
	pass
