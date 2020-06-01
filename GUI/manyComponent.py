import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='다양한 컴포넌트')
        self.SetSize(300,800)

        panel = wx.Panel(self)

        self.label01 = wx.StaticText(panel, label='라벨은 편집이 불가능합니다.',
                                     pos=(20, 30))

        # TextCtrl
        wx.StaticText(panel,label='이름은',
                      pos=(20,70))
        self.txtName = wx.TextCtrl(panel,value='홍길동',
                                   pos=(60,60))
        # self.Bind(wx.EVT_TEXT,self.OnText,self.txtName)
        self.txtName.Bind(wx.EVT_TEXT,
                          self.OnText)
        # CheckBox
        self.chkBar = wx.CheckBox(panel,label='굵게 설정합니다',
                                  pos=(20,100))
        self.chkBar.Bind(wx.EVT_CHECKBOX,self.OnCheck)
        # RadioBox
        radioData = ['마포','용산','강남']
        self.rb = wx.RadioBox(panel,label='어디 사세요?',
                              pos=(20,130),choices=radioData)
        self.rb.Bind(wx.EVT_RADIOBOX,self.OnRadio)
        # ComboBox
        cboData = ['프랑스','이탈리아',]
        wx.StaticText(panel,label='가고 싶은 곳?',
                      pos=(20,200))
        self.cbo = wx.ComboBox(panel,
                    pos=(20,230),
                    choices=cboData,
                    style=wx.CB_READONLY)
        self.cbo.Bind(wx.EVT_COMBOBOX,self.OnCombo)
        # MultiText
        self.txtShow = wx.TextCtrl(panel,
                                   pos=(20,330),
                                   size=(250,200),
                                   style=wx.TE_MULTILINE | wx.TE_READONLY)
    def OnText(self,event):
        self.txtShow.AppendText(event.GetString())

    def OnCheck(self,event):
        style = wx.FONTSTYLE_NORMAL #글씨체
        if event.IsChecked() == True: # checkbox가 체크되어 있는지 확인하기
            self.txtShow.AppendText('굵게 설정\n') # 글씨 넣기
            weight = wx.FONTWEIGHT_BOLD #글씨 굵기
        else :
            self.txtShow.AppendText('얇게 설정\n') # 글씨 넣기
            weight = wx.FONTWEIGHT_NORMAL #글씨 굵기

        font = wx.Font(10,wx.FONTFAMILY_DEFAULT,style,weight)
        self.label01.SetFont(font)
        self.txtShow.SetFont(font)

    def OnRadio(self,event):
        self.txtShow.AppendText('거주지 : %s %s\n' %(event.GetInt(),event.GetString()))

    def OnCombo(self,event):
        self.txtShow.AppendText('여행지 : %s\n' %(event.GetString()))
# end class MyFrame

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()