import math

class BeamWeapons:

    def __init__(self, damage, accuracy, range, shots, clips, warmuptime,
                 wideangle,burstvalue,antimissile,antipersonnel,antipersonnelandmissile, allpurpose,
                 megabeam, longrange, fragile,disruptor, hydro):
        pass

    damage = {1: {cost: 1.5, range: 4},
        1: {cost: 1.5, range: 4},
        1: {cost: 1.5, range: 4},
        1: {cost: 1.5, range: 4},
        1: {cost: 1.5, range: 4},
        1: {cost: 1.5, range: 4},
        1: {cost: 1.5, range: 4},
        1: {cost: 1.5, range: 4},
        1: {cost: 1.5, range: 4},
        1: {cost: 1.5, range: 4},
        1: {cost: 1.5, range: 4},
        1: {cost: 1.5, range: 4},
        1: {cost: 1.5, range: 4},
        1: {cost: 1.5, range: 4},
        1: {cost: 1.5, range: 4},
        1: {cost: 1.5, range: 4},
        1: {cost: 1.5, range: 4},
        1: {cost: 1.5, range: 4},
        1: {cost: 1.5, range: 4},
        1: {cost: 1.5, range: 4}
        }

    # [Range modified, Cost multiplier]
    range = 
        [.25,.62],
        [.5, .75],
        [.75, .88],
        [1,1],
        [1.25,1.12],
        [1.5, 1.25],
        [1.75, 1.38],
        [2, 1.5],
        [2.5, 1.75],
        [3, 2]

    # [Accuracy modifier, Cost multiplier]
    accuracy = 
        [-2,.6],
        [-1,.8],
        [0,.9],
        [1,1],
        [2,1.5],
        [3,2]

    # [Warm-up time, Cost multiplier]
    warmup_time =  
        [0,1],
        [1,.9],
        [2,.7],
        [3,.6]

    # [Number of shots, Cost multiplier]
    shots = 
        [0,.33],
        [1,.5],
        [2,.6],
        [3,.7],
        [5,.8],
        [10,.9],
        [math.inf,1]


    # [Beam angle in degrees, Cost multiplier, Diameter in Hex]
    wide_angle =
        [0,2,2],
        [60,3,1],
        [180,5,1],
        [300,7,1],
        [360,9,1]

    burst_value

    clip_fed

    anti_personnel

    anti_missile

    anti_missile_anti_personnel

    all_purpose

    fragile

    long_range

    hydro

    mega_beam

    disruptor
