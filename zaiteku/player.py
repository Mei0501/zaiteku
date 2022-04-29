#!/usr/bin/env python

import random

#Playerクラスの作成

class Player():

    def __init__(self, name):
        self.name = name
        self.money = 0
        self.position = 0
        self.is_finished = False

    #procceed関数（サイコロの分だけ進む関数）作成
    def proceed(self):
        if not self.is_finished:
            self.position = self.position + role_dice()
            if self.position > 30:
                self.position -= 0 
                self.money = self.money + 1000

                if self.money >= 10000:
                    self.is_finished = True

        else:
             raise RuntimeError("already finished")

    def _event(self):
        print("hoge")

#サイコロを２個ふった数をかえす
def role_dice():
    dice_eyes1 = random.randint(1, 6)
    dice_eyes2 = random.randint(1, 6)
    dice_sum = dice_eyes1 + dice_eyes2
    return dice_sum

