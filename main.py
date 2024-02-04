import os, re
from beamweapons import BeamWeapon
from frame import Frame 

#big_beam_gun = BeamWeapon()

class_list = ['superlight', 'lightweight', 'striker', 'medium_striker', 'heavy_striker', 'mediumweight',
                  'light_heavy', 'medium_heavy', 'armored_heavy', 'super_heavy', 'mega_heavy']
armor_class_list = ['ablative', 'standard', 'alpha', 'beta', 'gamma']
ram_armor_class_list = ['level 1', 'level 2', 'level 3', 'level 4']

user_name = ""
user_CP = ""


def getInitialData():
    global user_name
    global user_CP

    user_name = input("What is your name?\n ")
    
    try:
        user_CP = input("How many Construction Points will you need?\n")
        user_CP = int(user_CP)
    except ValueError:
        input("That's not an acceptable value.")
        

if __name__ == "__main__":
    # Build processes
    #getInitialData()
    #buildFrame()
    buildBeamWeapon()

    # Summary
    print(
        "Name: " + user_name + "\n",
        "CP: " + str(user_CP) + "\n\n",
        "Current Build \n",
        "Torso: " + str(user_torso) + "\n",
        "Head: " + str(user_head) + "\n",
        "Arm, Right: " + str(user_arm_right) + "\n",
        "Arm, Left: " + str(user_arm_left) + "\n",
        "Leg, Right: " + str(user_leg_right) + "\n",
        "Leg, Left: " + str(user_leg_left) + "\n",
        "Wing: " + str(user_wing) + "\n",
        "Tail: " + str(user_tail) + "\n",
        "Armor: " + str(user_armor) + "\n",
        "Armor Type: " + str(user_armortype) + "\n",
        "RAM Armor: " + str(user_ram_armor) + "\n",
    )
