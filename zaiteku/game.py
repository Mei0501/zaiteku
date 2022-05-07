import sys
from player import Player
sys.path.append('/Users/mizo/Project/zaiteku/zaiteku')

# Player(name)でインスタンス化マネーなどはデフォルト値


class Game():

    def __init__(self, player_names, finish_money=10000, monthly_money=1000):
        self.players = {name: Player(name, monthly_money=monthly_money)
                        for name in player_names}
        self.finish_money = finish_money
        self.monthly_money = monthly_money

    def run(self):
        is_finished = False
        while not is_finished:
            for name in self.players:
                self.players[name].proceed()
                if self.players[name].position == 0:
                    self.players[name].money += self.monthly_money
                is_finished = self.check_is_finished(name=name)

    def check_is_finished(self, name):
        if self.players[name].money >= self.finish_money:
            print(name + " won the game")
            return True
        return False
