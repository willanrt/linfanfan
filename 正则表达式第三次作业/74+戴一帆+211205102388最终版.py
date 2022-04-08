import re
ID = '89757'
Name = '手机'
Price = '6000'
Company = "百世汇通"
State = "拣货"
Start_time = "4.1"
End_time = "4.3"
Start_local = "深圳"
End_local = "珠海"
Account = 'miss/20210307'
Complaints = '投诉'
while True:
    问题 = input()
    type1 = r"公司|发.+快递"
    guize1 = re.findall(type1, 问题)
    if guize1 == []:
        pass
    else:
        print("亲！你的快递是%s。" % Company)

    type2 = r"什么时候发货？|多久发货|.+时候发货"
    guize2 = re.findall(type2, 问题)
    if guize2 == []:
        pass
    else:
        print("你的快递估计在%s发货。" % Start_time)

    type3 = r"多.+到|时候到"
    guize3 = re.findall(type3, 问题)
    if guize3 == []:
        pass
    else:
        print("你的快递估计在%s到达。" % End_time)

    type4 = r"7天无理由|7天无条件"
    guize4 = re.findall(type4, 问题)
    if guize4 == []:
        pass
    else:
        print("亲！我们绝对支持7天无理由退货的并回退两倍邮费。")

    type5 = r"优惠券"
    guize5 = re.findall(type5, 问题)
    if guize5 == []:
        pass
    else:
        print("亲！我们会提供本店满1000元减300元的优惠券。")

    type6 = r"在.+发货|发货地址"
    guize6 = re.findall(type6, 问题)
    if guize6 == []:
        pass
    else:
        print("你的快递在%s发货。" % Start_local)

    type7 = r"包邮"
    guize7 = re.findall(type7, 问题)
    if guize7 == []:
        pass
    else:
        print("亲！该商品为贵重物品，需要本人亲自查验签收并支付50元快递费。")

    type8 = r"赠品"
    guize8 = re.findall(type8, 问题)
    if guize8 == []:
        pass
    else:
        print("亲！该商品为贵重物品，我们将随机发放赠品，赠品详细在商品介绍里有详细介绍。")

    type9 = r"订单号"
    guize9 = re.findall(type9, 问题)
    if guize9 == []:
        pass
    else:
        print("亲！你的订单号是%s。" % ID)

    type10 = r"投诉"
    guize10 = re.findall(type10, 问题)
    if guize10 == []:
        pass
    else:
        print("亲！请千万不要投诉我，我是小可怜！")

    type11 = r"发票"
    guize11 = re.findall(type11, 问题)
    if guize11 == []:
        pass
    else:
        print("亲！如果你需要发票，请联系人工客服并提交Account。")

    type12 = r"价格"
    guize12 = re.findall(type12, 问题)
    if guize12 == []:
        pass
    else:
        print("亲！商品原价%s元。"%Price)
    
    end = '谢谢' # 顾客输入“谢谢”，即退出机器人客服服务。
    if 问题 == end:
        print("亲！给个五星好评哦，非常感谢!")
        break
