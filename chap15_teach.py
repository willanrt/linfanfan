import wx

app = wx.App()

frame = wx.Frame(parent = None,title = "hello",size = (300,300))   ###顶级窗口
txt = wx.StaticText(parent = frame,label = "账户",pos=(5,5))       ###静态数据框
path_text = wx.TextCtrl(frame,pos = (45,5),size = (50,24))         ###动态数据框
path1_text = wx.TextCtrl(frame,pos = (150,5),size = (50,24))       ###第二个动态数据框
open_button = wx.Button(frame,label="登录",pos = (370,5))          ###按钮
frame.Show()
app.MainLoop()

