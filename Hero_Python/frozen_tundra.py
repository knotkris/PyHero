# -*- coding: utf-8 -*-
"""
Created on Sat May 11 14:42:38 2019

@author: Knot
"""
from warrior import Warrior
from environment import Environment
import os
from random import randint

class FrozenTundra(Environment):
    def __init__(self):
        #read name file to load all the names and their types
        enemies = []
        self._file = os.getcwd() + "\\frozen_enemy.txt"
        enemies = self.read_enemy_file(self._file)
        Environment.__init__(self, "Frozen Mountains of Absolute Doom", enemies, 0.75, randint(1, 2))
        self.boss = Warrior("The Great Ice Giant, Halafor", False)
        self.boss.hero_stats.hit_points += 250
        self.boss.hero_stats.mana_points += 150
        self.boss.hero_stats.attack_power += 70
        self.boss.hero_stats.defense += 70
