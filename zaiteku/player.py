#!/usr/bin/env python

from dice import role_dice
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
        self.is_advanced_couse = False

