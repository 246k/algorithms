# import datetime
# a = datetime.datetime.now()
# print(10**4)
# b = datetime.datetime.now()
# delta = b - a
# print(delta.total_seconds())
# print((b-a).total_seconds() * 1000)

import time

start_time = time.time()
a = 10**4
print(a)
end_time = time.time()
elapsed_time = (end_time - start_time)
print(elapsed_time * 1000)
