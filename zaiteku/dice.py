#!/usr/bin/env python

import sys
import random
sys.path.append('/Users/mizo/Project/zaiteku/zaiteku')

def role_dice(is_single):
    dice_eyes1 = random.randint(1, 6)
    dice_eyes2 = random.randint(1, 6)
    if is_single is False:
        dice_sum = dice_eyes1 + dice_eyes2
    else:
        dice_sum = dice_eyes1
    return dice_sum

