"""Subclass of FrameWarningKey, which is generated by wxFormBuilder."""

import wx
import FrameKey
import random

# Implementing FrameWarningKey
class authenticationFrameWarningKey( FrameKey.FrameWarningKey ):
	def __init__( self, parent ):
		FrameKey.FrameWarningKey.__init__( self, parent )
		self.nilai = random.randint(1700,1900)
		print (self.nilai)
		self.lisennombor = self.nilai*4 + 223445435
		self.m_staticText144.SetLabel(str(self.lisennombor))


	# Handlers for FrameWarningKey events.
	def m_textCtrl49OnText( self, event ):
		# TODO: Implement m_textCtrl49OnText
		pass

	def m_button38OnButtonClick( self, event ):
		# TODO: Implement m_button38OnButtonClick
		print ("batal")
		self.Close()
		pass

	def m_button39OnButtonClick( self, event ):
		# TODO: Implement m_button39OnButtonClick
		global lisensi
		from AppsSDS.keygenapps.keygen import Key
		self.keynumber = self.m_textCtrl49.GetValue()
		print (self.keynumber)
		lisensi =  (self.lisennombor - 223445435)/4
		print (lisensi)
		self.gen = Key(self.keynumber)

		print (self.gen.verify(lisensi))

		self.verify = self.gen.verify(lisensi)
		
		print ("validasi")
		pass

if __name__ == "__main__":
    root = wx.App()
    RunApp = authenticationFrameWarningKey(None)
    RunApp.Show()
    root.MainLoop()
    
    pass