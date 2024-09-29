import numpy as np

import random

import time


def create_table(size):
    table = np.full((size,size), "·")
    return table



def place_battleship(battleship, table):
    for position in battleship:
        table[position] = "O"
    return table



def fire(position, table):
    if table[position] == "#":
        print("Direct hit!")
        table[position] = "X"
    else:
        print("Miss!")
        table[position] = "≈"
    return table



def create_battleship(longitude):
    position_0 = (random.randint(0,5), random.randint(0,5))
    orientation = random.choice(["Vertical", "Horizontal"])

    battleship = [position_0]
    position = position_0
    while len(battleship) < longitude:
        if orientation == "Vertical":
            position = (position[0]+1, position[1])
            battleship.append(position) # Vertical
        else:
            position = (position[0], position[1]+1)
            battleship.append(position) # Horizontal
    return battleship



def plot_fleet_positions(table):

    list_coordinates = [create_battleship(4), create_battleship(3), create_battleship(3), create_battleship(2), create_battleship(2), create_battleship(2)]

    for ships in list_coordinates:
        for y, x in ships:
            if table[x,y] == '#':
                return plot_fleet_positions(table)
            else:
                return list_coordinates



def place_fleet(fleet, table):
    for ship in fleet:
        for coordinate in ship:
            table[coordinate] = '#'
    return table 



def user_firing_mechanism(fleet, target_map):

    hit = True

    while hit == True:
        
        hit = False #reset flow if hit 
        position = input('Write longitude and latitude separated by comma, no spaces: ').split(',')
        position = tuple(map(int, position))

        for ship in fleet:
                
                if position in ship:
                    print('Direct hit!')
                    ship.remove(position)
                    target_map[position] = 'X'
                    print(target_map)

                    if len(ship) == 0:
                        print('Enemy ship destroyed!')
                    
                    hit = True #hit detected so allow loop to continue
                    break #hit detected so no need to iterate through other ships. restart while loop, since hit==True
                    
        if hit == False: #if hit is still false after the loop through all ships, then it is a miss. 
            print('Miss')
            target_map[position] = '0'
            print(target_map)
            return False 



def adversary_firing_mechanism(fleet, target_map):

    hit = True

    while hit == True:
        
        hit = False #reset flow if hit 
        position = (random.randint(0,9), random.randint(0,9))

        for ship in fleet:
                
                if position in ship:
                    print('Direct hit!')
                    ship.remove(position)
                    target_map[position] = 'X'
                    print(target_map)

                    if len(ship) == 0:
                        print('Enemy ship destroyed!')
                    
                    hit = True #hit detected so allow loop to continue
                    break #hit detected so no need to iterate through other ships. restart while loop, since hit==True
                    
        if hit == False: #if hit is still false after the loop through all ships, then it is a miss. 
            print('Miss')
            target_map[position] = '0'
            print(target_map)
            return False 