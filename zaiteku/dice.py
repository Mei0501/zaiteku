#!/usr/bin/env python

import sys
import random
import player
sys.path.append('/Users/mizo/Project/zaiteku/zaiteku')

def role_dice(is_singl):
    dice_eyes1 = random.randint(1, 6)
    dice_eyes2 = random.randint(1, 6)
    if is_single is False:
        dice_sum = dice_eyes1 + dice_eyes2
    else:
        dice_sum = dice_eyes1
    return dice_sum

def proceed(player):
    player.position = player.position + role_dice()
    if player.position > 58:
        player.position = 0
        player.money += player.monthly_money
        player.money += player.monthly_earn_money
        player.money -= player.monthly_payment_money
