
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
            _get_event()
        else:
             raise RuntimeError("already finished")

    def _get_event(self):
        zaiteku_positions = [2, 5, 11, 16, 19, 23, 31, 34, 38, 46, 55]
        news_positions = [3, 7, 12, 21, 28, 32, 39, 44, 56]
        post_positions =  [4,13,18,26,36,40,47,53]
    
    
        if self.position in zaiteku_positions:
            self._draw_zaitekucard()
    
        elif self.position in news_positions:
            self._draw_newscard()
    
        else: #position in news_positions:
            self._draw_postcard()
    
    def _draw_zaitekucard():
        print("ziteku")
    
    def _draw_newscard():
            print("news")
    
    def _draw_postcard():
            print("post")
    
    
#get_event(3)

    def _event(self):
        print("hoge")

#サイコロを２個ふった数をかえす
def role_dice():
    dice_eyes1 = random.randint(1, 6)
    dice_eyes2 = random.randint(1, 6)
    dice_sum = dice_eyes1 + dice_eyes2
    return dice_sum

