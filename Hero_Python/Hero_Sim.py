# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:50:11 2019

@author: Knot
"""
from frozen_tundra import FrozenTundra
from scorching_desert import ScorchingDesert
from sorceress import Sorceress
from knight import Knight
from warrior import Warrior
from theif import Theif

game_state = 0
def choose_hero():
    #Choose your hero
        print("""
    1. Warrior
      A hero with great strength and                          
      the ability to enhance that strength
      through anger
      
    2. Knight 
      The noblest of heroes, a true defensive
      powerhouse, armed with a sheild and
      healing magic, this hero shines in defense
      
    3. Theif     
      Not the typical hero candidate, but a 
      powerful one nonetheless, with the ability
      to sneak and deal heavy damage on an opponent
      of much greater and lesser strength 
      
    4. Sorceress
      A powerful mage hero who's abilities are not
      limited to their skillset of multiple magic 
      types but the ability to create their own
      spell with the possibility of dealing
      huge damage
        """)
        choice = 0
        while(1): 
            try:
                choice = int(input("Choose what kind of hero you want to be: "))
                if(choice > 0 and choice < 5):
                    name = input("Please enter your name: ")
                    if(choice == 1):
                        #warrior
                        return Warrior(name)
                        break
                    elif(choice == 2):
                        #knight
                        familia = input("As a knight you must have a family name: ")
                        return Knight(name, familia)
                        break
                    elif(choice == 3):
                        #theif
                        return Theif(name)
                        break
                    elif(choice == 4):
                        #sorceress
                        return Sorceress(name)
                        break
                else:
                    print("Please enter a number between 1 and 4")
            except ValueError:
                print("Please enter a whole number") 
def choose_environment():
    print("Now you must choose where to start your adventure")
    print("""
      The terrible ice mountains of the Frozen Tundra...
      home to only the most vile frozen enemies of high level
      and a unholy ice giant of great power
      where you will take constant damage to your health or
      
      
      the lands of extreme heat, the Scorching Desert, a
      exhausting hot arena home to less frequent enemies
      and stomping ground of the ultimate knight""")
    while(1):
        choice = int(input("(1) Ice Adventure or (2) Desert Journey: "))
        try:
            if(choice == 1):
                #tundra
                return FrozenTundra()
                break
            elif(choice == 2):
                #desert
                return ScorchingDesert()
                break
            else:
                print("Please enter a number between 1 and 2")
        except ValueError:
            print("Please enter a whole number")
def run():
    hero = None
    environment = None
    global game_state
    while(game_state == 0):
        hero = choose_hero()
        #Choose the environment
        environment = choose_environment()
        #Enter environment
        game_state = environment.enter_environment(hero)
        if(game_state == 2):
            print("You have defeated the boss, YOU WIN!!!")
        elif(game_state == 1):
            print("You have lost, better luck next time...")
run()
    