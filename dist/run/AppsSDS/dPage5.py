"""Subclass of Page5, which is generated by wxFormBuilder."""
import wx
import AppsSDS.sds as sds
import AppsSDS
# Implementing Page5
class dPage5( sds.Page5 ):
	def __init__( self, parent ):
		sds.Page5.__init__( self, parent )
# 		self.m_plota.Hide()

	# Handlers for Page5 events.
	def m_HitungSummaryCode( self, event ):
	
		
# 		print (tes.m_RealisticAOnText())
		
		# TODO: Implement m_HitungSummaryCode
		pass
	
	
	def m_tampilgrafikOnButtonClick(self,event):
		print("working")
# 		print (self.m_plota.Show())
# 		print (self.m_plotb.Show())
		
		if self.m_plota.IsShown()==True:
			self.m_plotb.Show()
			self.m_plota.Hide()
			print ("plotb tersembunyi")
		
		elif self.m_plotb.IsShown()==True:
			print ("plota tersembunyi")
			self.m_plota.Show()
			self.m_plotb.Hide()
		else :
			print ("error")
		
		self.Refresh()
		self.Layout()
		
		pass
	
	def onMotion(self, event):
# 		if event.inaxes:
# 			xpos = event.xdata
# 			print(' %0.1f' % (xpos))
		pass


