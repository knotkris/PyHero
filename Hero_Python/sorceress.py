# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:17:55 2019

@author: Knot
"""
from heroes_magic import Hero, Stats
from magics import Heal, Sleep, Invisiblity
from random import randint
"""
class Sorceress
child class of Hero
attributes
healing - heal class
sleep - sleep class
invisibility - invisible class
attack spell - is just a string holding attack
spells - dict that works similarly to action_list
allows user to choose from a list of spells
"""   
class Sorceress(Hero):
    healing_magic = Heal()
    sleep_spell = Sleep()
    invisibility_spell = Invisiblity()
    attack_spell = "attack"
    
    def __init__(self, name, welcome = True):
        Hero.__init__(self, name, Stats(85, 150, 20, 15))
        if(welcome):
            print("YOU ARE A SOCERESS. WELCOME TO HERO SIM 2019....GOOD LUCK")
        #spell action list
        self.spells = {1: self.healing_magic.heal_user,
              2: self.sleep_spell.put_to_sleep, 
              3: self.invisibility_spell.turn_invisible,
              4: self.magic_attack,
              5: self.spell_craft}
        #added to action list, to allow for using spells
        self.action_list[2] = ("Cast", self.use_spell, True)
        self.AI = not welcome
    #allows user to see and cast spells from action list
    def use_spell(self, enemy):
        self.hero_stats.mana_points -= 15
        if(self.hero_stats.mana_points < 0):
            self.hero_stats.mana_points += 15
            print("Cannot use magic, mana is too low")
            return False
        try:
            if(not self.AI):
                #user chooses a spell
                print("""
                          CHOOSE SPELL
                      1.HEAL     3.INVISIBLE
                      2.SLEEP    4.ATTACK
                      5.SPELL CRAFT""")
            while(1):
                try:
                    if(not self.AI):
                        choice = int(input("CHOICE: ")) 
                    else:
                        choice = randint(1, len(self.spells))
                    if(choice <= len(self.spells) and choice > 0):
                        break
                    else:
                        print("CHOOSE A VALUE BETWEEN 1-{}".format(len(self.spells)))
                except ValueError: print("PLEASE ENTER THE VALID OPTION")
            #check to see if choice is correct
            #check if attack was chosen
            if(choice > 3):
                self.spells[choice](enemy)
            elif(choice == 2):
                self.spells[choice](self, enemy)
            else:
                self.spells[choice](self)
            return True
        except ValueError: print("Enemy not of correct type class Hero"); return False
    #Does magic attack based on mp stat
    def magic_attack(self, enemy):
        try:
            print("{} uses magic attack".format(self.name))
            atk_damage = self.hero_stats.mana_points // 7.5
            enemy.take_damage(atk_damage)
            return True
        except ValueError: print("Enemy not of correct type class Hero"); return False
    '''def speech_craft(self, enemy):
        #based on the level
        #user has the chance of different effects
        #1. enemy runs and battle ends
        #2. enemy becomes enraged and gains +15 attack
        print("YOU TRY SPEECH CRAFTING")
        success = randint(0, 100) < 55 + (self.level - enemy.level)
        if(not success): 
            enemy.status = "enraged"
            enemy.status_dur = 2
            enemy.hero_stats.attack_power += 10
        return True'''
    def spell_craft(self, enemy):
        try:
            #check to make sure enemy type is of type HERO, KNIGHT, WARRIOR, SORCERESS
            #has the chance of using a randomly generated attack spell
            print("YOU TRY OUT A NEW SPELL")
            success = randint(0, 100) < 45 + (self.level - enemy.level)
            if(success):
                print("YOU SUCCEEDED IN MAKING A HUGE FIREBALL")
                enemy.take_damage(self.hero_stats.attack_power + randint(30, 50))
            else:
                print("YOU FAILED AND TRIPPED OVER YOUR ROBE")
            return True
        except ValueError: print("Enemy not of correct type class Hero"); return False        
