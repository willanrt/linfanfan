#!/usr/bin/env python
# coding: utf-8

# In[5]:


for y in range(1860,1921):
    if y%4==0 and y%100!=0:
        print(y)
    elif y%400==0:
        print(y)
    else:
        pass


# In[ ]:


sum1 =0
sum2 =0
for i in range(1,101):
    if i%2==0:
        sum2


# In[9]:


for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j:2d}",end='  ')
    print() #(end='\n')


# In[10]:


for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j:2d}  ",end='')
    print() #(end='\n')


# In[15]:


x = 1 #x代表行
while x<=9:
    y = 1 #y代表列
    while y<=x:
        print(f"{x}*{y}={x*y:2}",end='  ')
        y += 1
    print()#打印换行符号
    x +=1


# In[17]:


for i in range(1,10):
    for j in range(1,10):
        if i>=j:
            print(f"{i}*{j}={i*j:2}",end='  ')
        else:
            pass
    print()


# In[18]:


for i in range(1,10):
    for j in range(1,10):
        if i<=j:
            print(f"{i}*{j}={i*j:2}",end='  ')
        else:
            pass
    print()


# In[19]:


for i in range(1,10):
    for j in range(1,10):
        if i<=j:
            print(f"{i}*{j}={i*j:2}",end='  ')
        else:
            print('        ', end='')
    print()


# In[22]:


for i in range(1,10):
    for j in range(1,10):
        if i+j>=10:
            print(f"{i}*{j}={i*j:2}",end='  ')
        else:
            print('        ', end='')
    print()


# In[25]:


#循环提前终止

for i in range(1,10):
    print(i)
    break
    print(i)
    


# In[26]:


for i in range(1,10):
    print(i)
    continue
    print(i)
    


# In[27]:


for i in range(1,10):
    if i%3==0:
        break
    print(i)
    


# In[28]:


for i in range(1,10):
    if i%3==0:
        continue
    print(i)
    


# In[ ]:


while True: 
    s = input('input string: ')
    if s =='exit':
        break
    print(s,s)


# In[ ]:


while True: 
   s = input('input string: ')
   if s!='exit':
       print(s,s)
   else:
       break


# from random import randrange
# key = randrange(0,1000)
# while True:
#     x = int(input('gess a number 0--1000:'))
#     if x == key:
#         print(f'Corect!  key={key}')
#         break
#     elif x < key:
#         print('too small')
#     else:
#         print('too big')

# In[7]:


#n! = 1*2...*n
#10! = ?
prod = 1
for i in range(2,11):
    prod *= i
print(f"10! = {prod}")


# In[8]:


prod = 1
j = 10
while j>1:
    prod *= j
    j -=1
print("10! = %d" % prod)


# In[10]:


total = 0
for n in range(1,101):
    total += 1/(2*n-1)
print(f"total = {total:.2f}")


# In[11]:


total = 0
sign = 1
for n in range(1,101):
    total += sign / n
    sign = -sign
print(f"{total:.3f}")


# In[12]:


total = 0
A = 2**1
for n in range(1,11):
    total += n**2 / A
    A *= 2
print(f"{total:.2f}")


# In[ ]:




