import os
import sys
from pathlib import Path
sys.path.append('/Users/mizo/Project/zaiteku/zaiteku')
from player import Player

class Game():
    def __init__(self, player_names, finish_money, monthly_money):
        self.players =  {name: Player(name) for name in player_names}
        self.finish_money = finish_money
        self.monthly_money = monthly_money
        
    def run(self):
        is_continue = True
        while is_continue:
            for name in self.players:
                #players = players['taro']
                self.players[name].proceed()
                if self.players[name].is_finished is True:
                    print(name + " won the game")
                    is_continue = False
                    break

