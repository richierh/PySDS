#!usr/bin/env python

import wx

from AppsSDS.SDSHollandWindowUtama import SDSHollandWindowUtama as I


class run(I):

	def __init__(self, *args, **kwrgs):
		super(run, self).__init__(*args, **kwrgs)

	pass


root = wx.App()

class VerifyKey():
	
	def __init__(self,parent):
		self.value = parent
		pass
	
	def Verify(self):
		
		return self.value

	def __repr__(self):
		return str(self.value)

def openWindows():
	start = run(None)
	start.Show()
	root.MainLoop()	
	print ("lewat sini")
	return None

def close():
	from AppsSDS.authenticationFrameWarningKey import authenticationFrameWarningKey
	start = authenticationFrameWarningKey(None)
	start.Show()
	root.MainLoop()
	print ("lewat close")
	return None


KeyVerification = VerifyKey("1")
print (KeyVerification.Verify())
print (type(KeyVerification))

# KeyVerification_dict = {
# 	"1" : openWindows() ,
# 	# "2" : close
# }
# KeyVerification_dict.get("1"
# ,close())

if KeyVerification.Verify() == "1":
	openWindows()

else :
	close()