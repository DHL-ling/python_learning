import time

print(time.time())
print(time.localtime())
print(time.strftime('%Y%m%d'))

import datetime
print(datetime.datetime.now())
newtime = datetime.timedelta(minutes=10)
print(datetime.datetime.now()+newtime)