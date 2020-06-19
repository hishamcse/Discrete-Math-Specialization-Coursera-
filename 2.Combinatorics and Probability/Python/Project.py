# task 1
def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    for i in range(6):
        for j in range(6):
            if dice1[i]>dice2[j]:
                dice1_wins+=1
            elif dice1[i]<dice2[j]:
                dice2_wins+=1

    return (dice1_wins, dice2_wins)
# print(count_wins([1,1,6,6,8,8],[2,2,4,4,9,9]))
# print(count_wins([2,2,4,4,9,9],[3,3,5,5,7,7]))

# task 2
def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)

    p=tuple()
    q=tuple()
    p=count_wins(dices[0],dices[1])
    q=count_wins(dices[0],dices[2])
    if p[0]>p[1]>q[1]:
        return 0
    p=count_wins(dices[1],dices[0])
    q=count_wins(dices[1],dices[2])
    if p[0] > p[1] > q[1]:
        return 1
    p = count_wins(dices[2], dices[0])
    q = count_wins(dices[2], dices[1])
    if p[0] > p[1] > q[1]:
        return 2
    return -1
dices=list()
# dices.append([1,1,6,6,8,8])
# dices.append([2,2,4,4,9,9])
# dices.append([3,3,5,5,7,7])

# dices.append([1,1,2,4,5,7])
# dices.append([1,2,2,3,4,7])
# dices.append([1,2,3,4,5,6])
# print(find_the_best_dice(dices))
# t=tuple()
# t=count_wins(dices[0],dices[1])
# print(t[0])

# task 3
from random import randint,seed
from datetime import datetime

seed(datetime.now())

def compute(a,b):
    assert len(a) == 6 and len(b) == 6
    num1 = 0
    num2 = 0
    rounds = 10 * 20000
    for i in range(rounds):
       result1 = a[randint(0, 5)]
       result2 = b[randint(0, 5)]
       if result1 > result2:
         num1 += 1
       else:
         num2 += 1
    return (num1,num2)

def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True
    strategy["first_dice"] = 0
    for i in range(len(dices)):
        c = 0
        for j in range(len(dices)):
            p=tuple()
            p=count_wins(dices[i],dices[j])
            if p[1]>p[0]:
                c=-1
                break
        if c==0:
            strategy["first_dice"] = i
            return strategy

    strategy=dict()
    strategy["choose_first"] = False
    for i in range(len(dices)):
        for j in range(len(dices)):
            p=count_wins(dices[i],dices[j])
            if p[0] > p[1]:
               if i!=(j+1)%len(dices):
                   strategy[i] = (j + 1) % len(dices)
                   break
               else:
                   strategy[i] = (i+1) % len(dices)
                   break
            else:
                continue

    return strategy
# dices.append([4,4,4,4,0,0])
# dices.append([7,7,3,3,3,3])
# dices.append([6,6,2,2,2,2])
# dices.append([5,5,5,1,1,1])
# print(compute_strategy(dices))

# dices.append([1,1,6,6,8,8])
# dices.append([3,3,5,5,7,7])
# dices.append([2,2,4,4,9,9])
# print(compute_strategy(dices))

# dices.append([1,1,4,6,7,8])
# dices.append([2,2,2,6,7,7])
# dices.append([3,3,3,5,5,8])
# print(compute_strategy(dices))

dices=list()
dices.append([4,4,4,4,0,0])
dices.append([3,3,3,3,3,3])
dices.append([6,6,2,2,2,2])
dices.append([5,5,5,1,1,1])
print(compute_strategy(dices))