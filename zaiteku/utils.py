#!/usr/bin/env python

import random


def role_dice():
    dice_eyes1 = random.randint(1, 6)
    dice_eyes2 = random.randint(1, 6)
    dice_sum = dice_eyes1 + dice_eyes2
    return dice_sum
