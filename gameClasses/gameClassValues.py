'''
hp -> health points; how much damage a unit can take
mspd -> move speed; how fast a unit moves
aspd -> attack speed; how many seconds before a unit can attack after attacking
dmg -> damage the unit deals to an enemy
bounty -> how much gold the unit will give to the enemy player that kills it
exp -> experience; how much experience the unit will give to the enemy player that kills it


EXAMPLE:
Caveman = {
    "hp" : 0,
    "mspd" : 0,
    "aspd" : 0,
    "dmg" : 0,
    "bounty" : 0,
    "exp" : 0,
    "cost" : 0,
    "range" : 50,
    "img" : 'graphics\stickman.png'
    "imgScale" : (100,100) # width, height
}
'''


Melee_Caveman = {
    "hp" : 3,
    "mspd" : 1,
    "aspd" : 10,
    "dmg" : 1,
    "bounty" : 1,
    "exp" : 1,
    "cost" : 3,
    "range" : 100,
    "img" : 'graphics/unit_melee/melee_prehistoric_1.png',
    "imgScale" : (100,100)
}
Melee_Footman = {
    "hp" : 5,
    "mspd" : 1,
    "aspd" : 10,
    "dmg" : 2,
    "bounty" : 3,
    "exp" : 3,
    "cost" : 5,
    "range" : 100,
    "img" : 'graphics/unit_melee/melee_medieval_1.png',
    "imgScale" : (100,100)
}
Melee_Soldier = {
    "hp" : 8,
    "mspd" : 1,
    "aspd" : 10,
    "dmg" : 3,
    "bounty" : 9,
    "exp" : 9,
    "cost" : 7,
    "range" : 100,
    "img" : 'graphics/unit_melee/melee_modern_1_1.png',
    "imgScale" : (100,100)
}
Melee_Robot = {
    "hp" : 12,
    "mspd" : 1,
    "aspd" : 10,
    "dmg" : 4,
    "bounty" : 27,
    "exp" : 27,
    "cost" : 10,
    "range" : 100,
    "img" : 'graphics/unit_melee/melee_scifi_1.png',
    "imgScale" : (100,100)
}
Ranged_Slingshotter = {
    "hp" : 3,
    "mspd" : 1.3,
    "aspd" : 5,
    "dmg" : 1,
    "bounty" : 2,
    "exp" : 2,
    "cost" : 5,
    "range" : 200,
    "img" : 'graphics/unit_ranged/ranged_prehistoric_1.png',
    "imgScale" : (100,100)
}
Ranged_Archer = {
    "hp" : 5,
    "mspd" : 1.4,
    "aspd" : 5,
    "dmg" : 2,
    "bounty" : 4,
    "exp" : 4,
    "cost" : 8,
    "range" : 300,
    "img" : 'graphics/unit_ranged/ranged_medieval_1.png',
    "imgScale" : (100,100)
}
Ranged_Sniper = {
    "hp" : 7,
    "mspd" : 1.5,
    "aspd" : 5,
    "dmg" : 3,
    "bounty" : 16,
    "exp" : 16,
    "cost" : 11,
    "range" : 400,
    "img" : 'graphics/unit_ranged/ranged_modern_1_1.png',
    "imgScale" : (100,100)
}
Ranged_Stormtrooper = {
    "hp" : 9,
    "mspd" : 1.6,
    "aspd" : 5,
    "dmg" : 4,
    "bounty" : 32,
    "exp" : 32,
    "cost" : 15,
    "range" : 500,
    "img" : 'graphics/unit_ranged/ranged_scifi_1.png',
    "imgScale" : (100,100)
}

Tank_DinoRider = {
    "hp" : 15,
    "mspd" : 0.5,
    "aspd" : 3,
    "dmg" : 3,
    "bounty" : 12,
    "exp" : 12,
    "cost" : 10,
    "range" : 130,
    "img" : 'graphics/unit_tank/tank_prehistoric.png',
    "imgScale" : (256,185)
}

Tank_Cavalier = {
    "hp" : 30,
    "mspd" : 0.5,
    "aspd" : 3,
    "dmg" : 5,
    "bounty" : 24,
    "exp" : 24,
    "cost" : 15,
    "range" : 150,
    "img" : 'graphics/unit_tank/tank_medieval.png',
    "imgScale" : (168,143)
}

Tank_Tank = {
    "hp" : 50,
    "mspd" : 0.5,
    "aspd" : 3,
    "dmg" : 7,
    "bounty" : 36,
    "exp" : 36,
    "cost" : 20,
    "range" : 200,
    "img" : 'graphics/unit_tank/tank_modern.png',
    "imgScale" : (320,192)
}

Tank_Mecha = {
    "hp" : 80,
    "mspd" : 0.5,
    "aspd" : 3,
    "dmg" : 16,
    "bounty" : 96,
    "exp" : 96,
    "cost" : 60,
    "range" : 300,
    "img" : 'graphics/unit_tank/tank_scifi.png',
    "imgScale" : (390,391)
}

Ranged_Unit = {
    "hp" : 1,
    "mspd" : 3,
    "aspd" : 0,
    "dmg" : 0,
    "bounty" : 3,
    "exp" : 3,
    "cost" : 5,
    "range" : 200,
    "img" : 'graphics/unit_ranged/ranged_stickman.png',
    "imgScale" : (100,100)
}

Tank_Unit = {
    "hp" : 1,
    "mspd" : 1,
    "aspd" : 0,
    "dmg" : 0,
    "bounty" : 0,
    "exp" : 0,
    "cost" : 5,
    "range" : 130,
    "img" : 'graphics/unit_tank/tank_stickman.png',
    "imgScale" : (140,200)
}

UNITS = {
    "Caveman" : Melee_Caveman,
    "Footman" : Melee_Footman,
    "Soldier" : Melee_Soldier,
    "Robot" : Melee_Robot,
    "Slingshotter" : Ranged_Slingshotter,
    "Archer" : Ranged_Archer,
    "Sniper" : Ranged_Sniper,
    "Stormtrooper" : Ranged_Stormtrooper,
    "DinoRider" : Tank_DinoRider,
    "Cavalier" : Tank_Cavalier,
    "Tank" : Tank_Tank,
    "Mecha" : Tank_Mecha,
}


Base_Cave = {
    "hp" : 100,
    "expCost" : 300,
    "img" : 'graphics/bases/bases_prehistoric.png',
    "imgScale" : (400,400)
}
Base_Castle = {
    "hp" : 150,
    "expCost" : 500,
    "img" : 'graphics/bases/bases_medieval.png',
    "imgScale" : (400,400)
}
Base_Camp = {
    "hp" : 200,
    "expCost" : 700,
    "img" : 'graphics/bases/bases_modern_left.png',
    "imgScale" : (400,400)
}
Base_Citadel = {
    "hp" : 250,
    "expCost" : 99999,
    "img" : 'graphics/bases/bases_scifi.png',
    "imgScale" : (400,400)
}



BUILDINGS = {
    "Cave" : Base_Cave,
    "Castle" : Base_Castle,
    "Camp" : Base_Camp,
    "Citadel" : Base_Citadel
}

Stone = {
    "unit" : Ranged_Stoner,
    "img" : 'graphics/projectiles/stone.png',
    "imgScale" : (50,50)    
}

PROJECTILES = {
    "Stone" : Stone
}