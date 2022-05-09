


def _get_event(self):
   zaiteku_positions = [2, 5, 11, 16, 19, 23, 31, 34, 38, 46, 55]
   news_positions = [3, 7, 12, 21, 28, 32, 39, 44, 56]
   post_positions = [4, 13, 18, 26, 36, 40, 47, 53]
   insurance_positions = [8, 29, 42, 51]
   stock_position = [10, 48]
   car_accident_positions = [9, 50]
   get_sick_positions = [27, 37, 52]
   special_position = [49]

   if name.position in zaiteku_positions:
       name._draw_zaitekucard()

   elif name.position in news_positions:
       name._draw_newscard()

   elif name.position in post_positions:
       name._draw_postcard()

   elif name.position in insurance_positions:
       name._draw_insurancecard()

   elif name.position in stock_position:
       name._stock()

   elif name.position in special_position:
       name._special_bonus()

   elif name.position in car_accident_positions:
       name._car_accident()

   elif name.position in get_sick_positions:
       name._get_sick()

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
    if (self.holding_insurance['driver'] is True and
            self.holding_insurance['life'] is True):
        pass
    else:
        while True:
            print(self.holding_insurance)
            name = input("choose from 'driver' and 'life' and 'none'")
            if name == 'driver':
                if self.holding_insurance['driver'] is True:
                    print("you already have driver self.holding_insurance")
                else:
                    self.holding_insurance['driver'] = True
                    break
            elif name == 'life':
                if self.holding_insurance['life'] is True:
                    print("you already have life self.holding_insurance")
                else:
                    self.holding_insurance['life'] = True
                    break
            elif name == 'none':
                break
            else:
                print("input %s is illegal" % name)
        print(self.holding_insurance)

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
    self.money += 800s
