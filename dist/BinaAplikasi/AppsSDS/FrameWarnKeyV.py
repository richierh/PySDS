# usr/bin/python
import wx

class FrameKeyVerification(wx.Frame):
    __classname__ = "Frame_Key_Verfication"

    def __init__(self,*args,**kwds):
        super(FrameKeyVerification,self).__init__(*args,**kwds)
        self.__properties()
        self.__shape()

    def __properties(self):
        self.SetTitle("Binakarir Authentication")
        self.SetSize(500,300)
        self.Centre()

    def __shape(self):
            sizer1 = wx.BoxSizer(wx.VERTICAL)

            self.panel1 = wx.Panel(self,id=wx.ID_ANY,pos=wx.DefaultPosition,size=wx.DefaultSize)
            sizer1.Add(self.panel1,1,flag = wx.ALL|wx.EXPAND,border =10)

            sizer2 = wx.BoxSizer(orient=wx.VERTICAL)
            self.StaticText1 = wx.StaticText(self.panel1,id=wx.ID_ANY,\

            label = "SILAHKAN MASUKAN LISENSI AUTHENTIKASI" ,pos = wx.DefaultPosition,\
            size=wx.DefaultSize,style=0)
            sizer2.Add(self.StaticText1,0,wx.ALL|wx.ALIGN_CENTER_HORIZONTAL,5)
            
            sizer3 = wx.BoxSizer(orient=wx.HORIZONTAL)
            sizer2.Add(sizer3,0,wx.ALL|wx.ALIGN_LEFT,10)

            self.StaticText1 = wx.StaticText(self.panel1,id=wx.ID_ANY,\
            label = "SILAHKAN MASUKAN LISENSI AUTHENTIKASI" ,pos = wx.DefaultPosition,\
            size=wx.DefaultSize,style=0)
            sizer3.Add(self.StaticText1,0,flag = wx.ALL,border=10)


            self.StaticText1 = wx.StaticText(self.panel1,id=wx.ID_ANY,\
            label = "SILAHKAN MASUKAN LISENSI AUTHENTIKASI" ,pos = wx.DefaultPosition,\
            size=wx.DefaultSize,style=0)
            sizer3.Add(self.StaticText1,0,flag = wx.ALL,border=10)

            
            self.panel1.SetSizer(sizer2)
            self.SetSizer(sizer1)

if __name__ == "__main__":
    root = wx.App()
    RunApp = FrameKeyVerification(None)
    RunApp.Show()
    root.MainLoop()
    
    pass