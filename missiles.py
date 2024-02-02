class Missiles:

    long_range = 1.33
    foam = 1.33
    hypervelocity = 1.25
    flare = .5
    fuse = 1.1
    smoke = .5
    nuclear = 1000
    scatter = .5
    smoke_scatter = 1
    countermissile = [1, 1.8]

    damage = { 
        1 : {cost: .1, range: 4},
        2 : {cost: .2, range: 5},
        3 : {cost: .3, range: 6},
        4 : {cost: .4, range: 7},
        5 : {cost: .5, range: 8},
        6 : {cost: .6, range: 9},
        7 : {cost: .7, range: 9},
        8 : {cost: .8, range: 10},
        9 : {cost: .9, range: 11},
        10 : {cost: 1, range: 11}, 
        11 : {cost: 1.1, range: 12}, 
        12 : {cost: 1.2, range: 12}, 
        13 : {cost: 1.3, range: 13}, 
        14 : {cost: 1.4, range: 13}, 
        15 : {cost: 1.5, range: 14}, 
        16 : {cost: 1.6, range: 14}, 
        17 : {cost: 1.7, range: 14}, 
        18 : {cost: 1.8, range: 15}, 
        19 : {cost: 1.9, range: 15},
        20 : {cost: 2, range: 16}, 
    }

    accuracy = {
        -2 : .6,
        -1 : .8,
        0 : 1,
        1 : 1.3,
        2 : 1.6,
        3 : 2
    }

    range = {
        0 : .5,
        .25 : 62,
        .5 : .75,
        .75 : .88,
        1 : 1,
        1.25 : 1.12,
        1.5 : 1.25,
        1.75 : 1.38,
        2 : 1.5,
        5 : 3,
        10 : 5.5,
        30 : 15.5,
        50 : 25.5
    }

    smart = {
        1 : 2.5,
        2 : 3,
        3 : 3.5,
        4 : 4
    }

    skill = {
        6 : 1,
        9 : 1.3,
        12 : 1.6,
        15 : 1.9,
        18 : 2.2,
        20 : 2.5
    }

    blast_radius = {
        1 : 3,
        2 : 4,
        3 : 5,
        4 : 6,
        5 : 7,
        6 : 7.5,
        7 : 8,
        8 : 8.5,
        9 : 9,
        10 : 10,
        20 : 20
    }

    

