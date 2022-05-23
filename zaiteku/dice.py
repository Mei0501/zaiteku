#!/usr/bin/env python

import random
from player import Player

def role_dice(is_single player):
    dice_eyes1 = random.randint(1, 6)
    dice_eyes2 = random.randint(1, 6)
    if is_single is False:
        dice_sum = dice_eyes1 + dice_eyes2
    else:
        dice_sum = dice_eyes1
    return dice_sum
