import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent=None,title='버튼 연습',)
        self.InitUI() # 화면 구성을 위한 함수
        self.Center()

    def InitUI(self):
        panel = wx.Panel(self) # Panel__init__()
        #wx.StaticText(parent,label='',pos=(,)) pos 1 : 1 pixel
        wx.StaticText(panel,label='아이디',pos=(5,5))
        wx.StaticText(panel,label='비밀 번호',pos=(5,40))

        self.txtId = wx.TextCtrl(panel,pos = (70,5),size=(200,-1))
        self.txtPassword = wx.TextCtrl(panel,pos = (70,40))

        btnInput = wx.Button(panel,label='Button',pos=(5,100),size=(70,-1))
        tglButton = wx.ToggleButton(panel,label='Toggle',pos=(90,100),size=(70,-1))
        btnExit = wx.Button(panel,label='종료',pos=(180,100),size=(70,-1))

        btnInput.Bind(wx.EVT_BUTTON,self.OnInput)
        btnExit.Bind(wx.EVT_BUTTON,self.OnExit)

        tglButton.Bind(wx.EVT_TOGGLEBUTTON,self.OnToggle)

    def OnInput(self,event):
        #대화형 상자
        dig = wx.MessageDialog(self,message='일반 버튼 처리',caption='처리',style=wx.OK)
        #자식창이 켜있으면 부모창이 작동안됨 : modal
        # 작동됨 madaless
        dig.ShowModal()
        dig.Destroy()

        self.txtId.SetLabelText('메롱')
        self.txtPassword.SetLabelText('1234')

    def OnExit(self,event):
        print('프로그램 종료합니다')
        self.Close(True)

    def OnToggle(self,event):
        print(event.GetEventObject())
        print(event.GetEventObject().GetValue())

        if event.GetEventObject().GetValue():
            self.SetTitle('토글 연습')
            self.SetSize(500,250)
        else :
            self.SetTitle('')
            self.SetSize(300,250)
# end class MyFrame

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()