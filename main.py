import utils
import time 



#introduction

print('Welcome to battleships.')
time.sleep(1)
print('Your map is being created')
user_table = utils.create_table(10)
machine_table = utils.create_table(10)
time.sleep(1)
print('Your battleship fleet is moving into position')
user_fleet = utils.plot_fleet_positions(user_table)
user_table = utils.place_fleet(user_fleet, user_table)
machine_fleet = utils.plot_fleet_positions(machine_table)
time.sleep(1)
print(user_table)
time.sleep(2)
print('The enemy ships are evading our radar, but we know they are located within the quadrant below.')
time.sleep(3)
print(machine_table)
time.sleep(1)



# game loop dependant on length of players' fleet. 

while any(len(ship) > 0 for ship in machine_fleet) and any(len(ship) > 0 for ship in user_fleet):
    user_result = utils.user_firing_mechanism(machine_fleet, machine_table)
    if user_result == False:
        machine_result = utils.adversary_firing_mechanism(user_fleet, user_table) 
    
