import wx

class SizerFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,-1,title='사이저 만들기',size=(300,250))

        leftPnl = wx.Panel(self,-1)
        rightPnl = wx.Panel(self,-1)

        leftPnl.SetBackgroundColour('RED')
        rightPnl.SetBackgroundColour('BLUE')
        boxSizer = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer.Add(leftPnl,2,wx.EXPAND)
        boxSizer.Add(rightPnl,1,wx.EXPAND)

        self.SetSizer(boxSizer)

        self.Center()
        self.Show()

class App(wx.App):
    def __init__(self):
        super().__init__()
        self.frame = SizerFrame()

if __name__ == '__main__':
    app = wx.App()
    frame = SizerFrame()
    app.MainLoop()
