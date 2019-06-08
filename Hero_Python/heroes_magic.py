# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 18:05:10 2019

@author: Knot
"""
#import used for chance variables
from random import randint, random
import os
import time
import copy
'''
Global Variable
game_state contains the state of the game
over time so that when a user wins or loses
the loop in the run function exits and the
programs exits
'''

'''
class : MAGIC
a parent class for the magic spells
to be used by the Knight and Sorceress
classes

three attributes
magic_point_usage = how much mp the skill is worth when used
effect_desc = a string of the description for the spell
duration = an integer noting how long the spell effect lasts
'''
class Magic(object):
    def __init__(self, mp_usage, desc, dur):
        self.magic_point_usage = mp_usage
        self.effect_desc = desc
        self.duration = dur
    #prints spell description
    def show_desc(self, user):
        print(self.desc)
    '''
    Decrease user's mp based on the magic_point_usage attribute
    returns false if user does not have enough mp
    otherwise decreases user mp and returns true
    '''
    def decrease_mp(self, user):
        try:
            if(user.hero_stats.mana_points - self.magic_point_usage < 0):
                print("Not enough mana")
                return False
            else:
                user.hero_stats.mana_points -= self.magic_point_usage
                return True
        except ValueError: print("Incorrect type for user; not class or child class of Hero"); return False

"""
Stats class used to hold the hero classes
stat values including
HP - health
MP - mana points
ATK - attack power
DEF - defense power
""" 
class Stats:
    #initializes stats based on passed in values
    def __init__(self, hp, mp, atkpw, defense):
        self.hit_points = hp
        self.mana_points = mp
        self.attack_power = atkpw
        self.defense = defense
        self.prev_stats = copy.deepcopy(self)
    #updates stats when a user levels up and determines
    #if the user gets any extra bonuses as well
    def updateStats(self, level, special = None, value = 0):
        self.hit_points = self.prev_stats.hit_points
        self.mana_points = self.prev_stats.mana_points
        try:
            if(level >= 0):
                self.hit_points += abs(int(20 - (level * 0.01)))
                self.mana_points += abs(int(15 - (level * 0.01)))
                self.attack_power += abs(int(5 - (level * 0.01)))
                self.defense += abs(int(3 - (level * 0.01)))
                self.prev_stats = copy.deepcopy(self)
            else:
                print("Level cannot be negative; no updates done")
        except ValueError: print("Level was not of type number; no updates done")
    #Prints out the current stats of the user
    def printStats(self):
        print(
        """
        STATS:
        HP: {}
        MP: {}
        ATK: {}
        DEF: {}""".format(self.hit_points, self.mana_points, self.attack_power, self.defense))
    def printStatsLess(self):
        print(
        """
        HP: {}
        MP: {}
        """.format(self.hit_points, self.mana_points))
"""
class Hero
Parent class to the classes Knight, Warrior and Sorceress
Contains attributes
Level - the user's level
CurrExperience - the amount of experience the user has
expToNextLvl - how experience a user needs to level up
status - the hero's status affliction or boon
status_dur - how long hero's status effect will last
name - hero's name
hero_stats - Stat's class containing all stats for hero
            Different for each of the hero classes
action_list - a dictionary containing the hero's methods that a user
              will be able to choose
"""          
class Hero(object):
    level = 1
    currExperience = 0
    expToNextLvl = level * 15.00
    #inventory = []
    status = "fine"
    status_dur = 0
    def __init__(self, name, stats = None):
        self.name = name
        self.hero_stats = stats
        self.action_list = {1: ("Attack", self.attack), 
                            3: ("Inventory", self.useItem), 
                            4: ("Run", self.run)}
    #increases the hero's level as well updates stats and resets exp to next level
    def level_up(self):
        self.level += 1
        self.hero_stats.updateStats(self.level)
        self.expToNextLvl = self.level * 10
    #adds to curr experience based on the defeated enemy's level
    def add_exp(self, enemy_level):
        try:
            self.currExperience += enemy_level * 15
            while(self.currExperience >= self.expToNextLvl):
                print("YOU'VE LEVELED UP")
                self.currExperience -= self.expToNextLvl
                self.level_up()
        except: ValueError("add exp requires an integer value")
    #a method that occurs when a user enters battle with an enemy
    #the method controls the turn cycling as well determines
    #actions that take place if either the enemy or user asloses all health      
    def enter_battle(self, enemy):
        try:
            finished = False
            hero_turn = True
            print("BEGIN FIGHT")
            while not finished:
                #self makes first move
                #then enemy moves
                turn_success = False

                if(hero_turn):
                    self.display_status()
                    enemy.display_status(True)
                    if(self.status != "fine"):
                        if(self.status_dur <= 0):
                            print("Returning your state to normal")
                            if(self.status == "enraged"):
                                self.calm_down()
                            elif(self.status == "defending"):
                                self.lower_sheild()
                            self.status_dur = 0
                            self.status = "fine"
                        if(self.status_dur > 0):
                            self.status_dur -= 1
                    if(self.status == "sleep"):
                        print("You are asleep")
                    else:
                        print("{}'s TURN".format(self.name))
                        while(not turn_success):
                            turn_success = self.take_turn(enemy)
                        #after decision
                        hero_turn = False
                    time.sleep(2)
                else:
                    if(enemy.status != "fine"):
                        if(enemy.status_dur <= 0):
                            print("Returning state to normal")
                            if(enemy.status == "enraged"):
                                enemy.calm_down()
                            elif(enemy.status == "asleep"):
                                enemy.status == "fine"
                            elif(enemy.status == "defending"):
                                enemy.lower_sheild()
                            enemy.status_dur = 0
                            enemy.status = "fine"
                        if(self.status_dur > 0):
                            self.status_dur -= 1
                    if(enemy.status == "sleep"):
                        print("enemy is asleep")
                    else:
                        print("{}'s TURN".format(enemy.name))
                        while(not turn_success):
                            turn_success = enemy.take_turn(self, True)
                        #after decision
                        hero_turn = True
                    time.sleep(2)
                #check if either of them ran away
                if(enemy.status == "ran" or self.status == "ran"):
                    print("THE BATTLE IS OVER")
                    enemy.status = "fine"
                    self.status = "fine"
                    finished = True
                    return True
                else:
                    if(not hero_turn): #hero just went
                        #check enemy health
                        #if healthy then check status for update
                        if(enemy.hero_stats.hit_points < 0):
                            #they lost
                            print("ENEMY WAS DEFEATED")
                            self.add_exp(enemy.level)
                            finished = True
                            return True
                    else:
                        if(self.hero_stats.hit_points < 0):
                            #you lost
                            
                            print("YOU WERE DEFEATED")
                            print("END GAME")
                            finished = True
                            return False
        except: ValueError("Enemy is not of correct class type")
    #method for user to choose their action
    #if activated by AI then the function chooses a random base value
    def take_turn(self, enemy, AI = False):    
        choice = 1
        try:
            if(not AI):
                try:
                    if(enemy.status == "invisible"):
                        print("{} is invisible".format(enemy.name))
                        print("You try looking for them")
                        result = enemy.invisibility_spell.check_if_failed(self, enemy)
                        if(not result):
                            print("Failed to find enemy")
                            return True
                    while(1):
                        print("OPTIONS: ")
                        choices = list(self.action_list.keys())
                        choices.sort()
                        for choice in choices:
                            print("{}. {}\t".format(choice, self.action_list[choice][0]))
                        try:
                            choice = int(input("CHOICE: "))
                            if(choice < 1 or choice > len(self.action_list)):
                                print("PLEASE ENTER A VALUE BETWEEN 1 AND {}".format(len(self.action_list)))
                            else:
                                break
                        except ValueError:
                            print("Enter a valid value")
                except ValueError: print("Enemy is not of type class Hero")
            else:
                if(enemy.status == "invisible"):
                    print("{} is invisible".format(enemy.name))
                    print("You try looking for them")
                    result = enemy.invisibility_spell.check_if_failed(self, enemy)
                    if(not result):
                        print("Failed to find enemy")
                        return True
                #randomly choose an action based on stats
                limit = len(self.action_list)
                choice = randint(1, limit)
            #certain choices from users have the need to pass
            #enemy value or not
            #also takes into account action values 
            #created in different child classes
            #by checking the action list tuple third argument
            #if it exists
            if(choice < 2 or choice == 4):
                result = self.action_list[choice][1](enemy)
            elif(choice == 2 or choice > 4):
                if(len(self.action_list[choice]) == 3 and self.action_list[choice][2]):
                    result = self.action_list[choice][1](enemy)
                else:
                    result = self.action_list[choice][1]()
            else:
                result = self.action_list[choice][1]()
            return result
        except ValueError:("AI is not of type bool")
    #attack action command
    #does damage if attack hits
    #based random chance
    def attack(self, enemy):
        try:
            hit_chance = randint(1, 20)#has a one in a 20 chance of missing
            
            hit = hit_chance > 5 
            if(hit):
                print("{} attacked!!".format(self.name))
                enemy.take_damage(self.hero_stats.attack_power)
            else:
                print("{} missed".format(self.name)) 
            return True
        except ValueError: print("Enemy is not of type class Hero")
    #calculates the damage a user recieves
    def take_damage(self, enemy_atk):
        try:
            if(enemy_atk < 0):
                print("attack cannot be lower than zero")
                return
            damage = int(enemy_atk * (1000 / (1140 + (3 * self.hero_stats.defense))))
            print("{} took {} damage".format(self.name, damage))
            self.hero_stats.hit_points -= damage
        except ValueError: print("enemy_atk should be type integer or float")
    #causes the user to escape if the chance variable is true
    #higher chance of success if user level is higher than enemy's
    def run(self, enemy):
        try:
            print("{} tries to run away".format(self.name))
            run_chance = 10 #based on the level of the enemy and self level
            run_success = run_chance > (randint(20, 100))
            if(run_success):
                self.status = "ran"
                print("RUNNING AWAY IS SUCCESSFUL")
                return True
            return False
        except ValueError: print("Enemy is not of type class Hero")
    #would allow users to use items in inventory
    def useItem(self):
        #list out inventory items
        #if items are empty then return None
        #allow user to choose another action
        #not used
        print("Inventory empty")
    #displays stat values for user
    def display_status(self, AI = False):
        print("Name: {}\tLVL: {}".format(self.name, self.level))
        self.hero_stats.printStatsLess()
        if(not AI):
            print("\tSTATUS: {}\n\tDuration: {}".format(self.status, self.status_dur))
            print("\tEXP:{}/{}".format(self.currExperience, self.expToNextLvl))
        
    #possible method def save(self) #saves all info on hero in text then reloads text file when starting

