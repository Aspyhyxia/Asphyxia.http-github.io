a=5
print(a)
x = ['a', 'b', 'c']
y = [1, 2, 3]
dic=dict(zip(x,y))  
print(dic)
# 8.求1+2!+3!+…+20!的和，结果存于变量 s 中。
# Path: test.py
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
s = 0
for i in range(1, 21):
    s += factorial(i)
print(s)
sen="""To me, you are still nothing more than a little boy who is just like a hundred thousand other little boys. 11
And I have no need of you. And you, on your part, have no need of me 23 . To you,"""
#统计sen中逗号出现的个数
# Path: test.py
print(sen.count(','))
#统计sen中单词出现的个数
# Path: test.py
print(len(sen.split()))
#统计sen中空格出现个数
# Path: test.py
print(sen.count(' '))
#统计sen中英文字母个数
# Path: test.py
print(len([i for i in sen if i.isalpha()]))


