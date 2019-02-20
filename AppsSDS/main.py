#!usr/bin/env python

import wx

from AppsSDS.SDSHollandWindowUtama import SDSHollandWindowUtama as I


class run(I):

	def __init__(self, *args, **kwrgs):
		super(run, self).__init__(*args, **kwrgs)

	pass

root = wx.App()
start = run(None)
start.Show()
root.MainLoop()	
