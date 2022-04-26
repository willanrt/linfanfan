import os
import re
path = 'C:/Users/f1241/Desktop/python/python进阶/第十四章操作数据库第六次作业/附加题'
x = os.listdir(path)
a = 0
rule = r"_(\d{1,2})|(\d{2})-"
name = re.findall(rule, str(x))
#print(name)
rule_0 = r"\d\d?"
new_name = re.findall(rule_0, str(name))
#print(new_name)
os.chdir(path)
for i in x:
    oldDir = x[a]
    newDir = new_name[a] + oldDir[oldDir.index('.'):]  # 新文件
    os.rename(oldDir, newDir)
    print(oldDir, newDir)
    a += 1
