import sys
from player import Player
sys.path.append('/Users/mizo/Project/zaiteku/zaiteku')

#Player(name)でインスタンス化マネーなどはデフォルト値
class Game():
    def __init__(self, player_names, finish_money=10000, monthly_money=1000):
        self.players = {name: Player(name) for name in player_names}
        self.finish_money = finish_money
        self.monthly_money = monthly_money

    def run(self):
        is_continue = True
        while is_continue:
            for name in self.players:
                self.players[name].proceed()
                if self.players[name].position == 0:
                    self.players[name].money += self.monthly_money
                    if self.players[name].money >= self.finish_money:
                    #if self.players[name].is_finished is True:
                        print(name + " won the game")
                        is_continue = False
                        break

    def check_finished(self):
        pass
