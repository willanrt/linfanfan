import re
import wx
import pymysql


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '用户登录', size=(400, 250))
        self.panel = wx.Panel(self)
        self.title = wx.StaticText(
            self.panel, label="请输入账号和密码", pos=(125, 15))
        self.account_input = wx.TextCtrl(
            self.panel, pos=(60, 40), size=(250, 25))
        self.password_input = wx.TextCtrl(self.panel, pos=(
            60, 80), size=(250, 25), style=wx.TE_PASSWORD)
        self.button_login = wx.Button(self.panel, label="登录", pos=(130, 140))
        self.button_login.Bind(wx.EVT_BUTTON, self.login)

    def login(self, event):
        global account_input
        self.account_input = self.account_input.GetValue()
        password_input = self.password_input.GetValue()
        result_input = (self.account_input, password_input)
        # print(result_input)
        conn = pymysql.connect(host="localhost", user="root",
                               password="1024", db="作业", charset='utf8')  # 连接
        cur = conn.cursor()  # 游标
        sql = "select ACCOUNT,PASSWORD from goods"
        cur.execute(sql)
        # 运行
        result1 = cur.fetchall()
        # print(result1)
        cur.close()
        conn.close()
        if result_input in result1:
            self.Destroy()  # 事件停止后是否删除顶层窗口
            frame = wx.Frame(None, title="可爱的机器人小八",
                             pos=(100, 200), size=(600, 300))
            self.panel = wx.Panel(frame)
            self.title = wx.StaticText(
                self.panel, label="您的问题是？", pos=(20, 80))
            self.input_path = wx.TextCtrl(
                self.panel, pos=(20, 100), size=(550, 24))
            self.title1 = wx.StaticText(
                self.panel, label="ID：", pos=(20, 39))
            self.id_input = wx.TextCtrl(
                self.panel, pos=(100, 35), size=(150, 24))
            self.button_inquire = wx.Button(
                self.panel, label="查询", pos=(430, 35))
            self.button_check = wx.Button(
                self.panel, label="核对", pos=(340, 35))
            self.button_check.Bind(wx.EVT_BUTTON, self.check)
            self.button_inquire.Bind(wx.EVT_BUTTON, self.inquire)
            self.output_text = wx.TextCtrl(self.panel, pos=(
                20, 150), size=(550, 50), style=wx.TE_MULTILINE)
            conn = pymysql.connect(
                host="localhost", user="root", password="1024", db="作业", charset='utf8')  # 连接
            cur = conn.cursor()
            sql4 = '''select NAME,COMPANY from goods'''
            cur.execute(sql4)
            result1 = cur.fetchall()
            qw_1 = (self.account_input, None)
            if qw_1 in result1:
                welcome_message = '欢迎。'
            elif qw_1 not in result1:
                welcome_message = '欢迎！您可在下方输入关键词获取相关信息，询问客服小八。'
            self.output_text.SetValue("".join(welcome_message))
            frame.Show()
        else:
            message1 = "您输入的用户名或密码错误。\n请重试"
            title1 = "请注意"
            wx.MessageBox(message1, title1)

    def check(self, event):
        id_1 = self.id_input.GetValue()
        id_number = id_1
        result2 = (id_number, self.account_input)
        conn = pymysql.connect(host="localhost", user="root",
                               password="1024", db="作业", charset='utf8')  # 连接
        cur = conn.cursor()
        sql5 = '''select ID,ACCOUNT from goods'''
        cur.execute(sql5)
        qw_2 = cur.fetchall()
        # print(qw_2)
        if result2 not in qw_2:
            message4 = "信息核对有误"
            title4 = "系统提示"
            wx.MessageBox(message4, title4)
        elif result2 in qw_2:
            message5 = "订单已查询到！"
            title5 = "系统提示"
            wx.MessageBox(message5, title5)
        sql6 = "select * from goods where ID = " + \
            str(id_number) + " and ACCOUNT = " + \
            "'" + str(self.account_input) + "'"
        cur.execute(sql6)
        result3 = cur.fetchall()
        self.result_deal = result3[0]
        conn.close()

    def inquire(self, event):
        question = self.input_path.GetValue()
        number = self.result_deal[0]
        thing = self.result_deal[1]
        price = self.result_deal[2]
        company = self.result_deal[3]
        state = self.result_deal[4]
        start_time = self.result_deal[5]
        end_time = self.result_deal[6]
        start_local = self.result_deal[7]
        end_local = self.result_deal[8]
        f1 = re.search(r"是.+商品|我买的是+.|我的商品是.+什么？|我的商品是.*?", question)
        f2 = re.search(r"(多贵|金额|价格|钱)", question)
        f3 = re.search(r"(家).+(快递)|(快递公司)", question)
        f4 = re.search(r"(投诉)", question)
        f5 = re.search(r"((发货).+(地址)|(在哪发货))|.+发货地址.+", question)
        f6 = re.search(
            r"((送货|到货).*?(地址|地点)|(送到哪)|(寄到哪力)|(哪个快递站点.*?))", question)
        f7 = re.search(r".*?(出库的时间|出货的时间|出厂的时间|发货的时间).+", question)
        f8 = re.search(r"(订单|定单|货物|商品|快递).*(怎么样了|状态|怎么了|到哪里了|到哪一步)", question)
        f9 = re.search(r"多.+到|.+时候到|.+快递多久|最快几号到", question)
        f10 = re.search(r"(7天无理由|7天无条件)", question)
        f11 = re.search(r"(优惠|优惠券)", question)
        f12 = re.search(r"(发票)", question)
        f13 = re.search(r"ID,id", question)

        if f1 != None:
            answer = "亲，您购买的商品是" + thing
        elif f2 != None:
            answer = "亲，您购买的商品为" + price + "元"
        elif f3 != None:
            answer = "亲，您的快递是" + company
        elif f4 != None:
            answer = "亲！请您千万不要投诉我，我是小可怜！"
        elif f5 != None:
            answer = "亲，您的快递在" + start_local + "发货"
        elif f6 != None:
            answer = "亲，您购买的商品将送到" + end_local
        elif f7 != None:
            answer = "亲，您的快递在" + start_time + "发货"
        elif f8 != None:
            answer = "亲，您的快递在" + state
        elif f9 != None:
            answer = "亲，您的快递估计在" + end_time + "到达"
        elif f10 != None:
            answer = "亲,我们无条件支持7天无理由退货的哦。"
        elif f11 != None:
            answer = "亲！联系人工客服，以获得更多优惠消息。"
        elif f12 != None:
            answer = "亲！如果你需要发票，请联系人工客服"
        elif f13 != None:
            answer = number
        else:
            answer = "对不起，客服小八没有理解！现在为您转接到人工客服"
        self.output_text.Clear()
        self.output_text.SetValue(answer)


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None, -1)
    frame.Show()
    app.MainLoop()
