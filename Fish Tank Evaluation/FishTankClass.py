# File for FishTank class

# define class
class FishTank:

    # constructor
    def __innit__(self, name, gallons, num_fish, inches_fish, plants, ph, kh, nitrite, nitrate, ammonia, water_change, ans):
    
        # docstring
        """
            Create a new fish tank profile instance.

            name: how you want to refer to the tank
            gallons: how many gallons of water the tank holds
            num_fish: how many fish you have in the tank
            inches_fish: the sum of the length of all of the fish / creatures in your tank
            plants: if the tank has none (0), if there are some (1), or it is heavily planted (2)
            ph: the ph reading of the water
            kh: the kh reading of the water
            nitrite: the amount of nitrites in the water (ppm)
            nitrate: the amount of nitrates in the water (ppm)
            ammonia: the amount of ammonia in the wate (ppm)
            water_change: how many days ago the last water change was
        """
        # private variables
        self.name = name
        self.gallons = gallons
        self.num_fish = num_fish
        self.inches_fish = inches_fish
        self.plants = plants
        self.ph = ph
        self.kh = kh
        self.nitrite = nitrite
        self.nitrate = nitrate
        self.ammonia = ammonia
        self.water_change = water_change
        self.ans = ""
        
    # methods
    def get_name(self):
        # Return the name of the new tank
        return self.name

    def set_name(self):
        # Sets the value for the name variable from user input
        self.name = input("What do you want to call this tank?\n")

    def get_gallons(self):
        # Returns how many gallons the tank is
        return self.gallons
    
    def set_gallons(self):
        # Sets the value for gallons from user input
        self.gallons = int(input("How many gallons is the tank?\n"))

    def get_num_fish(self):
        # Returns how many fish / creatures are in the tank
        return self.num_fish

    def set_num_fish(self):
        # Sets the value for num_fish from user input
        self.num_fish = int(input("How many fish / creatures live in this tank?\n"))

    def get_inches_fish(self):
        # Returns the num of the length of all of the fish / creatures in the tank
        return self.inches_fish

    def set_inches_fish(self):
        # Sets the value for inches_fish from user input
        self.inches_fish = float(input("What is the sum of the length of all of the fish / creatures in this tank?\n"))

    def get_plants(self):
        # Returns the planted rating 0-2 of the tank
        return self.plants

    def set_plants(self):
        # Sets the value for the plants variable from user input
        self.plants = int(input("Is your tank planted (1), heavily planted (2), does it have no plants (0)?\n"))

    def get_ph(self):
        # Returns the ph reading of the tank
        return self.ph

    def set_ph(self):
        # Sets the value for the ph level variable from the user input
        self.ph = float(input("What is the ph reading?\n"))

    def get_kh(self):
        # Returns the kh reading of the tank
        return self.kh

    def set_kh(self):
        # Sets the value for the kh level variable from the user input
        self.kh = int(input("What is the kh level? (ppm)\n"))

    def get_nitrite(self):
        # Returns the nitrite reading of the tank (ppm)
        return self.nitrite

    def set_nitrite(self):
        # Sets the nitrite level from the user input
        self.nitrite = int(input("What is the nitrite level (ppm)\n"))

    def get_nitrate(self):
        # Returns the nitrate reading of the tank (ppm)
        return self.nitrate

    def set_nitrate(self):
        # Sets the nitrite level from the user input
        self.nitrate = int(input("What is the nitrate level? (ppm)\n"))

    def get_ammonia(self):
        # Returns the ammonia level of the tank (ppm)
        return self.ammonia

    def set_ammonia(self):
        # Sets the ammonia level of the tank from the user input (ppm)
        self.ammonia = int(input("What is the ammonia level? (ppm)\n"))

    def get_water_change(self):
        # Returns the number of days it has been since the last water change
        return self.water_change

    def set_water_change(self):
        # Sets the value for the number of days it has been since the water change from the user input
        self.water_change = int(input("How many days ago was the last water change?\n"))


    def tank_profile(self):
        print("\n\n******************************************************************************\n")
        print("Fish Tank Profile:\n")
        print("Name: ", self.name)
        print("Gallons: ", self.gallons)
        print("Number of inhabitants: ", self.num_fish)
        
        if self.plants == 0:
            print("Plants: None")
        elif self.plants == 1:
            print("Plants: Some")
        elif self.plants ==2:
            print("Plants: Heavily planted")

        print("pH: ", self.ph)
        print("kH: ", self.kh)
        print("Nitrites(ppm): ", self.nitrite)
        print("Nitrates(ppm): ", self.nitrate)
        print("Ammonia(ppm): ", self.ammonia)
        print("Last water change: ", self.water_change, " days ago")  
        print("\n******************************************************************************\n\n")



    def over_stocked(self):
        if (self.inches_fish / self.gallons) > 1:
            return True
        else:
            return False

    def planted(self):
        if self.plants > 0:
            return True
        else:
            return False

    def ph_check(self):
        if self.ph < 5.5 and self.ph > 8.5:
            return False
        else:
            return True
    
    def water_change_check(self):
        if self.water_change > 7:
            return 20
        elif self.ammonia > 0 & self.ammonia < 2:
            return 20
        elif self.ammonia >= 40:
            return 50
        elif self.nitrite > 20 & self.ammonia < 40:
            return 20
        elif self.nitrite >= 40:
            return 50
        elif self.nitrate > 25 & self.ammonia < 50:
            return 20
        elif self.nitrate >= 50:
            return 50

    def tank_eval_check(self):
        self.ans = input("Do you want to evaluate the parameters of your tank?(Y for yes, N for no)\n")
        if self.ans == "N":
            pass
        elif self.ans == "Y":
            self.tank_eval()

    def tank_eval(self):
        print("\n******************************************************************************\n\n")
        print(self.name, "evaluation\n")
        if self.over_stocked() is True:
            print("""Your tank is overstocked, you should have one inch of fish / creature per gallon of water
            This tank will require more frequent water changes
            Becareful of frequent / large water changes if there are shrimp in the tank, it could stress them out
            """)
        else:
            pass
        
        if self.planted() is True:
            print("""The plants in your tank might require fertilizer and special lighting conditions
            """)
        else:
            pass

        if self.ph_check() is True:
            print("The pH is within a normal range, but you should always make sure it is within the reccomended parameters for every creature in your tank")
        elif self.ph_check() is False:
            print("The pH is not within the normal range")
        
        print("A" + str(self.water_change_check()) + "% water change is reccomended.")



        print("\n******************************************************************************\n\n")


        




