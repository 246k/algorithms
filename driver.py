import random
import string
import time

from brute-force import brute-force
from dynamicProgramming import dynamicProgramming
from manachersAlgorithm import manachersAlgorithm

def randStr(N):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(N*(10**4)))

for x in range(10):
    inputValue = randStr(x)
    print(str(x+1) + ": ")

    for j in range(10):
        start_time = time.time()
        print(manachersAlgorithm(inputValue))
        end_time = time.time()
        elapsed_time = (end_time - start_time)
        print(elapsed_time * 1000)