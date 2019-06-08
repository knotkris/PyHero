# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:22:24 2019

@author: Knot
"""
from heroes_magic import Hero, Stats
from magics import Heal
from random import randint

'''
class Knight
child class of Hero
attributes
armor_boost = when user is defense mode
heal_spell = class Heal, allows knight class to use heal spell
familia = holds the knight's family name, its an honor thing ya know
'''
class Knight(Hero):
    armor_boost = 15
    heal_spell = Heal()
    def __init__(self, name, familia, welcome = True):
        #Ask for user's name
        if(welcome):
            print("YOU ARE A KNIGHT. WELCOME TO HERO SIM 2019....GOOD LUCK")
        Hero.__init__(self, name, Stats(130, 50, 25, 40 + self.armor_boost))
        self.familia = familia
        self.action_list[2] = ("Sheild Charge", self.sheild_charge, True)
        self.action_list[5] = ("Defend", self.raise_shield, False)
        self.action_list[6] = ("Heal", self.heal, False)
    #increases defense, effect lasts one turn
    def raise_shield(self):
        if(self.status == "defending"):
            print("Cannot defend anymore")
            return False
        print(self.name, " DEFENDED")
        self.status = "defending"
        self.status_dur = 1
        self.hero_stats.defense += 10
        #increase defense for that turn
        return True
    #resets stat raise of raise_shield
    def lower_sheild(self):
        self.status = "fine"
        try:
            print("{} lowers their sheild".format(self.name))
            if(self.hero_stats.defense > 10):
                self.hero_stats.defense -= 10
                self.status = "fine"
            else:
                self.hero_stats.defense = 0
                print("Defense cannot go any lower")
        except ValueError: print("Defense or hero_stats have been changed to be of incorrect type")
    #special attack that does damage based on Defense stat
    #has a high chance of missing
    def sheild_charge(self, enemy):
        self.hero_stats.mana_points -= 10 + self.level
        if(self.hero_stats.mana_points < 0):
            self.hero_stats.mana_points += 10 + self.level
            print("Cannot use this skill, mana is too low")
            return False
        try:
            print("DAMAGE BASED ON DEFENSE")
            #determine if it hit
            hit_chance = randint(1, 20)#has a 5 in 20 chance of missing or 25%
            hit = hit_chance > 5 
            if(hit):
                print("HIT ENEMY")
                enemy.take_damage(self.hero_stats.defense)
            else:
                print("{} missed".format(self.name))  
            return True
        except ValueError: print("Enemy not of correct type class Hero"); return False
    #activates the heal spell class
    def heal(self):
        self.hero_stats.mana_points -= 15
        if(self.hero_stats.mana_points < 0):
            self.hero_stats.mana_points += 15
            print("Cannot use this skill, mana is too low")
            return False
        try:
            print("HEAL SELF")
            self.heal_spell.heal_user(self)
            return True
        except ValueError: print("heal_spell was not of correct type class Heal"); return False
