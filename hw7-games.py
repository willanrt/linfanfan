import random

class Game:

    #######编写属性
    def __init__(self,n):
        self.n = n
        self.choice = ["石头","剪刀","布"]
    
    
    #######内置一次的规则
    def rules(self,p_c,c_c):
        if p_c == c_c:
            p_plus = 0
            c_plus = 0
            print("这一把平局！")
        elif (p_c == "剪刀" and c_c == "布") or (p_c == "石头" and c_c == "剪刀") or (p_c == "布" and c_c == "石头"):
            p_plus = 1
            c_plus = 0
            print("这一把您赢了！")
        elif (p_c == "剪刀" and c_c == "石头") or (p_c == "石头" and c_c == "布") or (p_c == "布" and c_c == "剪刀"):
            p_plus = 0
            c_plus = 1
            print("这一把您输了！")
        return p_plus,c_plus
    
    
    ########编写一次游戏
    def start_game(self):
        p_score = 0
        c_score = 0
        n = self.n
        #print(n)
        try:
            for i in range(int(2*n) - 1):
                p_c = input("石头、剪刀、布任选其一:")
                c_list = self.choice
                c_c = random.sample(c_list,1)[0]
                print("用户选择：",p_c)
                print("电脑选择:",c_c)
                p_score_plus,c_score_plus = self.rules(p_c,c_c)
                p_score += p_score_plus
                c_score += c_score_plus
                if p_score == n:
                    print("##################您竟然赢了电脑，果然天选之人！！####################")
                    print("电脑获胜次数为：",c_score)
                    break
                elif c_score == n:
                    print("##################您竟然输给了电脑，果然天选之人！！！！####################")
                    print("用户获胜次数为：",p_score)
                    break
                if i == 2*n - 2:
                    print("您竟然与电脑未分胜负！！！！")
        except:
            print("游戏发生错误请核对游戏过程！！")



if __name__ == "__main__":
    m = input("局数选定(提示:最好选择奇数数):")
    num = (int(m)+1)/2
    games = Game(num)
    games.start_game()





