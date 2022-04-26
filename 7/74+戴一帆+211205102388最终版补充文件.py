import random
u = int(input())
count = 2 *int(u)+1
o = 0
p = 0
while count:
 a = input("请出(石头/剪刀/布):")
 b = ["剪刀", "石头", "布"]  # 定义赢的列表
 win_list = [["石头", "剪刀"], ["剪刀", "布"], ["布", "石头"]]
 # 计算机随机选择出
 x = random.choice(b)
 print("你出：", a)
 print("计算机出：", x)
 q = "平局"
 w = "恭喜，你赢了"
 e = "你输了"
 if a in b:
  count -= 1
  if a == x:
    print(q)
  elif [a, x] in win_list:
    print(w)
    o += 1
  else:
    print(e)
    p += 1
 else:
  print("输入错误")
 print("你还剩余机会", count)
 print(o, ":", p)
 if o == int(u+1):
   print("玩家胜利")
   break
 elif p == int(u)+1:
   print("电脑胜利")
   break

