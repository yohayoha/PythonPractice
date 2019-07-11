import sys
'''
list=[1,2,3,4]
it=iter(list)#创建迭代器对象 it
'''
'''
print(next(it)) #输出迭代器的下一个元素

print(next(it))
'''
'''
#使用常规for语句遍历迭代器

for i in it:
    print(i,end='\t')     #print()完整形式：print(x,end='\n').此处是打印不换行

print('**********************',end=('\n'))
'''
'''
#使用next()函数遍历
import sys
list=[1,2,3,4]
it=iter(list)

while True:
    try:
        print(next(it),end="\t")
    except StopIteration:
        sys.exit()
'''
'''
#创建一个迭代器
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    x = self.a
    self.a += 1
    return x
 
myclass = MyNumbers()
myiter = iter(myclass)
 
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(MyNumbers)
'''
'''
#Stoplteration一场用于标识迭代的完成，防止出现无限循环
class MyNumbers:
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
           
myclass=MyNumbers()
myiter=iter(myclass)

for x in myiter:
    print(x)
'''

#调用一个生成器函数，返回的是一个迭代器对象

def fibonacci(m):           #生成函数-斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if(counter > m):
            return
        yield a         #函数暂停并保存当前所有的运行消息，返回yield的值，并在下一次执行next()方法时从当前位置继续运行
        a, b = b, a+b
        counter += 1


f = fibonacci(10)           #f 是一个迭代器，由生成器返回生成
while True:
    try:
        print(next(f), end='\t')
    except StopIteration:
        sys.exit()
