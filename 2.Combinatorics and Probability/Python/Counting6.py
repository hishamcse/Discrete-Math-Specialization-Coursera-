# Dice Game(slide+code).so,how will the shady person will win always.see the last page of the slide
from random import randint, seed
from datetime import datetime

seed(datetime.now())

dice1 = [1, 1, 6, 6, 8, 8]
dice2 = [2, 2, 4, 4, 9, 9]
dice3 = [3, 3, 5, 5, 7, 7]

num_rounds = 10**5

assert len(dice1) == 6 and len(dice2) == 6 and len(dice3)==6

# for dice 1 & dice 2

# num_dice1_wins = 0
# num_dice2_wins = 0

# for _ in range(num_rounds):
#     dice1_result = dice1[randint(0, 5)]
#     dice2_result = dice2[randint(0, 5)]
#
#     if dice1_result > dice2_result:
#             num_dice1_wins += 1
#     elif dice2_result > dice1_result:
#             num_dice2_wins += 1
#
# if num_dice1_wins > num_dice2_wins:
#         print("The dice {} is better than {}:\nout of {} rounds it won {} times for dice 1 and {} times for dice 2".format(dice1, dice2, num_rounds, num_dice1_wins,num_dice2_wins))
# elif num_dice2_wins > num_dice1_wins:
#         print("The dice {} is better than {}:\nout of {} rounds it won {} times for dice 2 and {} times for dice 1".format(dice2, dice1, num_rounds, num_dice2_wins,num_dice1_wins))
# else:
#         print("A tie")

# for dice 2 and dice 3

# num_dice2_wins = 0
# num_dice3_wins = 0
# for _ in range(num_rounds):
#     dice2_result = dice2[randint(0, 5)]
#     dice3_result = dice3[randint(0, 5)]
#
#     if dice2_result > dice3_result:
#             num_dice2_wins += 1
#     elif dice3_result > dice2_result:
#             num_dice3_wins += 1
#
# if num_dice2_wins > num_dice3_wins:
#         print("The dice {} is better than {}:\nout of {} rounds it won {} times for dice 2 and {} times for dice 3".format(dice2, dice3, num_rounds, num_dice2_wins,num_dice3_wins))
# elif num_dice3_wins > num_dice2_wins:
#         print("The dice {} is better than {}:\nout of {} rounds it won {} times for dice 3 and {} times for dice 2".format(dice3, dice2, num_rounds, num_dice3_wins,num_dice2_wins))
# else:
#         print("A tie")


# for dice 1 and 3


num_dice1_wins = 0
num_dice3_wins = 0

for _ in range(num_rounds):
    dice1_result = dice1[randint(0, 5)]
    dice3_result = dice3[randint(0, 5)]

    if dice1_result > dice3_result:
            num_dice1_wins += 1
    elif dice3_result > dice1_result:
            num_dice3_wins += 1

if num_dice1_wins > num_dice3_wins:
        print("The dice {} is better than {}:\nout of {} rounds it won {} times for dice 1 and {} times for dice 3".format(dice1, dice3, num_rounds, num_dice1_wins,num_dice3_wins))
elif num_dice3_wins > num_dice1_wins:
        print("The dice {} is better than {}:\nout of {} rounds it won {} times for dice 3 and {} times for dice 1".format(dice3, dice1, num_rounds, num_dice3_wins,num_dice1_wins))
else:
        print("A tie")