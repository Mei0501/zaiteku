
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
        self.holding_insurance = {'driver': False, 'life': False}
        self.zaiteku_type = None
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
                self.money -= self.monthly_payment_money

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
        stock_position = [10, 48]
        car_accident_positions = [9, 50]
        get_sick_positions = [27, 37, 52]
        special_position = [49]


    
    
        if self.position in zaiteku_positions:
            self._draw_zaitekucard()
    
        elif self.position in news_positions:
            self._draw_newscard()
    
        elif self.position in news_positions:
            self._draw_postcard()

        elif self.position in insurance_positions:
            self._draw_insurancecard()

        elif self.position in stock_position:
            self._stock()

        elif self.position in special_position:
            self._special_bonus()

        elif self.position in car_accident_positions:
            self._car_accident()

        elif self.position in get_sick_positions:
            self._get_sick()


    
    def _draw_zaitekucard(self):
         if self.has_zaiteku is False:
            self.zaiteku_type = 'investment'
            self.money -= 40000
            self.has_zaiteku = True
            self.monthly_earn_money = 5000

    
    def _draw_newscard(self):
        if self.zaiteku_type == 'investment':
            self.money += 5000

    
    def _draw_postcard(self):
        self.money -= 100

    def _draw_insurancecard(self):
        if self.holding_insurance['driver'] is True and self.holding_insurance['life'] is True :
            pass
        else:
            while True:
                print(self.holding_insurance)
                name = input("choose from 'driver' and 'life' and 'none'")
                if name == 'driver':
                    if self.holding_insurance['driver'] is True:
                        print("you already have driver self.holding_insurancerance")
                    else:
                        self.holding_insurance['driver'] = True
                        break
                elif name == 'life':
                    if self.holding_insurance['life'] is True:
                        print("you already have life self.holding_insurancerance")
                    else:
                        self.holding_insurance['life'] = True
                        break
                elif name == 'none':
                    break
                else:
                    print("input %s is illegal" % name)
            print(self.holding_insurance)

    def _stock(self):
        stock_price = role_dice() *100
        if self.position == 10:
            print(self.money)
            self.money += stock_price
            print(self.money)
            print("株価暴騰")
        else:
            self.money -= stock_price
            print("株価暴落")


    def _car_accident(self):
        if self.holding_insurance['driver'] is False:
            self.money -= 100
        else:
            self.holding_insurance['driver'] = False
            print("自動車保険を回収します")

    def _get_sick(self):
        if self.holding_insurance['life'] is False:
            if self.position == 27:
                self.money -= 80
        else:
            self.holding_insurance['life'] = False
            print("生命保険を回収します")


    def _special_bonus(self):
        self.money += 800
        print("Bonus" + str(self.money))



#サイコロを２個ふった数をかえす
def role_dice():
    dice_eyes1 = random.randint(1, 6)
    dice_eyes2 = random.randint(1, 6)
    dice_sum = dice_eyes1 + dice_eyes2
    return dice_sum

