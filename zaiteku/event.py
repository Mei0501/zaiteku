#!/usr/bin/env/ python

import sys
from dice import role_dice
import random

sys.path.append('/Users/mizo/Project/zaiteku/zaiteku')


def get_event(name, players, donation_box):
    player = players[name]
    zaiteku_positions = [2, 5, 11, 16, 19, 23, 31, 34, 38, 46, 55]
    news_positions = [3, 7, 12, 21, 28, 32, 39, 44, 56]
    post_positions = [4, 13, 18, 26, 36, 40, 47, 53]
    insurance_positions = [8, 29, 42, 51]
    stock_position = [10, 48]
    car_accident_positions = [9, 50]
    get_sick_positions = [27, 37, 52]
    special_position = [49]
    encouragement_party_position = [43]
    enter_special_bonus_position = [24]
    exit_special_bonus_position = [110, 111, 112, 113, 114, 115]
    last_special_bonus_position = [49]
    lucky_chance_position = [15, 30]
    incentive_position = [100, 103, 105, 107, 109]
    shopping_position = [102, 106]
    promotion_position = [17]
    donation_position = [22, 33, 101, 104, 108]


    if player.position in zaiteku_positions:
        _draw_zaitekucard(player)

    elif player.position in news_positions:
        _draw_newscard(player)

    elif player.position in post_positions:
        _draw_postcard(player)

    elif player.position in insurance_positions:
        _draw_insurancecard(player)

    elif player.position in stock_position:
        _stock(player)

    elif player.position in special_position:
        _special_bonus(player)

    elif player.position in car_accident_positions:
        _car_accident(player)

    elif player.position in get_sick_positions:
        _get_sick(player)

    elif player.position in encouragement_party_position:
        _encouragement(name, players)

    elif player.position in enter_special_bonus_position:
        _enter_special_bonus(player)

    elif player.position in exit_special_bonus_position:
        _exit_special_bonus(player)

    elif player.position in last_special_bonus_position:
        _last_special_bonus(player)

    elif player.position in lucky_chance_position:
        _lucky_chance(player)

    elif player.position in incentive_position:
        _incentive(player)

    elif player.position in shopping_position:
        _shopping(player)

    elif player.position in promotion_position:
        _promotion(name, players)

    elif player.position in donation_position:
        _add_money_from_player_to_donation_box(player, donation_box)

def _draw_zaitekucard(player):
    if player.has_zaiteku is False:
        player.zaiteku_type = 'investment'
        player.money -= 40000
        player.has_zaiteku = True
        player.monthly_earn_money = 5000

def _draw_newscard(player):
    if player.zaiteku_type == 'investment':
        player.money += 5000

def _draw_postcard(player):
    player.money -= 100

def _draw_insurancecard(player):
    if (player.holding_insurance['driver'] is True and
            player.holding_insurance['life'] is True):
        pass
    else:
        while True:
            print(player.holding_insurance)
            name = input(player.name + "-> choose from 'driver' and 'life' and 'none'>>>")
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


def _stock(player):
    stock_price = role_dice(player.is_advanced_couse) * 100
    if player.position == 10:
        player.money += stock_price
    else:
        player.money -= stock_price

def _car_accident(player):
    if player.holding_insurance['driver'] is False:
        player.money -= 100
    else:
        player.holding_insurance['driver'] = False


def _get_sick(player):
    if player.holding_insurance['life'] is False:
        if player.position == 27:
            player.money -= 80
    else:
        player.holding_insurance['life'] = False


def _special_bonus(player):
    player.money += 800


def _encouragement(name, players):
    for player_name in players:
        if player_name == name:
            players[player_name].money += (len(players)-1) * 100
        else:
            players[player_name].money -= 100


def _enter_special_bonus(player):
    player.money += 400
    adventure_course = input("Do you want to go on an adventure course? yes or no >>>")
    if adventure_course == "yes":
        print("enter the adventure course")
        player.is_advanced_couse is True
    else:
        print("nomal course")


def _exit_special_bonus(player):
    player.position = 49
    player.is_advanced_couse is False
    _last_special_bonus(player)


def _last_special_bonus(player):
    return bet_money
    player.money += 800


def _lucky_chance(player):
    player.position = 30
    bet_money = _get_bet_money()
    player.money -= bet_money
    for _ in range(3):
        dice_eyes3 = random.randint(1, 6)
        dice_eyes4 = random.randint(1, 6)
        if dice_eyes3 == dice_eyes4:
            player.money += bet_money * 10
            print("Win!!")
            break
        else:
            print("Lose")

def _get_bet_money():
    while True:
        try:
            bet_money = int(input("Please enter the bet 100-500."))
        except ValueError:
            print("fail! try again")
            continue
        if (bet_money >= 100 and bet_money <= 500):
            return bet_money

def _incentive(player):
    print("???????????????????????????")
    if player.position == 100:
        player.money += 100
    elif player.position == 103:
        player.money += 500
    elif player.position == 105 or 107:
        player.money += 1000
    elif player.position == 109:
        player.money += 3000

def _shopping(player):
    if player.position == 102:
        player.money -= 200
    elif player.position == 106:
        player.money -= 2000


def _promotion(name, players):
    for player_name in players:
        if player_name == name:
            players[player_name].money += (len(players)-1) * 50
            players[player_name].position = 24
        else:
            players[player_name].money -= 50

def _add_money_from_player_to_donation_box(player, donation_box):
    if player.position == 22 or player.position == 33:
        donation_price = 100
    elif player.position == 101:
        donation_price = 500
    elif player.position == 104 or player.position ==108 :
        donation_price =1000
    player.money -= donation_price
    donation_box.add_money(donation_price)
