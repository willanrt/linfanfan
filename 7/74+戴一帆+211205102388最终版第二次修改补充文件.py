import random
user = int(input("次数"))
u = 0
r = 0
def robot_choice():
    return random.choice( ["剪刀", "石头", "布"])
while user > 0:
    user_1 = input("请出(石头/剪刀/布):")
    robot = robot_choice()
    if (user_1 == "石头" and robot == "剪刀") or (user_1 == "剪刀" and robot == "布") or (user_1 == "布" and robot == "石头"):
        print("你出：", user_1)
        print("电脑:" + robot)
        print("你赢了 ")
        u += 1
    elif (user_1 == "石头" and robot == "石头") or (user_1 == "剪刀" and robot == "剪刀") or (user_1 == "布" and robot == "布"):
        print("你出：", user_1)
        print("电脑:" + robot)
        print("平局")
    else:
        print("你出：", user_1)
        print("电脑:" + robot)
        print("你输了")
        r += 1
    user -= 1
print(u, ":", r)
if u > r :
    print("you win")
elif u==r:
    print("draw")
else:
    print("you loss")