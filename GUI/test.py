import wx
import wx.lib.buttons as buttons
import wx.lib.plot.plotcanvas as plotcanvas

class MyFrame(wx.Frame):
    def __init__(self, parent, title):

        wx.Frame.__init__(self, parent, wx.ID_ANY, title, size=(500 ,600))
        panel = wx.Panel(self)

        # Build a bitmap button and a normal one
        bmp = wx.ArtProvider.GetBitmap(wx.ART_INFORMATION, wx.ART_OTHER, (16, 16))
        btn1 = buttons.ThemedGenBitmapButton(panel, -1, bmp, pos=(50, 50))

        self.plot1 = plotcanvas.PlotCanvas(panel,wx.ID_ANY,wx.Point(0,0),wx.Size(300,300),0,'hello')
        self.cnt = wx.GraphicsRenderer.CreateContext(panel)

        btn1.Bind(wx.EVT_PAINT,self.OnPaint)

    def OnPaint(self, event):
        # Create paint DC
        dc = wx.PaintDC(self)

        # Create graphics context from it
        gc = wx.GraphicsContext.Create(dc)

        if gc:
            # make a path that contains a circle and some lines
            gc.SetPen(wx.RED_PEN)
            path = gc.CreatePath()
            path.AddCircle(50.0, 50.0, 50.0)
            path.MoveToPoint(0.0, 50.0)
            path.AddLineToPoint(100.0, 50.0)
            path.MoveToPoint(50.0, 0.0)
            path.AddLineToPoint(50.0, 100.0)
            path.CloseSubpath()
            path.AddRectangle(25.0, 25.0, 50.0, 50.0)

            gc.StrokePath(path)






app = wx.App()
frame = MyFrame(None, 'wx.lib.buttons Test')
frame.Show()
app.MainLoop()