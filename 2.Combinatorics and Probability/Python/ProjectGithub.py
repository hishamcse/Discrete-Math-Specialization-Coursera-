"""Dice game
"""
import itertools as it


def count_wins(dice1, dice2):
    """List all outcome when throw dices, calculate number
    of outcomes to dice 1 is winner or dice 2 is winner
    :param: dice1, list
    :param: dice2, list
    :return: tuple of int
    """
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    for outcome in it.product(dice1, dice2):
        if outcome[0] > outcome[1]:
            dice1_wins += 1
        elif outcome[1] > outcome[0]:
            dice2_wins += 1

    return (dice1_wins, dice2_wins)


# def find_the_best_dice(dices):
#     """Find best of dice, which have highest probability occur win
#     If exist, return index of dict, else return -1
#     :param: dices, 2d array of int
#     :return: int
#     """
#     assert all(len(dice) == 6 for dice in dices)
#     dice_wins = {}
#     for i in range(len(dices)):
#         dice_wins[i] = []
#
#     for i in range(len(dices)-1):
#         for j in range(i+1, len(dices)):
#             dice_i_wins, dice_j_wins = count_wins(dices[i], dices[j])
#             if dice_i_wins > dice_j_wins:
#                 dice_wins[i].append(j)
#             elif dice_j_wins > dice_i_wins:
#                 dice_wins[j].append(i)
#
#     for i in range(len(dices)):
#         if i not in dice_wins:
#             continue
#         for loser in dice_wins[i]:
#             if loser not in dice_wins:
#                 continue
#             if i in dice_wins[loser]:
#                 return -1
#             dice_wins[i] += dice_wins[loser]
#             dice_wins.pop(loser)
#
#     return list(dice_wins.keys())[0]

def find_the_best_dice(dices):
    """Find best of dice, which have highest probability occur win
    If exist, return index of dict, else return -1
    :param: dices, 2d array of int
    :return: int
    """
    assert all(len(dice) == 6 for dice in dices)
    dice_wins = {}
    for i in range(len(dices)):
        dice_wins[i] = []

    for i in range(len(dices)-1):
        for j in range(i+1, len(dices)):
            dice_i_wins, dice_j_wins = count_wins(dices[i], dices[j])
            if dice_i_wins > dice_j_wins:
                dice_wins[i].append(j)
            elif dice_j_wins > dice_i_wins:
                dice_wins[j].append(i)

    for i in range(len(dices)):
        if i not in dice_wins:
            continue
        for loser in dice_wins[i]:
            if loser not in dice_wins:
                continue
            if i in dice_wins[loser]:
                return -1
            dice_wins[i] += dice_wins[loser]
            dice_wins.pop(loser)

    return list(dice_wins.keys())[0]


def compute_strategy(dices):
    """Compute strategy
    If best dice exist, this return choose_first = True and
    first_dice is index of best dice
    Else, it return choose_first is False and strategy for
    choose dice after opponient choose
    :param: dices, 2d array of int
    :param: dict
    """
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True
    strategy["first_dice"] = 0

    result = find_the_best_dice(dices)
    if result != -1:
        strategy["first_dice"] = result
    else:
        strategy = dict()
        strategy["choose_first"] = False
        for i in range(len(dices)):
            for j in range(len(dices)):
                if i != j:
                    dice_i_wins, dice_j_wins = count_wins(dices[i], dices[j])
                    if dice_j_wins > dice_i_wins:
                        break
            strategy[i] = j
    return strategy


dices = list()
dices.append([4, 4, 4, 4, 0, 0])
dices.append([7, 7, 3, 3, 3, 3])
dices.append([6, 6, 2, 2, 2, 2])
dices.append([5, 5, 5, 1, 1, 1])
print(compute_strategy(dices))

# dices.append([1,1,6,6,8,8])
# dices.append([3,3,5,5,7,7])
# dices.append([2,2,4,4,9,9])
# print(compute_strategy(dices))

# dices.append([1,1,4,6,7,8])
# dices.append([2,2,2,6,7,7])
# dices.append([3,3,3,5,5,8])
# print(compute_strategy(dices))

# dices=list()
# dices.append([4,4,4,4,0,0])
# dices.append([3,3,3,3,3,3])
# dices.append([6,6,2,2,2,2])
# dices.append([5,5,5,1,1,1])
# print(compute_strategy(dices))