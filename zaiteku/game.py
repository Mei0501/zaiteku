#!/usr/bin/env python

import sys
from player import Player
from event import get_event
from dice import role_dice
sys.path.append('/Users/mizo/Project/zaiteku/zaiteku')

# Player(name)でインスタンス化マネーなどはデフォルト値


class Game():

    def __init__(self, player_names, finish_money=10000, monthly_money=1000):
        self.players = {name: Player(name, monthly_money=monthly_money)
                        for name in player_names}
        self.finish_money = finish_money
        self.monthly_money = monthly_money
        #self.proceed = proceed

    def run(self):
        is_finished = False
        while not is_finished:
            for name in self.players:
                self.players[name].proceed(players[name])
                event.get_event(name, self.players)
                #exent.いらん？
                is_finished = self.check_is_finished(name=name)
                if is_finished is True:
                    break
                

    def check_is_finished(self, name):
        if self.players[name].money >= self.finish_money:
            print(name + " won the game")
            return True
        return False

    def _proceed(self, player):
        player.position = player.position + role_dice(player.is_advanced_couse)
        if player.position > 58:
            player.position = 0
            player.money += player.monthly_money
            player.money += player.monthly_earn_money
            player.money -= player.monthly_payment_money
        print("puro")
