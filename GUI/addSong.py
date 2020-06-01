import wx
import wx.xrc

class MyFrame3(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(800, 500), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        #첫번째 판넬
        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.lblSinger = wx.StaticText(self.m_panel1, wx.ID_ANY, u"가수이름", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblSinger.Wrap(-1)
        bSizer5.Add(self.lblSinger, 0, wx.ALL, 5)

        self.txtSinger = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.txtSinger, 0, wx.ALL, 5)

        self.lblSong = wx.StaticText(self.m_panel1, wx.ID_ANY, u"노래 제목", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblSong.Wrap(-1)
        bSizer5.Add(self.lblSong, 0, wx.ALL, 5)

        self.txtSong = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.txtSong, 0, wx.ALL, 5)

        self.btnInput = wx.Button(self.m_panel1, wx.ID_ANY, u"등록하기", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.btnInput, 0, wx.ALL, 5)

        self.m_panel1.SetSizer(bSizer5)
        self.m_panel1.Layout()
        bSizer5.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)
        # 첫번째 판넬

        # 두번째 판넬
        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.lstMusic = wx.ListCtrl(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.LC_REPORT)
        bSizer6.Add(self.lstMusic, 0, wx.ALL, 5)

        self.m_panel2.SetSizer(bSizer6)
        self.m_panel2.Layout()
        bSizer6.Fit(self.m_panel2)
        bSizer1.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)
        # 두번째 판넬

        # 세번째 판넬
        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.lblSongtotal = wx.StaticText(self.m_panel3, wx.ID_ANY, '노래 개수 : ' + str(self.lstMusic.GetItemCount())
                                          , wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblSongtotal.Wrap(-1)
        bSizer7.Add(self.lblSongtotal, 0, wx.ALL, 5)

        self.m_panel3.SetSizer(bSizer7)
        self.m_panel3.Layout()
        bSizer7.Fit(self.m_panel3)
        bSizer1.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # my event code Bind

        # 내가 추가한 코드
        self.lstMusic.InsertColumn(0,'가수 이름', width=200)
        self.lstMusic.InsertColumn(1,'노래 제목', width=200)
        #가수,노래 추가하기 버튼 클릭
        self.btnInput.Bind(wx.EVT_BUTTON,self.OnInsert)



    def OnInsert(self,event):
        singer = self.txtSinger.GetValue()
        song = self.txtSong.GetValue()

        i = self.lstMusic.InsertItem(1000,0)
        print(i)

        self.lstMusic.SetItem(i,0,singer)
        self.lstMusic.SetItem(i,1,song)

        self.txtSong.SetValue('')
        self.txtSinger.SetValue('')
        self.txtSinger.SetFocus()

        self.lblSongtotal.SetLabelText('노래 개수 : ' + str(self.lstMusic.GetItemCount()))
    def __del__(self):
        pass

if __name__ == '__main__':
    app = wx.App()
    MyFrame3(None).Show()
    app.MainLoop()