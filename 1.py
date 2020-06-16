
from typing import List, Any


def multiplesofN(number , N):
    multiples = [] #set()
    m = 0
    i = 1
    while m < number:
        print(m)
        m = i * N
        if m >= number:
            break
        multiples.append(m)
        i = i + 1
    return multiples

def multiplesOf3and5(number):
    threes = multiplesofN(number, 3)
    fives = multiplesofN(number, 5)
    union = list(set(threes) | set(fives))
    return sum(union)


print(multiplesOf3and5(1000))
