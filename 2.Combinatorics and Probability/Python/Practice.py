# counting 4
# from random import randint,seed
# from datetime import datetime
#
# seed(datetime.now())
#
# s=0
# for i in range(10**5):
#     s+=randint(1,6)
# print(s/(10**5))

# counting 5
from random import randint,seed
from datetime import datetime

seed(datetime.now())
a=[2,2,2,2,3,3]
b=[1,1,1,1,6,6]
def compute(a,b):
    assert len(a) == 6 and len(b) == 6
    num1 = 0
    num2 = 0
    rounds = 10 ** 5
    for i in range(rounds):
       result1 = a[randint(0, 5)]
       result2 = b[randint(0, 5)]
       if result1 > result2:
         num1 += 1
       else:
         num2 += 1
    return (num1,num2)

# if num1>num2:
#     print("{} wins more than {} in {} rounds {} times".format(a,b,rounds,num1))
# else:
#     print("{} wins more than {} in {} rounds {} times".format(b,a,rounds,num2))
print(compute(a,b))


# def count_wins(dice1, dice2):
#     assert len(dice1) == 6 and len(dice2) == 6
#     dice1_wins, dice2_wins = 0, 0
#
#     for i in range(6):
#         for j in range(6):
#             if dice1[i] > dice2[j]:
#                 dice1_wins += 1
#             elif dice1[i] < dice2[j]:
#                 dice2_wins += 1
#
#     return (dice1_wins, dice2_wins)
#
#
# def compute_strategy(dices):
#     assert all(len(dice) == 6 for dice in dices)
#
#     strategy = dict()
#     strategy["choose_first"] = True
#     strategy["first_dice"] = 0
#     for i in range(len(dices)):
#         c = 0
#         for j in range(len(dices)):
#             p = tuple()
#             p = count_wins(dices[i], dices[j])
#             if p[1] > p[0]:
#                 c = -1
#                 break
#         if c == 0:
#             strategy["first_dice"] = i
#             return strategy
#
#     strategy = dict()
#     strategy["choose_first"] = False
#     for i in range(len(dices)):
#         for j in range(len(dices)):
#             p = count_wins(dices[i], dices[j])
#             if p[0] > p[1]:
#                 if i != (j + 1) % len(dices):
#                     strategy[i] = (j + 1) % len(dices)
#                     break
#                 else:
#                     strategy[i] = (i + 1) % len(dices)
#                     break
#             else:
#                 continue
#
#     return strategy

