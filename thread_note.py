# 多线程
import threading
import time
from threading import current_thread


# def myTread(arg1, arg2):
#     print(current_thread().getName(),'start') # 线程的名称+注释
#     print('%s %s' %(arg1, arg2))
#     time.sleep(1)
#     print(current_thread().getName(), 'stop')
#
# for i in range(1,6,1):
#     t1 = threading.Thread(target=myTread, args=(i, i+1))
#     t1.start()
#
# print(current_thread().getName(), 'end')

# 控制主线程先结束，使用join
class Mainthread(threading.Thread):
    def run(self):
        print(current_thread().getName(), 'start')  # 线程的名称+注释
        print('run')
        print(current_thread().getName(), 'stop')

t1 = Mainthread()
t1.start()
t1.join() # 这个线程先执行，直到这线程结束后，再执行下面的线程
print(current_thread().getName(),'end')

