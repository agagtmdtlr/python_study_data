import wx
import wx.xrc
import sqlite3
import sys

class MyDialog(wx.Dialog):
    def __init__(self, _parent, _title, *col_list):
        wx.Dialog.__init__(self, parent=_parent, title=_title)
        self.SetSize(180, 390)

        self.panel = wx.Panel(self)

        print(col_list)
        newtuple = col_list[0]
        length = len(newtuple)

        xpos, ypos = 30, 20
        for idx in range(length) :
            wx.StaticText(self.panel, label=newtuple[idx], pos=(xpos, ypos))
            ypos += 30

        self.btnClose = wx.Button(self.panel, label="닫기", pos=(xpos, ypos))
        print(xpos, ypos)
        self.Layout()

        self.Centre(wx.BOTH)

        self.Bind(wx.EVT_BUTTON, self.OnClose, self.btnClose)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def __del__(self):
        pass

    def OnClose(self, e):
        self.Destroy()

class MyFrame1(wx.Frame):
    dbname = 'mall.db'

    table_dict = {0:'departments', 1:'employees', 2:'customers'}

    column_dict = {0: ['부서번호', '부서명', '위치', '전화 번호'], 1: ['아이디', '이름', '부서번호', '직급', '급여', '입사일자', '성별'], 2: ['아이디', '이름', '전화번호', '주민 번호', '담당자']}

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='Mall Database', pos=wx.DefaultPosition,
                          size=wx.Size(722, 470), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        radioBoxChoices = [u"부서", u"사원", u"고객"]

        self.radioBox = wx.RadioBox(self.m_panel1, wx.ID_ANY, u"테이블 선택", wx.DefaultPosition, wx.DefaultSize, radioBoxChoices, 1, wx.RA_VERTICAL)
        self.radioBox.SetSelection(0)
        bSizer2.Add(self.radioBox, 0, wx.ALL, 5)

        self.btnSelect = wx.Button(self.m_panel1, wx.ID_ANY, u"조회", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.btnSelect, 0, wx.ALL, 5)

        self.btnDialog = wx.Button(self.m_panel1, wx.ID_ANY, u"대화 상자", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.btnDialog, 0, wx.ALL, 5)
        
        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.txtSearch = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.txtSearch, 0, wx.ALL, 5)

        self.btnSearch = wx.Button(self.m_panel2, wx.ID_ANY, u"검색", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.btnSearch, 0, wx.ALL, 5)

        self.m_panel2.SetSizer(bSizer3)
        self.m_panel2.Layout()
        bSizer3.Fit(self.m_panel2)
        bSizer1.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.lstCtrl = wx.ListCtrl(self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        bSizer4.Add(self.lstCtrl, 0, wx.EXPAND | wx.ALL, 5)

        self.m_panel3.SetSizer(bSizer4)
        self.m_panel3.Layout()
        bSizer4.Fit(self.m_panel3)
        bSizer1.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # 일반 변수
        self.curr_index = -1
        self.mytuple = None

        # 데이터 베이스 관련
        self.DbInitialize()

        # 이벤트 처리
        self.radioBox.Bind(wx.EVT_RADIOBOX, self.OnRadioBox)
        self.btnSelect.Bind(wx.EVT_BUTTON, self.OnSelect)
        self.btnSearch.Bind(wx.EVT_BUTTON, self.OnSearch)
        self.btnDialog.Bind(wx.EVT_BUTTON, self.OnDialog)
        self.lstCtrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnListEvent)

    def OnListEvent(self, event):
        row = event.GetItem().GetId()
        # print(row)

        columns = self.lstCtrl.GetColumnCount()
        # print(self.lstCtrl.GetColumn(2))
        self.mytuple = tuple()
        for data in range(columns):
            self.mytuple = self.mytuple + (self.lstCtrl.GetItem(row, data).GetText(), )
        # print(event.GetSelection())
        # for dd in event.GetItem():
        # print(mytuple)

    def OnDialog(self, event):
        if self.curr_index == -1:
            dlg = wx.MessageDialog(self, message='테이블을 우선 선택해 주세요.', caption='테이블 선택하기', style=wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
        else :
            if self.mytuple == None:
                dlg = wx.MessageDialog(self, message='리스트의 아이템을 선택해 주세요.', caption='리스트 아이템 선택', style=wx.OK)
                dlg.ShowModal()
                dlg.Destroy()
            else:
                dlg = MyDialog(self, "Modal Dialog", self.mytuple)
                dlg.ShowModal()

    def OnSearch(self, event):
        if self.curr_index == -1:
            dlg = wx.MessageDialog(self, message='테이블을 우선 선택해 주세요.', caption='테이블 선택하기', style=wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
        else :
            findwho = self.txtSearch.GetValue()
            print(findwho)
            self.SetColumn()
            self.FillTable(where=findwho)

    def OnSelect(self, event):
        if self.curr_index == -1:
            dlg = wx.MessageDialog(self, message='테이블을 우선 선택해 주세요.', caption='테이블 선택하기', style=wx.OK)
            dlg.ShowModal()
            dlg.Destroy()

        else :
            self.column_list = self.column_dict[self.curr_index]
            self.table_name = self.table_dict[self.curr_index]
            print(self.column_list)
            self.SetColumn()
            self.FillTable()

    def FillTable(self, where = None):
        sql = 'select * from ' + self.table_name + ' '
        if where != None :
            sql += " where name like '%" + where + "%' "

        print(sql)
        self.cur.execute(sql)

        for row in self.cur :
            idx = self.lstCtrl.InsertItem(1000, row[0])
            for su in range(len(row)):
                # print()
                self.lstCtrl.SetItem(idx, su, str(row[su]))
    # lstCtrl에 데이터 채워 넣기

    def SetColumn(self):
        self.lstCtrl.ClearAll()
        for idx in range(len(self.column_list)):
            # print(idx)
            self.lstCtrl.InsertColumn(idx, self.column_list[idx], width=100)

    def OnRadioBox(self, event):
        # print(event.GetSelection())
        # print(event.GetString())
        self.curr_index = event.GetSelection()
        self.column_list = self.column_dict[self.curr_index]
        self.table_name = self.table_dict[self.curr_index]
        print(self.table_name)

    def DbInitialize(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

if __name__ == '__main__':
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop()