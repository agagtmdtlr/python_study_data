import wx

class MusicFrame(wx.Frame):
    def __init__(self,parent):
        super().__init__(parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ),
                         style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        boxSizers = wx.BoxSizer(wx.HORIZONTAL)

        #첫번째 콤보박스
        self.pnlSinger = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        subbx1 = wx.BoxSizer()


        self.singerData = ['이선희','이문세','이승식']
        self.cmbSinger = wx.ComboBox(self.pnlSinger,choices=self.singerData)
        subbx1.Add(self.cmbSinger, 0, wx.ALL, 5 )

        self.pnlSinger.SetSizer(subbx1)
        self.pnlSinger.Layout()
        subbx1.Fit(self.pnlSinger)
        boxSizers.Add(self.pnlSinger, 1, wx.EXPAND |wx.ALL, 5 )

        #2번째 리스트 박스
        self.pnlSong = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        subbx2 = wx.BoxSizer(wx.VERTICAL)

        self.songData = {'이선희':['사과','배'],'이문세':['오렌지','귤'],'이승식':['포도','프로틴']}

        self.lcmSong = wx.ListBox(self.pnlSong)
        subbx2.Add(self.lcmSong, 0, wx.ALL, 5 )

        self.pnlSong.SetSizer(subbx2)
        self.pnlSong.Layout()
        subbx2.Fit(self.pnlSong)
        boxSizers.Add(self.pnlSong, 1, wx.EXPAND |wx.ALL, 5 )

        #3번째 라벨 멀티라인
        self.pnlSubtitle = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        subbx3 = wx.BoxSizer(wx.VERTICAL)

        self.subtitleData = {'사과':'사과는 맛있어','배':'배는 맛있어',
                             '오렌지':'오렌지는 맛있어','귤':'귤는 맛있어',
                             '포도':'포도는 맛있어','프로틴':'프로틴는 맛있어'}

        self.lblSubtitle = wx.StaticText(self.pnlSubtitle,label='가사')
        subbx3.Add(self.lblSubtitle, 0, wx.ALL, 5 )

        self.pnlSubtitle.SetSizer(subbx3)
        self.pnlSubtitle.Layout()
        subbx3.Fit(self.pnlSubtitle)
        boxSizers.Add(self.pnlSubtitle,1, wx.EXPAND |wx.ALL, 5 )

        self.SetSizer(boxSizers)
        self.Layout()
        
        self.Centre()
        self.Show()

        self.cmbSinger.Bind(wx.EVT_COMBOBOX,self.OnCombo)
        self.lcmSong.Bind(wx.EVT_LISTBOX,self.OnListBox)

    def OnCombo(self,event):
        singer = self.cmbSinger.GetValue()
        for i in self.songData[singer]:
            self.lcmSong.Append(i)


    def OnListBox(self,event):
        idx = self.lcmSong.GetSelection()
        song = self.lcmSong.Items[idx]
        self.lblSubtitle.SetLabelText(song)






if __name__ == '__main__':
    app = wx.App()
    frame = MusicFrame(None)

    app.MainLoop()