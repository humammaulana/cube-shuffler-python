import random

def generateMoveset(arr):
    result = []

    dictionary = {
        0 : "R",
        1 : "L",
        2 : "U",
        3 : "D",
        4 : "F",
        5 : "B",
        6 : "R'",
        7 : "L'",
        8 : "U'",
        9 : "D'",
        10 : "F'",
        11 : "B'",
        12 : "R2",
        13 : "L2",
        14 : "U2",
        15 : "D2",
        16 : "F2",
        17 : "B2"
    }

    for i in range(len(arr)):
        result.append(dictionary[arr[i]])

    return result


shuffle = []

n = int(input("Move: "))

shuffle.append(random.randint(0, 17))

for i in range(1, n):
    same = True
    while same:
        num = random.randint(0, 17)
        if(num%6 != shuffle[i-1]%6):
            same = False
    shuffle.append(num)

moveset = generateMoveset(shuffle)

for i in moveset:
    print(i, end=" ")
