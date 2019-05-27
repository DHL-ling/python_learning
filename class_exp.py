class Player():
    def __init__(self, name, age):
        #self.__name = name # 不会被外部赋值随意改变
        self.name = name
        self.age = age
    def print_role(self):
        print('%s %s' %(self.name, self.age))

fun1 = Player('tome', 10)
fun2 = Player('add', 20)
print(fun1.print_role())
print(fun2.print_role())


# 类的继承
class Monster():
    def __init__(self, hp = 100):
        self.hp = hp
    def run(self):
        print('aaaaa')

class Animal(Monster):
     def __init__(self, hp):
    #     self.hp = hp
        super().__init__(hp) # 父类初始化的某些属性，在子类中不用重复初始化

a1 = Monster(200)
print(a1.run())
a2 = Animal(10)
print(a2.hp)
print(a2.run())


# 自定义with语句
class TestWith():
    def __enter__(self):
        print('run')
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('successfull exit')
        else:
            print('error %s' %exc_tb)

# 异常与类的结合
with TestWith():
    print('test is running')
    raise NameError('testError')