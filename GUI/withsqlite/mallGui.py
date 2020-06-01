import wx
import wx.xrc
import sqlite3


class MyDialog(wx.Dialog):
    def __init__(self,parent,title,dlgdict):
        super().__init__(parent=parent,title=title)
        self.SetSize(200,300)
        self.mainPanel = wx.Panel(self)
        self.vtBoxSizer = wx.BoxSizer(wx.VERTICAL)

        for key,val in dlgdict.items():
            lbltxt = wx.StaticText(self.mainPanel,label= key+' : '+val )
            self.vtBoxSizer.Add(lbltxt,0,wx.ALIGN_CENTER,5)

        self.closekButton = wx.Button(self.mainPanel, label="Close")

        self.vtBoxSizer.Add(self.closekButton, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.mainPanel.SetSizer(self.vtBoxSizer)

        self.Bind(wx.EVT_BUTTON, self.OnClose, self.closekButton)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnClose(self, e):
        self.Destroy()

    def __del__(self):
        pass


class MyFrame2(wx.Frame):
    dbname = 'mall.db'

    tabledict = {'부서': 'departments',
                 '직원': 'employees',
                 '고객': 'customers'}
    # print(tabledict[dictkey]) # test
    colname = {'부서': ['dno', 'name', 'locations', 'tel'],
               '직원': ['eid', 'name', 'dno', 'jikcode', 'pay', 'hiredate', 'gender'],
               '고객': ['cid', 'name', 'tel', 'juminno', 'eid']}

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='Mall Db', pos=wx.DefaultPosition,
                          size=wx.Size(500, 400), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(500, 50), wx.TAB_TRAVERSAL)
        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        rdboxTableChoices = [u"부서", u"직원", u"고객"]
        # imsi = ["부서","직원","고객"]
        self.rdboxTable = wx.RadioBox(self.m_panel4, wx.ID_ANY, u"테이블", wx.DefaultPosition,wx.Size(300,-1),
                                      rdboxTableChoices, 1, wx.RA_SPECIFY_ROWS)
        self.rdboxTable.SetSelection(0)
        bSizer6.Add(self.rdboxTable, 0, wx.ALL, 5)

        self.btnTable = wx.Button(self.m_panel4, wx.ID_ANY, u"선택", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.btnTable, 0, wx.ALL, 5)

        self.m_panel4.SetSizer(bSizer6)
        self.m_panel4.Layout()
        bSizer5.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel7 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.lblSearch = wx.StaticText(self.m_panel7, wx.ID_ANY, u"키워드검색", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblSearch.Wrap(-1)
        bSizer8.Add(self.lblSearch, 1, wx.ALIGN_CENTER, 5)

        self.txtKwd = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.txtKwd, 2, wx.ALIGN_CENTER, 5)

        self.btnSearch = wx.Button(self.m_panel7, wx.ID_ANY, u"조회", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.btnSearch, 1, wx.ALIGN_CENTER, 5)

        self.m_panel7.SetSizer(bSizer8)
        self.m_panel7.Layout()
        bSizer8.Fit(self.m_panel7)
        bSizer5.Add(self.m_panel7, 1, wx.EXPAND | wx.ALL, 5)
        # if use wx.LC_ICON
        # wx._core.wxAssertionError: C++ assertion "info.m_col == 0"
        # failed at ..\..\src\msw\listctrl.cpp(3594)
        # in wxConvertToMSWListItem(): columns only exist in report view
        # solution :
        self.lstlist = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(500, 200), wx.LC_REPORT)
        bSizer5.Add(self.lstlist, 0, wx.ALL, 5)

        self.SetSizer(bSizer5)
        self.Layout()

        self.Centre(wx.BOTH)
        self.btnTable.Bind(wx.EVT_BUTTON,self.OnBtnTable)
        self.btnSearch.Bind(wx.EVT_BUTTON,self.OnBtnSearch)
        self.lstlist.Bind(wx.EVT_LIST_ITEM_SELECTED,self.OnDetail)

    def OnDetail(self,event):
        idx =event.GetItem().GetId()
        lens = self.lstlist.ColumnCount
        dlgdict = { self.colname[self.dictkey][i]:self.lstlist.GetItem(idx,i).Text for i in range(lens)}
        # print(idx)
        # print(event.Column)
        # print(self.lstlist.GetItem(idx))
        # print(self.lstlist.GetItem(idx,1).Text)
        # print(self.lstlist.ColumnCount)
        print(dlgdict)
        dlg = MyDialog(self, "Detail Dialog",dlgdict)
        dlg.Show()

    def OnBtnTable(self,event):
        conn,cur = self.callDb()

        idx = self.rdboxTable.GetSelection()
        self.dictkey = self.rdboxTable.GetString(idx)
        self.tablename = self.tabledict[self.dictkey]
        sql = 'select * from %s' %(self.tabledict[self.dictkey])
        # tables = cur.execute(sql,(tabledict[dictkey],))
        tables = cur.execute(sql)
        self.reloadList(tables)
        cur.close()
        conn.close()

        boximsi = wx.BoxSizer()


    def OnBtnSearch(self,event,where = None):
        kwd = self.txtKwd.GetValue()
        conn,cur = self.callDb()

        sql = 'select * from {} where name like "{}"'.format(self.tablename,'%'+kwd+'%')
        tables = cur.execute(sql)

        self.reloadList(tables)
        self.txtKwd.SetValue('')
        cur.close()
        conn.close()

        self.Show()


    def reloadList(self,tables):
        self.lstlist.ClearAll()
        for i, val in enumerate(self.colname[self.dictkey]):
            # print(i) # test
            self.lstlist.InsertColumn(i, val, width=60)
        for row in tables:
            idx = self.lstlist.InsertItem(1000, 0)
            for i, val in enumerate(row):
                self.lstlist.SetItem(idx, i, str(val))

    def callDb(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        return (conn,cur)

    def __del__(self):
        pass


if __name__ == '__main__':
    app = wx.App()
    myframe = MyFrame2(None)
    myframe.Show()
    app.MainLoop()