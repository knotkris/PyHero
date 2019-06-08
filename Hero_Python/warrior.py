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
class Warrior(Hero):
    def __init__(self, name, welcome = True):
        Hero.__init__(self, name, Stats(110, 25, 50, 35))
        if(welcome):
            print("YOU ARE A WARRIOR. WELCOME TO HERO SIM 2019....GOOD LUCK")
        self.enraged_boost = 10
        self.action_list[2] = ("Enrage", self.enrage, False)
    #increases base attack stat and sets status to enraged
    def enrage(self):
        if(self.status == "enraged"):
            print("You are already enraged")
            return False
        self.hero_stats.mana_points -= 5 + self.level
        if(self.hero_stats.mana_points < 0):
            self.hero_stats.mana_points += 5 + self.level
            print("Cannot use this skill, mana is too low")
            return False
        print("{} BECOMES ENRAGED".format(self.name))
        self.status = "enraged"
        self.status_dur = 1
        self.hero_stats.attack_power += self.enraged_boost
        return True
    #does special attack that does damage extra damage and uses mp
    def smash_attack(self, enemy):
        self.hero_stats.mana_points -= 5 + self.level
        if(self.hero_stats.mana_points < 0):
            self.hero_stats.mana_points += 5 + self.level
            print("Cannot use this skill, your mana is too low")
            return False
        try:
            if(self.hero_stats.mana_points < 15):
                print("Cannot use that skill...Not enough mana")
                return False
            print("{} DOES SPECIAL SMASH ATTACK".format(self.name))
            #increase attack by 15 for attack
            #but uses skill points
            self.hero_stats.mana_points -= 15
            enemy.take_damage(self.hero_stats.attack_power + 15)
            return True
        except ValueError: print("Enemy not of correct type class Hero"); return False
    #reverts stats back to previous state
    def calm_down(self):
        print("{} CALMED DOWN".format(self.name))
        self.status = "fine"
        self.hero_stats.attack_power -= self.enraged_boost
        
