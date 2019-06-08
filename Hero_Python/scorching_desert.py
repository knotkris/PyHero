# -*- coding: utf-8 -*-
"""
Created on Sat May 11 14:42:38 2019

@author: Knot
"""

from environment import Environment
from knight import Knight
import os
from random import randint

class ScorchingDesert(Environment):
    def __init__(self):
        #read name file to load all the names and their types
        enemies = []
        self._file = os.getcwd() + "\\desert_enemy.txt"
        enemies = self.read_enemy_file(self._file)
        Environment.__init__(self, "Desert of Unending Misery", enemies, 0.9, randint(0, 2))
        self.boss = Knight("The Ultimate Knight of Flames, Hades", "Diablo", False)
        self.boss.hero_stats.hit_points += 200
        self.boss.hero_stats.mana_points += 100
        self.boss.hero_stats.attack_power += 50
        self.boss.hero_stats.defense += 50
