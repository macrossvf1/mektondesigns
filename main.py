import frame


def torsoServo(args):
    # Torso Servo stats
    # No servo may be more than one classification level above the Torso.
    torso = {
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

    print("You chose a " + args + " torso " + "with the following stats: \n" + str(torso[args]))

def ask():

    torso_prompt = ('''
        [1] superlight
        [2] lightweight
        [3] striker
        [4] medium_striker 
        [5] heavy_striker 
        [6] mediumweight 
        [7] light_heavy 
        [8] medium_heavy 
        [9] armored_heavy 
        [10] super_heavy 
        [11] mega_heavy 
        ''')

    torso_list = ['superlight', 'lightweight', 'striker', 'medium_striker', 'heavy_striker', 'mediumweight',
                  'light_heavy', 'medium_heavy', 'armored_heavy', 'super_heavy', 'mega_heavy']

    user_torso_selection = input(torso_prompt + "\n" + "Select your torso servo: ")
    user_torso_selection = torso_list[int(user_torso_selection)-1]
    #print(user_torso_selection)
    torsoServo(user_torso_selection)

if __name__ == "__main__":
    ask()
