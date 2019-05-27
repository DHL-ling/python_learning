# 装饰器的使用
def tips(func):
    def test(a, b):
        print('start:')
        func(a, b)
        print('stop')
    return test


@tips
def add(a, b):
    print(a + b)


print(add(4, 5))
