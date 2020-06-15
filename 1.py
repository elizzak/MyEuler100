

# def multiplesof3(number):
#     total = 0
#     nexter = 0
#     i = 1
#     while nexter < number:
#         nexter = i*3
#         total = total + nexter
#         i = i +1
#     return total
# for i in range(1, number):
#     next = i*3
#     total = total + next
# return total


# def multiplesofN(number , N):
#     total = 0
#     nexter = 0
#     i = 1
#     while nexter < number:
#         print(nexter)
#         nexter = i * N
#         if nexter >= number:
#             break
#         print(nexter)
#         total = total + nexter
#         i = i + 1
#     return total
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
