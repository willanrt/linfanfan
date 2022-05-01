import re
from itertools import chain
import pymysql
class WenTi:
    # 1.定义NAME函数
    def name(self):
        f = r"是.+商品|我买的是+.|我的商品是.+什么？|我的商品是.*?"
        g = re.findall(f, wenti)
        return g

    # 2.定义PRICE函数
    def price(self):
        f = r"(多贵|金额|价格|钱)"
        g = re.findall(f, wenti)
        return g

    # 3.定义COMPANY函数
    def company(self):
        f = r"(家).+(快递)|(快递公司)"
        g = re.findall(f, wenti)
        return g

    # 4.定义COMPLAINTS函数
    def complaints(self):
        f  = r"(投诉)"
        g = re.findall(f, wenti)
        return g

    # 5.定义START_LOCAL函数
    def start_local(self):
        f = r"((发货).+(地址)|(在哪发货))|.+发货地址.+"
        g = re.findall(f, wenti)
        return g

    # 6.定义END_LOCAL函数
    def end_local(self):
        f = r"((送货|到货).*?(地址|地点)|(送到哪)|(寄到哪力)|(哪个快递站点.*?))"
        g = re.findall(f, wenti)
        return g

    # 7.定义START_TIME函数
    def start_time(self):
        f = r".*?(出库的时间|出货的时间|出厂的时间|发货的时间).+"
        g = re.findall(f, wenti)
        return g

    # 8.定义STATE函数
    def state(self):
        f = r"(订单|定单|货物|商品|快递).*(怎么样了|状态|怎么了|到哪里了|到哪一步)"
        g = re.findall(f, wenti)
        return g

    # 9.定义END_TIME函数
    def end_time(self):
        f = r"多.+到|.+时候到|.+快递多久|最快几号到"
        g = re.findall(f, wenti)
        return g

    # 10.定义（匹配7天无理由）的函数
    def day(self):
        f = r"(7天无理由|7天无条件)"
        g = re.findall(f, wenti)
        return g

    # 11.定义SAVE函数
    def save(self):
        f = r"(优惠|优惠券)"
        g = re.findall(f, wenti)
        return g
    #12.定义发票函数
    def fapiao(self):
        f = r"(发票)"
        g = re.findall(f, wenti)
        return g
print("亲爱的顾客，您好！这里是机器小八，为您服务。(输入“bye”可退出)")
while True:
    conn = pymysql.connect(host="localhost", user="root", password="1024",
                           db="作业", charset='utf8')  # 连接
    cur = conn.cursor()  # 游标
    sql = "select ACCOUNT from goods"
    sql1 = "select ID from goods"
    cur.execute(sql)
    # 运行
    result = cur.fetchall()
    Name = list(chain.from_iterable(result))
    while True:
        Account = input("Your account is:")
        if Account in Name:
            print("成功找到相应账户")
            break
        else:
            print("你的Account有问题。")
    cur.execute(sql1)
    result1 = cur.fetchall()
    id1 = list(chain.from_iterable(result1))
    while True:
        ID = input("Your id is:")
        if ID in id1:
            print("找到相应id的商品信息")
            break
        else:
            print("找不到您购买记录。")

    id = "'" + str(ID) + "'"
    account = "'" + str(Account) + "'"
    sql2 = "select * from goods where ACCOUNT = %s and ID = %s" % (account, id)
    cur.execute(sql2)
    result2 = cur.fetchmany()
    cur.close()
    conn.close()
    for i in result2:
        data = i
    if __name__ == "__main__":
        WEN = WenTi()
    end = "bye"
    wenti = input("亲爱的顾客，您的问题是?")
    while True:
        if not WEN.name():
            pass
        else:
            print("问题是：",wenti)
            print("亲，您购买的商品是%s。" % data[1])
        if not WEN.price():
            pass
        else:
            print("问题是：",wenti)
            print("亲，您购买的商品为%s元。" % data[2])
        if not WEN.company():
            pass
        else:
            print("问题是：",wenti)
            print("亲，您的快递是%s。" % data[3])
        if not WEN.state():
            pass
        else:
            print("问题是：",wenti)
            print("亲，您购买的商品已经%s。" % data[4])
        if not WEN.start_time():
            pass
        else:
            print("问题是：",wenti)
            print("亲，您的快递估计在%s发货。" % data[5])
        if not WEN.end_time():
            pass
        else:
            print("问题是：",wenti)
            print("亲，您的快递估计在%s到达。" % data[6])
        if not WEN.start_local():
            pass
        else:
            print("问题是：",wenti)
            print("亲，您的快递在%s发货。" % data[7])
        if not WEN.end_local():
            pass
        else:
            print("问题是：",wenti)
            print("亲，您购买的商品将送到%s。" % data[8])
        if not WEN.complaints():
            pass
        else:
            print("问题是：",wenti)
            print("亲！请您千万不要投诉我，我是小可怜！")
        if not WEN.day():
            pass
        else:
            print("问题是：",wenti)
            print("亲,我们无条件支持7天无理由退货的哦。")
        if not WEN.save():
            pass
        else:
            print("问题是：",wenti)
            print("亲！联系人工客服，以获得更多优惠消息。")
        if not WEN.fapiao():
            pass
        else:
            print("问题是：" ,wenti)
            print("亲！如果你需要发票，请联系人工客服")    
        if not WEN.day() and not WEN.save() and not WEN.name() and not WEN.price() and not WEN.company()and not WEN.state() and not WEN.start_time() and not WEN.end_time() and not WEN.start_local() and not WEN.end_local() and not WEN.complaints() and not WEN.fapiao() and wenti != "bye":
            print("问题是：",wenti)
            print("您的问题太难了，正为您联通人工客服")
        if wenti == end:
            print("问题是：",wenti)
            print("亲！给个五星好评哦，非常感谢!")
            break
        wenti = input("亲爱的顾客，您还有其他问题吗?")
    if wenti == end:
        print(wenti)
        print("谢谢")
        break
