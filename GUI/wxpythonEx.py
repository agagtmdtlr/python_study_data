import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='')

        self.Bind(wx.EVT_LEFT_DOWN, self.LButton)
        self.Bind(wx.EVT_RIGHT_DOWN, self.RButton)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
    def LButton(self, event):
        self.SetSize(wx.Size(400, 200))

    def RButton(self, event):
        self.SetSize(wx.Size(200, 400))

    def OnClose(self, event):
        print('안녕히 계세요.')
        self.Destroy()
# end class MyFrame

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()