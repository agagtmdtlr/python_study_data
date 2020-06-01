import wx
import wx.xrc
import sqlite3

class MyFrame2 ( wx.Frame ):
    dbname = 'emp.db'
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"id :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txtId = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtId, 0, wx.ALL, 5 )
        
        self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"name : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.txtName = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtName, 0, wx.ALL, 5 )
        
        self.btnInsert = wx.Button( self.m_panel1, wx.ID_ANY, u"추가", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.btnInsert, 0, wx.ALL, 5 )

        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.lstList = wx.ListCtrl( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer3.Add( self.lstList, 1, wx.ALL, 5 )
        
        self.m_panel2.SetSizer( bSizer3 )
        self.m_panel2.Layout()
        bSizer3.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        self.btnInsert.Bind(wx.EVT_BUTTON, self.OnBtnInsert)
        
        self.DbLoad()
        print('완료')
        
    def OnBtnInsert(self, event):
        newId = self.txtId.GetValue()
        newName = self.txtName.GetValue()
        # insert
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()

        sql = 'insert into employees values(?,?)'
        indata = (newId,newName)
        cur.execute(sql,indata)

        conn.commit()

        cur.close()
        conn.close()
        # insert
        # default
        self.txtId.SetValue('')
        self.txtName.SetValue('')
        # default
        # reload list
        idx = self.lstList.InsertItem(1000,0)
        print(idx)
        self.lstList.SetItem(idx,0,newId)
        self.lstList.SetItem(idx,1,newName)
        # reload list

    def DbLoad(self):
        #ListCtrl 초기화
        self.lstList.ClearAll()
        #ListCtrl 칼럼 추가 ( 칼럼 인덱스, 칼럼명 , 너비 )
        self.lstList.InsertColumn(0,'id',width=100)
        self.lstList.InsertColumn(1,'name',width=100)

        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()

        sql = 'select * from employees'
        cur.execute(sql)
        for row in cur :
            idx =  self.lstList.InsertItem(1000,0)
            self.lstList.SetItem(idx,0, row[0])
            self.lstList.SetItem(idx, 1, row[1])
        cur.close()
        conn.close()
        
    def __del__( self ):
        pass

if __name__ == '__main__':
    app = wx.App()
    MyFrame2(None).Show()
    app.MainLoop()