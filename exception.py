# i = j # 定义错误NameError: name 'j' is not defined

#print()) #语法错误SyntaxError: invalid syntax

#a = '123'
#print(a[4]) #IndexError: string index out of range

#d = {'a':1, 'b':2}
#print(d['c']) #KeyError: 'c'


try:
    year = int(input('input year'))
except Exception as e:
    print('%s' %e)
finally:
    print('success')