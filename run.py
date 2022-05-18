#!/usr/bin/env python

import os
import sys
from pathlib import Path
sys.path.append('/Users/mei/Project/zaiteku/zaiteku')
from player import Player
from game import Game
from event import get_event

game1 = Game(['taro','jiro'], finish_money= 10000, monthly_money= 4000)
game1.run()
