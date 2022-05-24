####建立三层结构，登录---商品---询问
import wx
import pymysql
import re


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '客服系统', size=(400, 300))
        self.panel = wx.Panel(self)
        self.name = wx.StaticText(self.panel, label="账户名:", pos=(70, 100))
        self.account = wx.TextCtrl(self.panel, pos=(130, 100), size=(150, 30))
        self.number = wx.StaticText(self.panel, label="密  码:", pos=(70, 150))
        self.passwd = wx.TextCtrl(self.panel, pos=(130, 150), size=(150, 30))
        self.ok = wx.Button(self.panel, label="登录", pos=(200, 200))
        self.ok.Bind(wx.EVT_BUTTON, self.sure)
        self.no = wx.Button(self.panel, label="取消", pos=(100, 200))
        self.no.Bind(wx.EVT_BUTTON, self.exit)

    def sure(self, event):
        name = "'" + self.account.GetValue() + "'"
        passwd = "'" + self.passwd.GetValue() + "'"
        conn = pymysql.Connect(host='localhost', user='root', password='leech', db='world', charset='utf8')
        # 打开游标
        cur = conn.cursor()
        # 编写sql
        sql = "select * from goods_new where ACCOUNT = %s and PASSWD = %s" % (name, passwd)
        # conn.rollback()
        cur.execute(sql)
        # 运行
        number = cur.fetchmany()
        # print(number)
        cur.close()
        conn.close()
        if number == ():
            message = "你的账户名或密码错误！"
            wx.MessageBox(message)
        else:
            self.Destroy()  #######事件停止后是否删除顶层窗口
            frame = wx.Frame(None, title="帐单查询", pos=(100, 200), size=(500, 400))
            self.panel = wx.Panel(frame)
            self.title = wx.StaticText(self.panel, label="请选择你要查询的商品订单", pos=(10, 5))
            self.remind_text = wx.StaticText(self.panel, label="请选择:", pos=(5, 225))
            self.input_text = wx.TextCtrl(self.panel, pos=(5, 255), size=(470, 100))
            self.open = wx.Button(self.panel, label="确定", pos=(400, 225))
            self.open.Bind(wx.EVT_BUTTON, self.computer)
            self.input_goods = wx.Button(self.panel, label="取消", pos=(320, 225))
            self.input_goods.Bind(wx.EVT_BUTTON, self.back)
            self.output_text = wx.TextCtrl(self.panel, pos=(8, 25), size=(470, 200), style=wx.TE_MULTILINE)
            frame.Show()
    def open(self, event):
        self.Destroy()  #######事件停止后是否删除顶层窗口
        frame = wx.Frame(None, title="客服", pos=(100, 200), size=(500, 400))
        self.panel = wx.Panel(frame)
        self.title = wx.StaticText(self.panel, label="很高兴为你服务", pos=(10, 5))
        self.remind_text = wx.StaticText(self.panel, label="请输入:", pos=(5, 225))
        self.input_text = wx.TextCtrl(self.panel, pos=(5, 255), size=(470, 100))
        self.open = wx.Button(self.panel, label="发送", pos=(400, 225))
        self.open.Bind(wx.EVT_BUTTON, self.computer)
        self.output_text = wx.TextCtrl(self.panel, pos=(8, 25), size=(470, 200), style=wx.TE_MULTILINE)
        frame.Show()

    def good(self, event):
        global data
        Q = self.input_text.GetValue()
        name = "'" + self.account.GetValue() + "'"
        passwd = "'" + self.passwd.GetValue() + "'"
        goods = "''" + self.GetValue() + "'"
        conn = pymysql.Connect(host='localhost', user='root', password='leech', db='world', charset='utf8')
        # 打开游标
        cur = conn.cursor()
        # 编写sql
        sql = "select * from goods_new where ACCOUNT = %s and PASSWD = %s and NAME = %s" % (name, passwd, goods)
        # conn.rollback()
        cur.execute(sql)
        # 运行
        cur.close()
        conn.close()
        self.number = cur.fetchmany()
        for lin in self.number:
            data = lin
        return data

    def computer(self, event):
        computer = """亲，您的问题是什么？
"""
        data = self.good(event)
        Q = self.input_text.GetValue()
        # ID
        def id():
            gui = r"(订单|定单|货物|商品|快递).*?(编号|号码|单号|号)"
            pi = re.findall(gui, Q)
            return pi

        # PRICE
        def price():
            gui = r"(价格|钱)"
            pi = re.findall(gui, Q)
            return pi

        # COMPANY
        def company():
            gui = r"(家).*?(快递)|(快递公司)"
            pi = re.findall(gui, Q)
            return pi

        # COMPLAINTS
        def complaints():
            gui = r"(投诉)"
            pi = re.findall(gui, Q)
            return pi

        # START_LOCAL
        def start_local():
            gui = r"((发货).*?(地址|地点)|(在哪发货))"
            pi = re.findall(gui, Q)
            return pi

        # END_TIME
        def end_time():
            gui = r"多.+到|时候到[达货]"
            pi = re.findall(gui, Q)
            return pi

        # START_TIME
        def start_time():
            gui = r"[什么时候|多久].+(出库|出货|出发|送货|发货)"
            pi = re.findall(gui, Q)
            return pi

        # 匹配7天无理由
        def day():
            gui = r"(7天无理由|7天无条件)"
            pi = re.findall(gui, Q)
            return pi

        # SAVE
        def save():
            gui = r"(优惠)"
            pi = re.findall(gui, Q)
            return pi

        # STATE
        def state():
            gui = r"(订单|定单|货物|商品|快递).*?(怎么样了|状态|怎么了|哪一步)"
            pi = re.findall(gui, Q)
            return pi

        # END_LOCAL
        def end_local():
            gui = r"((送货|到货).*?(地址|地点)|(送到哪)|(送到那)|(寄到哪))"
            pi = re.findall(gui, Q)
            return pi

        if not day():
            pass
        else:
            print("亲，我们是绝对支持7天无理由退货的。")
        if not save():
            pass
        else:
            print("亲，你购买的商品已经很便宜了。")
        if not id():
            pass
        else:
            print("亲，您的订单号是%s。" % data[0])
        if not price():
            pass
        else:
            print("亲，您购买的商品是%s元。" % data[2])
        if not company():
            pass
        else:
            print("亲，您的快递是%s。" % data[3])
        if not state():
            pass
        else:
            print("亲，你购买的商品已经%s。" % data[4])
        if not start_time():
            pass
        else:
            print("亲，您的快递估计在%s发货。" % data[5])
        if not end_time():
            pass
        else:
            print("亲，您的快递估计在%s到达。" % data[6])
        if not start_local():
            pass
        else:
            print("亲，您的快递在%s发货。" % data[7])
        if not end_local():
            pass
        else:
            print("亲，你购买的商品将送到%s。" % data[8])
        if not complaints():
            pass
        else:
            print("亲！请千万不要投诉我，含泪请求！")
        if not day() and not save() and not id() and not price() and not company() and not state() and not start_time() \
                and not end_time() and not start_local() and not end_local() and not complaints() and Q != "更换密码" and Q != "none":
            print("你的问题太难了，请联系人工客服")

    def exit(self, event):
        self.account.SetValue("")
        self.passwd.SetValue("")

    def back(self, event):
        self.input_text.SetValue("")


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None, -1, )
    frame.Show()
    app.MainLoop()
