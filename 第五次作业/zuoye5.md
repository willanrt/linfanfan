<center><big><b>作业5</b></big></center>
<center><small>戴一帆</small></center>
<center><small>2022年4月2号</small></center>

[toc]
# 要求
i.	编写一个计算BMI的函数提示：BMI的计算方法为（BMI）=体重（kg）÷身高^2（m）；
ii.	编写一个计算体脂率FAT的函数，体质率的计算方法为： 参数a=腰围（cm）×0.74； 参数b=体重（kg）×0.082+44.74； 体脂肪重量（kg）=a－b； 体脂率=（身体脂肪总重量÷体重）×100%;
iii.	将以上的两个函数合在一起生成一个计算体重指标的类Health，其中有一个人的固定指标作为类的属性，其中身高180，体重70kg，腰围：80；
iv.	编写一个Health的子类，子类继承了Health的属性，并且拥有2个方法，分别为判断BMI和FAT的情况，并输出身体的BMI或者FAT状况，提示：BMI的正常范围在18.5-23.99;FAT的正常范围在0.15-0.18之间。
v.	调用以上Health的子类，输入计算类中默认的身体属性和自己的身体状况。

# 代码与解释
## 完成要求1
def建立计算BMI的函数
```python
# 定义一个计算BMI的的函数
def bmi():
    weight = float(input("体重（kg）：")) #输入所需体重的数据
    stature = float(input("身高（m）："))  # 输入所需身高的数据
    bmi_process = weight/(stature*stature) # 定义计算的过程
    return bmi_process # 返回计算值
```

## 完成要求2
def建立计算FAT的函数

```python
# 定义一个计算FAT的的函数
def fat():
    weight = float(input("体重（kg）："))  # 输入所需体重的数据
    upper_arm =float(input("腰围（cm）：")) # 输入所需腰围的数据
    #为计算FAT进行的处理
    a = upper_arm*0.74 # 处理腰围数据
    b = weight*0.082+44.74 # 处理体重数据
    fat_weight = a-b
    # 计算FAT的数据
    return (fat_weight/weight)*100  # 返回计算值

```

## 完成目标3

创建一个母类，其中包含Bmi和Fat这两个函数
```python
# 创建一个母类，其中包含Bmi和Fat这两个函数
# 定义一个类
class Health:
    # 属性
    stature = '1.80m'
    weight = '70kg'
    upper_arm = '80cm'
    # 调用函数
    def Bmi(self):
        q = bmi()
        return q
    def Fat(self):
        w = fat()
        return w
```

## 完成目标4
创建一个子类，用来调用母类的属性

```python
# 创建一个子类，用来调用母类的属性
# 定义一个类
class Happy(Health):
    #调用函数
    def Eat(self):
        bmi1 = self.Bmi()
        print(bmi1)
        if bmi1 > 23.99:  # if函数进行数据的归属
            return"你的BMI大于正常范围(BMI的正常范围在18.5-23.99)"
        elif bmi1 < 18.5:
            return"你的BMI小于正常范围(BMI的正常范围在18.5-23.99)"
        else:
            return"你的BMI处于正常范围内(BMI的正常范围在18.5-23.99)"
    def Fbt(self):
        fat1 = self.Fat()
        print(fat1)
        if fat1>0.18:
            return "你的FAT大于正常范围(FAT的正常范围在0.15-0.18之间)"
        elif fat1 <0.15:
            return "你的FAT小于正常范围(FAT的正常范围在0.15-0.18之间)"
        else:
            return "你的FAT处于正常范围(FAT的正常范围在0.15-0.18之间)"

```
## 完成目标5
调用函数


```python
# 调用函数
y = Happy()
print(y.Eat())
print(y.Fbt())
```

# 结果
## 默认身体属性
> 21.604938271604937
> 你的BMI处于正常范围内(BMI的正常范围在18.5-23.99)
> 12.457142857142856
> 你的FAT大于正常范围(FAT的正常范围在0.15-0.18之间)
## 个人身体属性
> 17.301038062283737
> 你的BMI小于正常范围(BMI的正常范围在18.5-23.99)
> -2.960000000000008
> 你的FAT小于正常范围(FAT的正常范围在0.15-0.18之间)