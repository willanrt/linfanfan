import re
shuju = "Harry Potter and the Philosopher's Stone is the first novel in the Harry Potter series written by J. K. Rowling and featuring Harry Potter."
x = re.findall(r"\b\w",shuju)
print(x)
import re
xinxi = '''
定单编号：  1049
寄件人：   张三
收件人：   李四
寄件地址：  珠海市
到货地址： 武汉市
定单编号：  1050
寄件人：   王五
收件人：   赵六
寄件地址：  天津市
到货地址：  北京市
定单编号：  1049
寄件人：   钱七
收件人：   周八
寄件地址：  海口市
到货地址： 广州市
'''
y = re.findall( r"定单编号：  (\d{4})\n寄件人：   (.+)\n收件人：   (.+)\n寄件地址：  (.+)\n到货地址：  ?(.+)", xinxi)
print(y)
import re
youxiang = '11120015613@qq.com，11abcakj@google.com，11xaksjdnas23@12306.com， abc!askdnla@gmail.com，56378925@yoole.com，1568#@ert.com，18923@zhbit.com，11683@hhhh.com。'
M =re.sub(r"@\w+.com", "@qq.com", youxiang)
print(M)
import re
wenzi = '2022年CPI同比涨幅会如何变动?如何实现3%的目标？政府出台的对中小微企业的帮扶释放了哪些信号？’就业目标新增1100万人以上’，”如何看待灵活就业？”实现共同富裕应当走什么样的路径？\今天（3月9日）晚上.《两会夜话》直播特别节目第五期，全国政协委员杨伟民/王一鸣，全国人大代表张兆安邀您云上夜话，一起来聊聊和GDP有关的那些事。(总台记者 薛晨 刘苏 王新琦 李竟成 颜蔚然)；'
print(re.split(r"[？/.。‘’“”《》()（）\\]", wenzi))