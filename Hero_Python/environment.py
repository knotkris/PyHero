# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:24:03 2019

@author: Knot
"""

from random import randint
from sorceress import Sorceress
from knight import Knight
from warrior import Warrior
from theif import Theif
import time
'''
Class Environment
Parent Class for effecting the overall
player state and determine the enemies 
that the player will encounter as well 
as the difficulty of the environment
'''
class Environment:
    def __init__(self, name, enemy_names = [], encounter_rate = 0.5, level_inc = 2):
        self.name = name
        self.enemy_names = enemy_names
        self.encounter_rate = encounter_rate
        self.hero = None
        self.boss = None
        self.boss_defeated = False
        self.level_inc = level_inc
    def read_enemy_file(self, file_name):
        try:
            with open(self._file) as enemy_file:
                return [{"name" : enemy_layout.split(',')[0].split(':')[1].strip(), 
                            "type" : enemy_layout.split(',')[1].split(':')[1].strip()} 
                                for enemy_layout in enemy_file.read().split(';')]
        except Exception as e: 
            print("There was an error: ", str(e))
            return []
    def enter_environment(self, hero):
        self.hero = hero
        print("{} has entered the {}".format(hero.name, self.name))
        alive = True
       
        while(alive and not self.boss_defeated):
            input("Please any value to continue...")
            time.sleep(2)
            alive = self.check_encounter(hero)
            hp_diff = hero.hero_stats.prev_stats.hit_points - hero.hero_stats.prev_stats.hit_points
            mp_diff = hero.hero_stats.prev_stats.mana_points - hero.hero_stats.mana_points
            #increments hp and mp overtime to allow for restoring values
            if(hp_diff > 0):
                if(hp_diff < 15):
                    hero.hero_stats.hit_points = hero.hero_stats.prev_stats.hit_points
                else:
                    hero.hero_stats.hit_points += 15
            if(mp_diff > 0):
                if(mp_diff < 15):
                    hero.hero_stats.mana_points = hero.hero_stats.prev_stats.mana_points
                else:
                    hero.hero_stats.mana_points += 15
                
        if(self.boss_defeated):
            return 2
        elif(not alive):
            return 1
    def check_encounter(self, hero):
        #randomized value to determine if a user meets a enemy
        if(randint(0, 100) <= (self.encounter_rate * 100)):
            #create new enemy and pop a name from the list
            #if the list is empty then enter the final boss
            if(len(self.enemy_names) > 0):
                enemy_temp = self.enemy_names.pop()
                enemy = None
                _type = enemy_temp["type"]
                _name = enemy_temp["name"]
                if(_type == "warrior"):
                    print("You have encountered {} the warrior".format(_name))
                    enemy = Warrior(_name, False)
                elif(_type == "knight"):
                    print("You have encountered {} the knight".format(_name))
                    enemy = Knight(_name, "", False)
                elif(_type == "sorceress"):
                    print("You have encountered {} the sorceress".format(_name))
                    enemy = Sorceress(_name, False)
                elif(_type == "theif"):
                    print("You have encountered {} the theif".format(_name))
                    enemy = Theif(_name, False)
                for i in range(hero.level+self.level_inc):
                    enemy.level_up()
                return hero.enter_battle(enemy)
            else:
                return self.summon_boss(hero)
        print("Nothing around here...")
        return True
    def summon_boss(self, hero):
        #summons boss of the environment
        #starts the final battle of the game
        print("You have defeated all the enemies of {}".format(self.name))
        if(self.boss == None):
            print("Unfortunately, the boss is out right now...So you win!!!")
            self.boss_defeated = True
            return True
        else:
            print("You will now face the ultimate enemy: {}".format(self.boss.name))
            for i in range(hero.level + 10):
                self.boss.level_up()
            return hero.enter_battle(self.boss)
        
        
    
    
