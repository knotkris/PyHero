# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:21:12 2019

@author: Knot
"""
from heroes_magic import Hero, Stats
from random import randint
"""
class Warrior
child class of Hero
attributes
enraged_boost - used to increase user attack when enrage is used
"""
class Theif(Hero):
    def __init__(self, name, welcome = True):
        Hero.__init__(self, name, Stats(40, 85, 70, 25))
        if(welcome):
            print("YOU ARE A THEIF. WELCOME TO HERO SIM 2019....GOOD LUCK")
        self.action_list[2] = ("Sneak Attack", self.sneak_attack, True)
    #increases base attack stat and sets status to enraged
    def sneak_attack(self, enemy):
        self.hero_stats.mana_points -= 5 + self.level
        if(self.hero_stats.mana_points < 0):
            self.hero_stats.mana_points += 5 + self.level
            print("Cannot use this skill, mana is too low")
            return False
        print("{} ATTEMPTS A SNEAK ATTACK".format(self.name))
        #higher chance if the user has a much higher level or a much lower level
        success = randint(1, 100) > (abs(self.level - enemy.level) * 10) % 100
        if(success):
            print("{}'s attack succeeded".format(self.name))
            enemy.take_damage(self.hero_stats.attack_power * 2.25)
        else:
            print("{}'s attack failed".format(self.name))
        return True
        
