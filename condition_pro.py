# 从1到1o所有偶数的平方
alist = []
for i in range(1,11):
    if (i % 2 == 0):
        alist.append( i*i )

print(alist)

# 列表推导式
blist = [i*i for i in range(1,11) if(i % 2) == 0]
print(blist)

# 字典推导式
name = {'a':1, 'b':2}
z_num = {i:0 for i in name}
print(z_num)