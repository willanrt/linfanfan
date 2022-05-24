# -*- coding: utf-8 -*-
"""
Created on Wed May 18 21:27:19 2022

@author: LH0

应用场景：本项目为某网购平台，提供订单信息及状态查询、新用户注册等功能。

特色功能：(1)对从未在本平台买过商品的新用户提供折扣；(2)对新注册用户信息与数据库对比，避免重复注册；
(3)同一用户若多次购买商品，则数据库中分多行展示；故用户登陆后首先需要输入订单号并核对，无误后才能进行查询。
"""

import wx
import pymysql

conn = pymysql.connect(host="localhost",user='root',password='123456',db='data',charset='utf8')
cur = conn.cursor()
sql1 = '''select NAME,PASSWORD from GOODS'''
cur.execute(sql1)
comb_sql = cur.fetchall()
cur.close()
conn.close()

class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'用户登录',size=(390,230))
        self.panel = wx.Panel(self)
        self.title = wx.StaticText(self.panel,label = "请输入账号密码以登录",pos=(125,15))
        self.account_input = wx.TextCtrl(self.panel,pos = (60,40),size=(250,25))
        self.password_input = wx.TextCtrl(self.panel,pos = (60,80),size=(250,25),style=wx.TE_PASSWORD)
        self.button_login = wx.Button(self.panel,label="登录",pos=(80,130))
        self.button_register = wx.Button(self.panel,label="注册账号",pos=(200,130))
        self.button_login.Bind(wx.EVT_BUTTON,self.login)
        self.button_register.Bind(wx.EVT_BUTTON,self.register) 
    
    def login(self,event):
        global account_input
        account_input = self.account_input.GetValue()
        password_input = self.password_input.GetValue()
        comb_input = (account_input,password_input)
        if comb_input in comb_sql:
            self.Destroy()
            frame = wx.Frame(None,title="客服机器人",pos=(100,200),size=(600,300))
            self.panel = wx.Panel(frame)
            self.title = wx.StaticText(self.panel,label="您想问点啥？",pos=(20,80))
            self.input_path = wx.TextCtrl(self.panel,pos=(20,100),size= (550,24))
            self.title1 = wx.StaticText(self.panel,label="请输入订单号：",pos=(20,39))
            self.id_input = wx.TextCtrl(self.panel,pos=(100,35),size= (150,24))
            self.button_inquire = wx.Button(self.panel,label="查询",pos=(430,35))
            self.button_check = wx.Button(self.panel,label="核对",pos=(340,35))
            self.button_check.Bind(wx.EVT_BUTTON,self.check)
            self.button_inquire.Bind(wx.EVT_BUTTON,self.inquire)
            self.output_text = wx.TextCtrl(self.panel,pos=(20,150),size=(550,50),style=wx.TE_MULTILINE)
            conn = pymysql.connect(host="localhost",user='root',password='123456',db='data',charset='utf8')
            cur = conn.cursor()
            sql4 = '''select NAME,COMMODITY from GOODS'''
            cur.execute(sql4)
            comb_sql1 = cur.fetchall()
            comb_1 = (account_input,None)
            if comb_1 in comb_sql1:
                welcome_message = '欢迎光临本平台。查询到您为新用户，现为您发放满60-15的优惠券。请您注意查收!'
            elif comb_1 not in comb_sql1:
                welcome_message = '欢迎光临本平台。您可在下方输入关键词获取相关信息。请问您购买的商品是什么？'
            self.output_text.SetValue("".join(welcome_message))
            frame.Show()
        else:
            message1 = "您输入的用户名或密码错误。\n请重试或联系管理员。"
            title1 = "请注意"
            wx.MessageBox(message1,title1)
        
    def register(self,event):
        name_new = self.account_input.GetValue()
        pwd_new = self.password_input.GetValue()
        comb_new = (name_new,pwd_new)
        try:
           if comb_new in comb_sql:
               message4 = "账号已存在。\n请勿重复注册。"
               title4 = "系统提示"
               wx.MessageBox(message4,title4)
           else:
               conn = pymysql.connect(host="localhost",user='root',password='123456',db='data',charset='utf8')
               cur = conn.cursor()
               sql3 = "insert into GOODS(NAME,PASSWORD) values(" + "'" + str(name_new) + "'" + "," + "'" + str(pwd_new) + "'" + ")"
               cur.execute(sql3)
               conn.commit()
               conn.close()
               message2 = "您已在本平台注册成功！"
               title2 = "系统提示"
               wx.MessageBox(message2,title2)
        except:
            message3 = "注册失败，请重试！"
            title3 = "系统提示"
            wx.MessageBox(message3,title3)
            
    def check(self,event):
        id_number1 = self.id_input.GetValue()
        id_number = int(id_number1)
        comb_2 = (id_number,account_input)
        conn = pymysql.connect(host="localhost",user='root',password='123456',db='data',charset='utf8')
        cur = conn.cursor()
        sql5 = '''select ID,NAME from GOODS'''
        cur.execute(sql5)
        comb_sql2 = cur.fetchall()
        if comb_2 not in comb_sql2:
            message4 = "核对信息有误，无法提供查询"
            title4 = "系统提示"
            wx.MessageBox(message4,title4)
        elif comb_2 in comb_sql2:
            message5 = "订单已查询到！"
            title5 = "系统提示"
            wx.MessageBox(message5,title5)
        sql6 = "select * from GOODS where ID = " + str(id_number) + " and NAME = " + "'" + str(account_input) + "'"
        cur.execute(sql6)
        result = cur.fetchall()
        global result_deal
        result_deal = result[0]
        conn.close()
        
    def inquire(self,event):
        import re
        question = self.input_path.GetValue()
        number = result_deal[0]
        company = result_deal[5]
        state = result_deal[6]
        start_time = result_deal[7]
        end_time = result_deal[8]
        start_local = result_deal[9]
        end_local = result_deal[10]
        account = result_deal[11]
        complaint_number = str(result_deal[12])
        match1 = re.search(r"[7七][天日]无[条件|理由]",question)
        match2 = re.search(r"订单号",question)
        match3 = re.search(r"发货地|哪发货",question)
        match4 = re.search(r"什么快递|快递公司",question)
        match5 = re.search(r"时候发货|发货时间",question)
        match6 = re.search(r"[时候|多久]到|[收|到]货时间",question)
        match7 = re.search(r"包邮",question)
        match8 = re.search(r"发票",question)
        match9 = re.search(r"[商品|订单]状态",question)
        match10 = re.search(r"投诉",question)
        match11 = re.search(r"人工",question)
        match12 = re.search(r"赠品",question)
        match13 = re.search(r"优惠券",question)
        match14 = re.search(r"发去哪",question)
        if match1 != None:
            answer = '亲！本店所有商品均支持7天无理由退换货哟！'
        elif match2 != None:
            answer = '亲！您的订单号是' + number
        elif match3 != None:
            answer = '亲！您的商品是从' + start_local + '发货的喔！'
        elif match4 != None:
            answer = '亲！本店统一发' + company + '哟，如有不便还望您理解！'
        elif match5 != None:
            answer = '亲！正常情况下预计' + start_time + '发货呢！'
        elif match6 != None:
            answer = '亲！正常情况下预计' + end_time + '到货呢！具体到货时间均以快递实际运输情况为准。'
        elif match7 != None:
            answer = '亲！本店所有商品都支持包邮哟！' 
        elif match8 != None:
            answer = '亲！本店所有商品都可以开发票哟！'
        elif match9 != None:
            answer = '亲！您的商品目前正在' + state + '中，请耐心等待'
        elif match10 != None:
            answer = '您好！亲！若要投诉请拨打电话' + complaint_number
        elif match11 != None:
            answer = '亲！正在为您转接到人工客服，请稍等。' 
        elif match12 != None:
            answer = '您好！亲！这个商品' + account + '赠品。'
        elif match13 != None:
            answer = '亲！很抱歉，这个商品的优惠券已经抢光了。'
        elif match14 != None:
            answer = '亲！您的商品是发往' + end_local + '的喔！'
        else:
            answer = "对不起，智能客服没有听懂！现在为您转接到人工客服"
        self.output_text.Clear()
        self.output_text.SetValue(answer)
        
        
if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None,-1,)
    frame.Show()
    app.MainLoop()