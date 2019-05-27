# 闭包

# 闭包：外部变量被内部变量使用
def sum(a): # 外部函数
    def add(b): # 内部函数
        return a+b

    return add # 引用add的函数

# add 函数名称或函数的引用
# add() 函数的调用
num = sum(2)
print(num(4))

# 计数器的实现
def counter(fist=0):
    cnt = [fist]
    def add_one():
        cnt[0] += 1
        return cnt[0]
    return add_one

num1 = counter(8)
print(num1())


##  下面两个函数相同
def a_line(a,b):
    def arg_y(x):
        return a*x+b
    return  arg_y

def a_line2(a,b):
    return  lambda x: a*x+b
##