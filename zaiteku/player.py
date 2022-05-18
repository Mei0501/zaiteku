#!/usr/bin/env python

import random
from utils import role_dice
# Playerクラスの作成


class Player():

    def __init__(self, name, monthly_money=1000):
        self.name = name
        self.money = 0
        self.position = 0
        self.has_zaiteku = False
        self.holding_insurance = {'driver': False, 'life': False}
        self.zaiteku_type = None
        self.monthly_money = monthly_money
        self.monthly_earn_money = 0
        self.monthly_payment_money = 0

    # procceed関数（サイコロの分だけ進む関数）作成
    def proceed(self):
        self.position = self.position + role_dice()
        if self.position > 58:
            self.position = 0
            self.money += self.monthly_money
            self.money += self.monthly_earn_money
            self.money -= self.monthly_payment_money
