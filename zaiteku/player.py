
#!/usr/bin/env python

import random

#Playerクラスの作成

class Player():

    def __init__(self, name, finish_money, monthly_money):
        self.name = name
        self.finish_money = finish_money
        self.monthly_money = monthly_money 
        self.money = 0
        self.position = 0
        self.is_finished = False
        self.has_zaiteku = False
        self.has_insurance = False
        self.zaiteku_type = None
        self.insurance_type = None
        self.monthly_earn_money = 0
        self.monthly_payment_money = 0


    #procceed関数（サイコロの分だけ進む関数）作成
    def proceed(self):
        if not self.is_finished:
            self.position = self.position + role_dice()
            if self.position > 58:
                self.position = 0 
                self.money += self.monthly_money
                self.money += self.monthly_earn_money

                if self.money >= self.finish_money:
                    self.is_finished = True
            self._get_event()
        else:
             raise RuntimeError("already finished")

    def _get_event(self):
        zaiteku_positions = [2, 5, 11, 16, 19, 23, 31, 34, 38, 46, 55]
        news_positions = [3, 7, 12, 21, 28, 32, 39, 44, 56]
        post_positions =  [4,13,18,26,36,40,47,53]
        insurance_positions = [8, 29, 42, 51]
    
    
        if self.position in zaiteku_positions:
            self._draw_zaitekucard()
    
        elif self.position in news_positions:
            self._draw_newscard()
    
        elif self.position in news_positions:
            self._draw_postcard()

        elif self.position in insurance_positions:
            self._draw_insurancecard()

    
    def _draw_zaitekucard(self):
         print("ziteku")
         if self.has_zaiteku == False:
            self.zaiteku_type = 'investment'
            self.money -= 40000
            self.has_zaiteku = True
            self.monthly_earn_money = 5000

    
    def _draw_newscard(self):
        print("news")
        if self.zaiteku_type == 'investment':
            self.money += 5000

    
    def _draw_postcard(self):
        print("post")
        print(self.money)
        self.money -= 100
        print(self.money)

    def _draw_insurancecard(self):
         print("insurance")
         if self.has_insurance == False:
             self.entry_insurance = "insurance"
             self.has_insurance = True
             self.monthly_payment_money -= 10
        
    

#サイコロを２個ふった数をかえす
def role_dice():
    dice_eyes1 = random.randint(1, 6)
    dice_eyes2 = random.randint(1, 6)
    dice_sum = dice_eyes1 + dice_eyes2
    return dice_sum

