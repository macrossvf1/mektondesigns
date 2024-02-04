import os, re
from beamweapons import BeamWeapon
#from frame import Frame 


class_list = ['superlight', 'lightweight', 'striker', 'medium_striker', 'heavy_striker', 'mediumweight',
                  'light_heavy', 'medium_heavy', 'armored_heavy', 'super_heavy', 'mega_heavy']
armor_class_list = ['ablative', 'standard', 'alpha', 'beta', 'gamma']
ram_armor_class_list = ['level 1', 'level 2', 'level 3', 'level 4']

user_name = ""
user_CP = ""

weapon_inventory = []
missile_inventory = {}


def getInitialData():
    global user_name
    global user_CP

    user_name = input("What is your name?\n ")
    
    try:
        user_CP = input("How many Construction Points will you need?\n")
        user_CP = int(user_CP)
    except ValueError:
        input("That's not an acceptable value.")
        
def buildFrame():
    pass

def buildBeamWeapon():
    # Gather user input to send to BeamWeapon class to create an instance of that weapon.
    global weapon_inventory
    beam_weapon = {}    # Create a dictionary of the new weapon's stats
    beam_name = ""
    beam_damage = ""    # Get table values from beamweapons
    beam_range = ""
    beam_accuracy = ""
    beam_shots = ""
    beam_burst_value = ""
    beam_warm_up_time = ""
    beam_wide_angle = ""
    beam_clipfed = False
    beam_anti_missile = False
    beam_anti_personnel = False
    beam_anti_missile_personnel = False
    beam_all_purpose = False
    beam_fragile = False
    beam_long_range = False
    beam_hydro = False
    beam_disruptor = False

    beam_name = input("Name the new beam weapon.\n")
    beam_weapon['Beam Weapon'] = beam_name

    beam_damage = input("How much damage will the beam weapon do? (1-20)\n")
    #beam_weapon['Beam Damage'] = beam_damage
   
    new_beam_weapon = BeamWeapon(beam_damage)
    print(new_beam_weapon.beamDamage())

    # Update Weapons Inventory with the new Beam Weapon.
    weapon_inventory.append(beam_weapon)

if __name__ == "__main__":
    # Build processes
    #getInitialData()
    #buildFrame()
    buildBeamWeapon()


# Summary
#    print(
#        "Name: " + user_name + "\n",
#        "CP: " + str(user_CP) + "\n\n",
#        "Current Build \n",
#        "Torso: " + str(user_torso) + "\n",
#        "Head: " + str(user_head) + "\n",
#        "Arm, Right: " + str(user_arm_right) + "\n",
#        "Arm, Left: " + str(user_arm_left) + "\n",
#        "Leg, Right: " + str(user_leg_right) + "\n",
#        "Leg, Left: " + str(user_leg_left) + "\n",
#        "Wing: " + str(user_wing) + "\n",
#        "Tail: " + str(user_tail) + "\n",
#        "Armor: " + str(user_armor) + "\n",
#        "Armor Type: " + str(user_armortype) + "\n",
#        "RAM Armor: " + str(user_ram_armor) + "\n",
#    )
