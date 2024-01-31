class Frame:
    def __init__(self, torso, head, arms, legs, wings, tail, pods, armor, armor_type, ram_armor):
        self.torso = torso
        self.head = head
        self.arms = arms
        self.legs = legs
        self.wings = wings
        self.tail = tail
        self.pods = pods
        self.armor = armor
        self.armor_type = armor_type
        self.ram_armor = ram_armor

    def torsoServo():
        # Torso Servo stats
        # No servo may be more than one classification level above the Torso.
        torso_servo = {superlight: {cost: 2, space: 2, kills: 2},
                   lightweight: {cost: 4, space: 4, kills: 4},
                   striker: {cost: 6, space: 6, kills: 6},
                   medium_striker: {cost: 8, space: 8, kills 8},
                   heavy_striker: {cost: 10, space: 10, kills: 10},
                   mediumweight: {cost: 12, space: 12, kills: 12},
                   light_heavy: {cost: 14, space: 14, kills: 14},
                   medium_heavy: {cost: 16, space: 16, kills: 16},
                   armored_heavy: {cost: 18, space: 18, kills: 18},
                   super_heavy: {cost: 20, space: 20, kills: 20},
                   mega_heavy: {cost: 22, space: 22, kills: 22}
                  }

    def headServo():
        # Head Servo stats
        # Sensors not placed in the head will suffer a -2 to Awareness rolls.
        head_servo = {superlight: {cost: 1, space: 1, kills: 1},
                   lightweight: {cost: 2, space: 2, kills: 2},
                   striker: {cost: 3, space: 3, kills: 3},
                   medium_striker: {cost: 4, space: 4, kills 4},
                   heavy_striker: {cost: 5, space: 5, kills: 5},
                   mediumweight: {cost: 6, space: 6, kills: 6},
                   light_heavy: {cost: 7, space: 7, kills: 7},
                   medium_heavy: {cost: 8, space: 8, kills: 8},
                   armored_heavy: {cost: 9, space: 9, kills: 9},
                   super_heavy: {cost: 10, space: 10, kills: 10},
                   mega_heavy: {cost: 11, space: 11, kills: 11}
                  }

    def armServo():
        # Arm Servo stats
        # 
        arm_servo = {superlight: {cost: 2, space: 2, kills: 2, damage_add: 0, throw: 1},
                   lightweight: {cost: 3, space: 3, kills: 3, damage_add: 0, throw: 2},
                   striker: {cost: 4, space: 4, kills: 4, damage_add: 0, throw: 2},
                   medium_striker: {cost: 5, space: 5, kills 5, damage_add: 1, throw: 3},
                   heavy_striker: {cost: 6, space: 6, kills: 6, damage_add: 1, throw: 3},
                   mediumweight: {cost: 7, space: 7, kills: 7, damage_add: 1, throw: 4},
                   light_heavy: {cost: 8, space: 8, kills: 8, damage_add: 2, throw: 4},
                   medium_heavy: {cost: 9, space: 9, kills: 9, damage_add: 2, throw: 5},
                   armored_heavy: {cost: 10, space: 10, kills: 10, damage_add: 2, throw: 5},
                   super_heavy: {cost: 11, space: 11, kills: 11, damage_add: 3, throw: 6},
                   mega_heavy: {cost: 12, space: 12, kills: 12, damage_add: 3, throw: 6}
                  }

    def legServo():
        # Leg Servo stats
        # Leg servos may not be smaller than 1 classification level lower than it's Torso's classification
        # level.
        leg_servo = {superlight: {cost: 2, space: 2, kills: 2, damage_add: 0},
                   lightweight: {cost: 3, space: 3, kills: 3, damage_add: 0},
                   striker: {cost: 4, space: 4, kills: 4, damage_add: 1},
                   medium_striker: {cost: 5, space: 5, kills 5, damage_add: 1},
                   heavy_striker: {cost: 6, space: 6, kills: 6, damage_add: 2},
                   mediumweight: {cost: 7, space: 7, kills: 7, damage_add: 2},
                   light_heavy: {cost: 8, space: 8, kills: 8, damage_add: 3},
                   medium_heavy: {cost: 9, space: 9, kills: 9, damage_add: 3},
                   legored_heavy: {cost: 10, space: 10, kills: 10, damage_add: 4},
                   super_heavy: {cost: 11, space: 11, kills: 11, damage_add: 4},
                   mega_heavy: {cost: 12, space: 12, kills: 12, damage_add: 5}
                  }

    def wingServo():
        # Wing Servo stats
        # 
        wing_servo = {superlight: {cost: 1, space: 1, kills: 1},
                   lightweight: {cost: 2, space: 2, kills: 2},
                   striker: {cost: 3, space: 3, kills: 3},
                   medium_striker: {cost: 4, space: 4, kills 4},
                   heavy_striker: {cost: 5, space: 5, kills: 5},
                   mediumweight: {cost: 6, space: 6, kills: 6},
                   light_heavy: {cost: 7, space: 7, kills: 7},
                   medium_heavy: {cost: 8, space: 8, kills: 8},
                   wingored_heavy: {cost: 9, space: 9, kills: 9},
                   super_heavy: {cost: 10, space: 10, kills: 10},
                   mega_heavy: {cost: 11, space: 11, kills: 11}
                  }

    def tailServo():
        # Tail Servo stats
        # 
        tail_servo = {superlight: {cost: 1, space: 1, kills: 1},
                   lightweight: {cost: 2, space: 2, kills: 2},
                   striker: {cost: 3, space: 3, kills: 3},
                   medium_striker: {cost: 4, space: 4, kills 4},
                   heavy_striker: {cost: 5, space: 5, kills: 5},
                   mediumweight: {cost: 6, space: 6, kills: 6},
                   light_heavy: {cost: 7, space: 7, kills: 7},
                   medium_heavy: {cost: 8, space: 8, kills: 8},
                   wingored_heavy: {cost: 9, space: 9, kills: 9},
                   super_heavy: {cost: 10, space: 10, kills: 10},
                   mega_heavy: {cost: 11, space: 11, kills: 11}
                  }

    def podServo():
        # Pod Servo stats
        # 
        wing_servo = {superlight: {cost: 1, space: 2},
                   lightweight: {cost: 2, space: 4},
                   striker: {cost: 3, space: 6},
                   medium_striker: {cost: 4, space: 8},
                   heavy_striker: {cost: 5, space: 10},
                   mediumweight: {cost: 6, space: 12},
                   light_heavy: {cost: 7, space: 14},
                   medium_heavy: {cost: 8, space: 16},
                   wingored_heavy: {cost: 9, space: 18},
                   super_heavy: {cost: 10, space: 20},
                   mega_heavy: {cost: 11, space: 22}
                  }

    def Armor():
        # Armor stats
        armor = {superlight: {cost: 1, stopping_power: 1},
                   lightweight: {cost: 2, stopping_power: 2},
                   striker: {cost: 3, stopping_power: 3},
                   medium_striker: {cost: 4, stopping_power: 4},
                   heavy_striker: {cost: 5, stopping_power: 5},
                   mediumweight: {cost: 6, stopping_power: 6},
                   light_heavy: {cost: 7, stopping_power: 7},
                   medium_heavy: {cost: 8, stopping_power: 8},
                   wingored_heavy: {cost: 9, stopping_power: 9},
                   super_heavy: {cost: 10, stopping_power: 10},
                   mega_heavy: {cost: 11, stopping_power: 11}
                  }
    def armorType():
        armorTypes = {ablative: {damage_coefficient: 0, cost: .5},
                      standard: {damage_coefficient: 1, cost: 1},
                      alpha: {damage_coefficient: 2, cost: 1.25},
                      beta: {damage_coefficient: 4, cost: 1.25},
                      gamma: {damage_coefficient: 8, cost: 2}
                     }

    def ram_armor():
        ram_armor = {1: {absorption_coefficient: .2, cost: 1.5, penalty: 1},
                     2: {absorption_coefficient: .25, cost: 1.8, penalty: .8},
                     3: {absorption_coefficient: .33, cost: 2.2, penalty: .75},
                     4: {absorption_coefficient: .5, cost: 2.5, penalty: .66}

