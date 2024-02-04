import os, re

class_list = ['superlight', 'lightweight', 'striker', 'medium_striker', 'heavy_striker', 'mediumweight',
                  'light_heavy', 'medium_heavy', 'armored_heavy', 'super_heavy', 'mega_heavy']
armor_class_list = ['ablative', 'standard', 'alpha', 'beta', 'gamma']
ram_armor_class_list = ['level 1', 'level 2', 'level 3', 'level 4']

user_CP = ""

# Mekton Parts, putting it all together for a complete mekton.
user_torso = "" 
user_head = ""
user_arm_right = ""
user_arm_left = ""
user_leg_right = ""
user_leg_left = ""
user_wing = ""
user_tail = ""
user_pod = ""
user_armor = ""
user_ram_armor = ""
user_weapons = ""
user_additives = ""
user_specials = ""
user_multis = ""


def torsoServo(args):
    # Torso Servo stats
    # No servo may be more than one classification level above the Torso.
    torso_servo = {
       'superlight': {'cost': 2, 'space': 2, 'kills': 2},
       'lightweight': {'cost': 4, 'space': 4, 'kills': 4},
       'striker': {'cost': 6, 'space': 6, 'kills': 6},
       'medium_striker': {'cost': 8, 'space': 8, 'kills': 8},
       'heavy_striker': {'cost': 10, 'space': 10, 'kills': 10},
       'mediumweight': {'cost': 12, 'space': 12, 'kills': 12},
       'light_heavy': {'cost': 14, 'space': 14, 'kills': 14},
       'medium_heavy': {'cost': 16, 'space': 16, 'kills': 16},
       'armored_heavy': {'cost': 18, 'space': 18, 'kills': 18},
       'super_heavy': {'cost': 20, 'space': 20, 'kills': 20},
       'mega_heavy': {'cost': 22, 'space': 22, 'kills': 22}
        }

    return torso_servo[args]


def headServo(args):
    # Head Servo stats
    # Sensors not placed in the head will suffer a -2 to Awareness rolls.
    head_servo = {
       'superlight': {'cost': 1, 'space': 1, 'kills': 1},
       'lightweight': {'cost': 2, 'space': 2, 'kills': 2},
       'striker': {'cost': 3, 'space': 3, 'kills': 3},
       'medium_striker': {'cost': 4, 'space': 4, 'kills': 4},
       'heavy_striker': {'cost': 5, 'space': 5, 'kills': 5},
       'mediumweight': {'cost': 6, 'space': 6, 'kills': 6},
       'light_heavy': {'cost': 7, 'space': 7, 'kills': 7},
       'medium_heavy': {'cost': 8, 'space': 8, 'kills': 8},
       'armored_heavy': {'cost': 9, 'space': 9, 'kills': 9},
       'super_heavy': {'cost': 10, 'space': 10, 'kills': 10},
       'mega_heavy': {'cost': 11, 'space': 11, 'kills': 11}
      }

    return head_servo[args]

def armServo(args):
    # Arm Servo stats
    # 
    arm_servo = {
       'superlight': {'cost': 2, 'space': 2, 'kills': 2, 'damage_add': 0, 'throw': 1},
       'lightweight': {'cost': 3, 'space': 3, 'kills': 3, 'damage_add': 0, 'throw': 2},
       'striker': {'cost': 4, 'space': 4, 'kills': 4, 'damage_add': 0, 'throw': 2},
       'medium_striker': {'cost': 5, 'space': 5, 'kills':5, 'damage_add': 1, 'throw': 3},
       'heavy_striker': {'cost': 6, 'space': 6, 'kills': 6, 'damage_add': 1, 'throw': 3},
       'mediumweight': {'cost': 7, 'space': 7, 'kills': 7, 'damage_add': 1, 'throw': 4},
       'light_heavy': {'cost': 8, 'space': 8, 'kills': 8, 'damage_add': 2, 'throw': 4},
       'medium_heavy': {'cost': 9, 'space': 9, 'kills': 9, 'damage_add': 2, 'throw': 5},
       'armored_heavy': {'cost': 10, 'space': 10, 'kills': 10, 'damage_add': 2, 'throw': 5},
       'super_heavy': {'cost': 11, 'space': 11, 'kills': 11, 'damage_add': 3, 'throw': 6},
       'mega_heavy': {'cost': 12, 'space': 12, 'kills': 12, 'damage_add': 3, 'throw': 6}
      }

    return arm_servo[args]

def legServo(args):
    # Leg Servo stats
    # Leg servos may not be smaller than 1 classification level lower than it's Torso's classification
    # level.
    leg_servo = {
       'superlight': {'cost': 2, 'space': 2, 'kills': 2, 'damage_add': 0},
       'lightweight': {'cost': 3, 'space': 3, 'kills': 3, 'damage_add': 0},
       'striker': {'cost': 4, 'space': 4, 'kills': 4, 'damage_add': 1},
       'medium_striker': {'cost': 5, 'space': 5, 'kills':5, 'damage_add': 1},
       'heavy_striker': {'cost': 6, 'space': 6, 'kills': 6, 'damage_add': 2},
       'mediumweight': {'cost': 7, 'space': 7, 'kills': 7, 'damage_add': 2},
       'light_heavy': {'cost': 8, 'space': 8, 'kills': 8, 'damage_add': 3},
       'medium_heavy': {'cost': 9, 'space': 9, 'kills': 9, 'damage_add': 3},
       'legored_heavy': {'cost': 10, 'space': 10, 'kills': 10, 'damage_add': 4},
       'super_heavy': {'cost': 11, 'space': 11, 'kills': 11, 'damage_add': 4},
       'mega_heavy': {'cost': 12, 'space': 12, 'kills': 12, 'damage_add': 5}
      }

    return leg_servo[args]

def wingServo(args):
    # Wing Servo stats
    # 
    wing_servo = {
       'superlight': {'cost': 1, 'space': 1, 'kills': 1},
       'lightweight': {'cost': 2, 'space': 2, 'kills': 2},
       'striker': {'cost': 3, 'space': 3, 'kills': 3},
       'medium_striker': {'cost': 4, 'space': 4, 'kills':4},
       'heavy_striker': {'cost': 5, 'space': 5, 'kills': 5},
       'mediumweight': {'cost': 6, 'space': 6, 'kills': 6},
       'light_heavy': {'cost': 7, 'space': 7, 'kills': 7},
       'medium_heavy': {'cost': 8, 'space': 8, 'kills': 8},
       'wingored_heavy': {'cost': 9, 'space': 9, 'kills': 9},
       'super_heavy': {'cost': 10, 'space': 10, 'kills': 10},
       'mega_heavy': {'cost': 11, 'space': 11, 'kills': 11}
      }

    return wing_servo[args]

def tailServo(args):
    # Tail Servo stats
    # 
    tail_servo = {
       'superlight': {'cost': 1, 'space': 1, 'kills': 1},
       'lightweight': {'cost': 2, 'space': 2, 'kills': 2},
       'striker': {'cost': 3, 'space': 3, 'kills': 3},
       'medium_striker': {'cost': 4, 'space': 4, 'kills':4},
       'heavy_striker': {'cost': 5, 'space': 5, 'kills': 5},
       'mediumweight': {'cost': 6, 'space': 6, 'kills': 6},
       'light_heavy': {'cost': 7, 'space': 7, 'kills': 7},
       'medium_heavy': {'cost': 8, 'space': 8, 'kills': 8},
       'wingored_heavy': {'cost': 9, 'space': 9, 'kills': 9},
       'super_heavy': {'cost': 10, 'space': 10, 'kills': 10},
       'mega_heavy': {'cost': 11, 'space': 11, 'kills': 11}
      }

    return tail_servo[args]

def podServo(args):
    # Pod Servo stats
    # 
    wing_servo = {
       'superlight': {'cost': 1, 'space': 2},
       'lightweight': {'cost': 2, 'space': 4},
       'striker': {'cost': 3, 'space': 6},
       'medium_striker': {'cost': 4, 'space': 8},
       'heavy_striker': {'cost': 5, 'space': 10},
       'mediumweight': {'cost': 6, 'space': 12},
       'light_heavy': {'cost': 7, 'space': 14},
       'medium_heavy': {'cost': 8, 'space': 16},
       'wingored_heavy': {'cost': 9, 'space': 18},
       'super_heavy': {'cost': 10, 'space': 20},
       'mega_heavy': {'cost': 11, 'space': 22}
      }

    return wing_servo[args]

def armor(args):
    # Armor stats
    armor = {
       'superlight': {'cost': 1, 'stopping_power': 1},
       'lightweight': {'cost': 2, 'stopping_power': 2},
       'striker': {'cost': 3, 'stopping_power': 3},
       'medium_striker': {'cost': 4, 'stopping_power': 4},
       'heavy_striker': {'cost': 5, 'stopping_power': 5},
       'mediumweight': {'cost': 6, 'stopping_power': 6},
       'light_heavy': {'cost': 7, 'stopping_power': 7},
       'medium_heavy': {'cost': 8, 'stopping_power': 8},
       'wingored_heavy': {'cost': 9, 'stopping_power': 9},
       'super_heavy': {'cost': 10, 'stopping_power': 10},
       'mega_heavy': {'cost': 11, 'stopping_power': 11}
      }

    return armor[args]

def armorType(args):
    armor_type = { 
       'ablative': {'damage_coefficient': 0, 'cost': .5},
       'standard': {'damage_coefficient': 1, 'cost': 1},
       'alpha': {'damage_coefficient': 2, 'cost': 1.25},
       'beta': {'damage_coefficient': 4, 'cost': 1.25},
       'gamma': {'damage_coefficient': 8, 'cost': 2}
     }

    return armor_type[args]

def ramArmor(args):
    ram_armor = {
        'level 1': {'absorption_coefficient': .2, 'cost': 1.5, 'penalty': 1},
        'level 2': {'absorption_coefficient': .25, 'cost': 1.8, 'penalty': .8},
        'level 3': {'absorption_coefficient': .33, 'cost': 2.2, 'penalty': .75},
        'level 4': {'absorption_coefficient': .5, 'cost': 2.5, 'penalty': .66}
      }

    return ram_armor[args]

def ask():
    global user_torso
    global user_head
    global user_arm_right
    global user_arm_left
    global user_leg_right
    global user_leg_left
    global user_wing
    global user_tail
    global user_pod 
    global user_armor
    global user_ram_armor
    global user_weapons
    global user_additives
    global user_specials
    global user_multis

    # General prompt for selecting the class of the servo.
    class_selection_prompt = ('''
        [1] Superlight
        [2] Lightweight
        [3] Striker
        [4] Medium Striker 
        [5] Heavy Striker 
        [6] Mediumweight 
        [7] Light Heavy 
        [8] Medium Heavy 
        [9] Armored Heavy 
        [10] Super Heavy 
        [11] Mega Heavy 

        Select your servo class: 
        ''')
    armor_type_prompt = ('''
        [1] Ablative
        [2] Standard
        [3] Alpha
        [4] Beta
        [5] Gamma

        Select your Armor Type: 
        ''')
    ram_armor_prompt = ('''
        [1] Level 1
        [2] Level 2
        [3] Level 3
        [4] Level 4

        Select your RAM Armor level: 
        ''')

    os.system('clear')

    while True:
        try:

            # Ask the user to select a Torso.
            user_torso_selection = input("Select the Torso Class: " + class_selection_prompt)
            user_torso_selection = class_list[int(user_torso_selection)-1]
            user_torso = {user_torso_selection: torsoServo(user_torso_selection)}
            os.system('clear')

            # Ask the user to select a Head.
            user_head_selection = input("Select the Head Class: " + class_selection_prompt)
            user_head_selection = class_list[int(user_head_selection)-1]
            user_head = {user_head_selection: headServo(user_head_selection)}
            os.system('clear')
            
            # Ask the user to select Right Arm.
            user_arm_right_selection = input("Select the Right Arm Class: " + class_selection_prompt)
            user_arm_right_selection = class_list[int(user_arm_right_selection)-1]
            user_arm_right = {user_arm_right_selection: armServo(user_arm_right_selection)}
            os.system('clear')

            # Ask the user to select Left Arm.
            user_arm_left_selection = input("Select the Left Arm Class: " + class_selection_prompt)
            user_arm_left_selection = class_list[int(user_arm_left_selection)-1]
            user_arm_left = {user_arm_left_selection: armServo(user_arm_left_selection)}
            os.system('clear')

            # Ask the user to select Right Leg.
            user_leg_right_selection = input("Select the Right Leg Class: " + class_selection_prompt)
            user_leg_right_selection = class_list[int(user_leg_right_selection)-1]
            user_leg_right = {user_leg_right_selection: legServo(user_leg_right_selection)}
            os.system('clear')

            # Ask the user to select Left Leg.
            user_leg_left_selection = input("Select the Left Leg Class: " + class_selection_prompt)
            user_leg_left_selection = class_list[int(user_leg_left_selection)-1]
            user_leg_left = {user_leg_left_selection: legServo(user_leg_left_selection)}
            os.system('clear')

            # Ask the user to select a Armor.
            user_armor_selection = input("Select the Armor Class: " + class_selection_prompt)
            user_armor_selection = class_list[int(user_armor_selection)-1]
            user_armor = {user_armor_selection: armor(user_armor_selection)}
            os.system('clear')

            # Ask the user to select a Armor Type.
            user_armortype_selection = input("Select the Armor Type Class: " + armor_type_prompt)
            user_armortype_selection = armor_class_list[int(user_armortype_selection)-1]
            user_armortype = {user_armortype_selection: armorType(user_armortype_selection)}
            os.system('clear')

            # Ask the user to select RAM Armor Type.
            user_ram_armor_selection = input("Select the RAM Armor Type Class: " + ram_armor_prompt)
            user_ram_armor_selection = ram_armor_class_list[int(user_ram_armor_selection)-1]
            user_ram_armor = {user_ram_armor_selection: ramArmor(user_ram_armor_selection)}
            os.system('clear')

        except (IndexError, ValueError):
            input("Press ENTER to try again.")
            os.system('clear')
            continue
        else:
            break

if __name__ == "__main__":
    ask()

    print(
        "Current Build \n",
        "Torso: " + str(user_torso) + "\n",
        "Head: " + str(user_head) + "\n",
        "Arm, Right: " + str(user_arm_right) + "\n",
        "Arm, Left: " + str(user_arm_left) + "\n",
        "Leg, Right: " + str(user_leg_right) + "\n",
        "Leg, Left: " + str(user_leg_left) + "\n",
        "Armor: " + str(user_ram_armor) + "\n",
        "RAM Armor: " + str(user_ram_armor) + "\n",
    )
