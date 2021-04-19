import random
import string
import time

from bruteForce import bruteForce
from dynamicProgramming import dynamicProgramming
from manachersAlgorithm import manachersAlgorithm

def randStr(N):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(N*(10**4)))

for x in range(10):
    inputValue = randStr(x)
    print(str(x+1) + ": ")

    print("Brute Force: ")
    print(bruteForce(inputValue))
    for bf in range(10):
        start_time = time.time()
        bruteForce(inputValue)
        end_time = time.time()
        elapsed_time = (end_time - start_time)
        print(elapsed_time * 1000)

    print("Dynamic Programming: ")
    print(dynamicProgramming(inputValue))
    for dp in range(10):
        start_time = time.time()
        dynamicProgramming(inputValue)
        end_time = time.time()
        elapsed_time = (end_time - start_time)
        print(elapsed_time * 1000)

    print("Manacher's Algorithm: ")
    print(manachersAlgorithm(inputValue))
    for ma in range(10):
        start_time = time.time()
        manachersAlgorithm(inputValue)
        end_time = time.time()
        elapsed_time = (end_time - start_time)
        print(elapsed_time * 1000)