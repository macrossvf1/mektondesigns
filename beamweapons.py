import math

class BeamWeapon:

    def __init__(self, damage):
        self.damage = damage

    def beamDamage(damage):
        damage = [
            {'damage' : 1, 'cost': 1.5, 'range': 4},
            {'damage' : 2, 'cost': 3, 'range': 6},
            {'damage' : 3, 'cost': 4.5, 'range': 7},
            {'damage' : 4, 'cost': 6, 'range': 8},
            {'damage' : 5, 'cost': 7.5, 'range': 9},
            {'damage' : 6, 'cost': 9, 'range': 10},
            {'damage' : 7, 'cost': 10.5, 'range': 11},
            {'damage' : 8,'cost': 12, 'range': 11},
            {'damage' : 9, 'cost': 13.5, 'range': 12},
            {'damage' : 10, 'cost': 15, 'range': 13},
            {'damage' : 11, 'cost': 16.5, 'range': 13},
            {'damage' : 12, 'cost': 18, 'range': 14},
            {'damage' : 13, 'cost': 19.5, 'range': 14},
            {'damage' : 14, 'cost': 21, 'range': 15},
            {'damage' : 15, 'cost': 22.5, 'range': 15},
            {'damage' : 16, 'cost': 24, 'range': 16},
            {'damage' : 17, 'cost': 25.5, 'range': 16},
            {'damage' : 18, 'cost': 27, 'range': 17},
            {'damage' : 19, 'cost': 28.5, 'range': 17},
            {'damage' : 20, 'cost': 30, 'range': 18}
            ]
        print(beam_damage[args])
        return beam_damage[args]
        

#        # [Range modified, Cost multiplier]
#        beam_range = [
#            [.25,.62],
#            [.5, .75],
#            [.75, .88],
#            [1,1],
#            [1.25,1.12],
#            [1.5, 1.25],
#            [1.75, 1.38],
#            [2, 1.5],
#            [2.5, 1.75],
#            [3, 2]
#            ]
#
#        # [Accuracy modifier, Cost multiplier]
#        beam_accuracy = 
#            [-2,.6],
#            [-1,.8],
#            [0,.9],
#            [1,1],
#            [2,1.5],
#            [3,2]
#
#        # [Warm-up time, Cost multiplier]
#        beam_warmup_time =  
#            [0,1],
#            [1,.9],
#            [2,.7],
#            [3,.6]
#
#        # [Number of shots, Cost multiplier]
#        beam_shots = 
#            [0,.33],
#            [1,.5],
#            [2,.6],
#            [3,.7],
#            [5,.8],
#            [10,.9],
#            [math.inf,1]
#
#
#        # [Beam angle in degrees, Cost multiplier, Diameter in Hex]
#        beam_wide_angle =
#            [0,2,2],
#            [60,3,1],
#            [180,5,1],
#            [300,7,1],
#            [360,9,1]
#
#        # [Burst value, Cost multiplier]
#        beam_burst_value = 
#            [2,1.5],
#            [3,2],
#            [4,2.5],
#            [5,3],
#            [6,3.5],
#            [7,4],
#            [8,4.5],
#            [math.inf,5]
#
#        # Cost Modifier
#        clip_fed = .9
#
#        # [Range multiplier, Cost multiplier]
#        anti_personnel = [1,1.8]
#        anti_missile = [1,1.8]
#        anti_missile_anti_personnel = [1,1.8]
#        all_purpose = [1,2.6]
#
#        # Cost multipliers
#        fragile = 1
#        long_range = 1.33
#        hydro = .2
#        mega_beam = 10
#        disruptor = 2
#
#        
