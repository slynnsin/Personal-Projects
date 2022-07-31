# Sarah Sindeband
# 7/13/22
# Fishtank
# Description: this program will get input from the user about their fishtank and diagnose an issue
# if there is one.


from FishTankClass import FishTank
tank = FishTank()

tank.set_name()
tank.set_gallons()
tank.set_num_fish()
tank.set_inches_fish()
tank.set_plants()
tank.set_nitrate()
tank.set_nitrite()
tank.set_ammonia()
tank.set_ph()
tank.set_kh()
tank.set_water_change()

tank.tank_profile()

tank.tank_eval_check()

#first = FishTank("20gallon", 20, 18, 25.5, 1, 6.5, 180, 0, 0, 0, 2)

#first = FishTank()

#print(first.get_name())



