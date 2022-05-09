#!/usr/bin/env/ python

import sys
from player import Player
sys.path.append('/Users/mizo/Project/zaiteku/zaiteku')

def _get_event(name, players):
    player = players[name]
    zaiteku_positions = [2, 5, 11, 16, 19, 23, 31, 34, 38, 46, 55]
    news_positions = [3, 7, 12, 21, 28, 32, 39, 44, 56]
    post_positions = [4, 13, 18, 26, 36, 40, 47, 53]
    insurance_positions = [8, 29, 42, 51]
    stock_position = [10, 48]
    car_accident_positions = [9, 50]
    get_sick_positions = [27, 37, 52]
    special_position = [49]

    if player.position in zaiteku_positions:
        player._draw_zaitekucard()
 
    elif player.position in news_positions:
        player._draw_newscard()
 
    elif player.position in post_positions:
        player._draw_postcard()
 
    elif player.position in insurance_positions:
        player._draw_insurancecard()
 
    elif player.position in stock_position:
        player._stock()
 
    elif player.position in special_position:
        player._special_bonus()
 
    elif player.position in car_accident_positions:
        player._car_accident()
 
    elif player.position in get_sick_positions:
        player._get_sick()
 
    def _draw_zaitekucard():
        if player.has_zaiteku is False:
            player.zaiteku_type = 'investment'
            player.money -= 40000
            player.has_zaiteku = True
            player.monthly_earn_money = 5000
    
    def _draw_newscard():
        if player.zaiteku_type == 'investment':
            player.money += 5000
    
    def _draw_postcard():
        player.money -= 100
    
    def _draw_insurancecard():
        if (player.holding_insurance['driver'] is True and
                player.holding_insurance['life'] is True):
            pass
        else:
            while True:
                print(player.holding_insurance)
                name = input("choose from 'driver' and 'life' and 'none'")
                if name == 'driver':
                    if player.holding_insurance['driver'] is True:
                        print("you already have driver player.holding_insurance")
                    else:
                        player.holding_insurance['driver'] = True
                        break
                elif name == 'life':
                    if player.holding_insurance['life'] is True:
                        print("you already have life player.holding_insurance")
                    else:
                        player.holding_insurance['life'] = True
                        break
                elif name == 'none':
                    break
                else:
                    print("input %s is illegal" % name)
            print(player.holding_insurance)
    
    def _stock(self):
        stock_price = role_dice() * 100
        if self.position == 10:
            self.money += stock_price
        else:
            self.money -= stock_price
    
    def _car_accident(self):
        if self.holding_insurance['driver'] is False:
            self.money -= 100
        else:
            self.holding_insurance['driver'] = False
    
    def _get_sick(self):
        if self.holding_insurance['life'] is False:
            if self.position == 27:
                self.money -= 80
        else:
            self.holding_insurance['life'] = False
    
    def _special_bonus(self):
        self.money += 800
