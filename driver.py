import random
import string
import time

from bruteForce import bruteForce
from dynamicProgramming import dynamicProgramming
from manachersAlgorithm import manachersAlgorithm

def randStr(N):
    chars = string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(N*(10**3)))


for x in range(1, 11):
    inputValue = randStr(x)
    print("Test #" + str(x) + ": ")
    print("String inputValue is: " + inputValue)

    bfAvg = float(0)
    print("Brute Force output: " + bruteForce(inputValue))
    for bf in range(10):
        start_time = time.time()
        bruteForce(inputValue)
        end_time = time.time()
        elapsed_time = (end_time - start_time)
        bfAvg += (elapsed_time * 1000)
        print(elapsed_time * 1000)

    dpAvg = float(0)
    print("Dynamic Programming output: " + dynamicProgramming(inputValue))
    for dp in range(10):
        start_time = time.time()
        dynamicProgramming(inputValue)
        end_time = time.time()
        elapsed_time = (end_time - start_time)
        dpAvg += (elapsed_time * 1000)
        print(elapsed_time * 1000)

    maAvg = float(0)
    print("Manacher's Algorithm output: " + manachersAlgorithm(inputValue))
    for ma in range(10):
        start_time = time.time()
        manachersAlgorithm(inputValue)
        end_time = time.time()
        elapsed_time = (end_time - start_time)
        maAvg += (elapsed_time * 1000)
        print(elapsed_time * 1000)

    print( "Brute Force Average RT for run " + str(x) + ": " + str(bfAvg/10) )
    print( "Dynamic Programming Average RT for run " + str(x) + ": " + str(dpAvg/10) )
    print( "Manacher's Algorithm Average RT for run " + str(x) + ": " + str(maAvg/10) )

