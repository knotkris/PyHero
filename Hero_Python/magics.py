# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:20:21 2019

@author: Knot
"""
from heroes_magic import Magic
from random import randint
"""
class Heal
child class of Magic
Used by Knight and Sorceress Class to heal hp
initializes using the parent class
init_power refers to the initial amount that
user heals for without the addition of their
mp stat
costs 15 mp and lasts one turn
"""
class Heal(Magic):
    init_power = 15
    def __init__(self):
        Magic.__init__(self, 15, "USER HEALS HITPOINTS", 1)
    #Heals user based on init_power and the user's mp amount
    def heal_user(self, user):
        try:
            amount_healed = self.determine_amount(user.hero_stats.mana_points, user.level)
            print("{} healed for {} hp".format(user.name, amount_healed))
            user.hero_stats.hit_points += amount_healed 
        except ValueError: print("Incorrect type for user; not class or child class of Hero")

    #determines the amount a user heals for given their mana and level
    def determine_amount(self, user_mana, user_level):
        try:
            amt = user_mana / user_level
            if(amt < 0):
                print("Values were less than zero, heal for zero points")
                return 0
            else:
                return self.init_power + amt
        except ValueError: print("Incorrect type passed for level or mana; should be number"); return 0
"""
class Sleep
child class of Magic
Initializes the parent class
used by Sorceress class to determine
if a user is put to sleep or not
lasts 2 turns and costs 50 mp
"""
class Sleep(Magic):
    def __init__(self):
        Magic.__init__(self, 50, "USER ATTEMPTS TO PUT ENEMY TO SLEEP", 2)
    #check if spell worked
    #based on mp of user and mp of enemy
    def put_to_sleep(self, user, enemy):  
        print("{} tries to put {} to sleep".format(user.name, enemy.name))
        try:
            sleep_success = randint(0, 1000) < (user.hero_stats.mana_points / enemy.hero_stats.mana_points) * user.hero_stats.mana_points
            if(enemy.status == "sleep"):
                print("Enemy is already asleep")
                sleep_success = False
            if(sleep_success):
                enemy.status = "sleep"
                enemy.status_dur = self.duration
                print("ENEMY IS NOW ASLEEP")
            else:
                print("FAILED TO PUT ENEMY TO SLEEP")
        except ValueError: print("user or enemy not of correct type class Hero")
    #used to determine the chance of the enemy
    #being put to sleep
    def determine_chance(user_mp, enemy_mp):
        try:
            if(user_mp < 0 or enemy_mp < 0):
                print("Negative value entered as mp amount returning zero")
                return 0
            else:
                return (user_mp / enemy_mp)
        except ValueError: print("mp values should be type number; returning zero"); return 0

"""
class Invisibility
child class of the Magic class
used to turn the user invisible
which makes them invulnerable to 
damage unless invisibility fails
costs 75 mp and lasts 2 turns
"""    
class Invisiblity(Magic):
    def __init__(self):
        Magic.__init__(self, 75, "USER TURNS INVISIBLE", 2)
    #sets the user's status as invisible and sets status duration to set amount
    def turn_invisible(self, user):
        print("{} tries to turn invisible".format(user.name))
        try:
            if(user.status == "invisible"):
                print("{} is already invisible".format(user.name))
            else:
                print("{} is now invisible".format(user.name))
                user.status = "invisible"
                user.status_dur = self.duration
        except ValueError: print("user is not correct type class Hero")
    #chance method used to determine if a user's invisibility fails
    def check_if_failed(self, enemy, user):
        try:
            #chance based on lvl difference that enemy sees you which ends invisibility status
            failed = randint(0, 100) < 20 + (enemy.level - user.level)
            if(failed):
                print("{} IS NO LONGER INVISIBLE".format(user.name))
                user.status = "fine"
                user.status_dur = 0
                return True #invisibility failed
            return False
        except ValueError: print("User or enemy was of incorrect type"); return False
    #determining chance factor where having a higher level
    #than the enemy increases the chance of not being
    #found 
    def determine_chance(user_lvl, enemy_lvl):
        try:
            if(user_lvl < 0 or enemy_lvl < 0):
                print("level values are less than zero"); return False
                
            return randint(0, 1000) < (enemy_lvl/user_lvl * 100)
        except ValueError: print("level values not of type number"); return False