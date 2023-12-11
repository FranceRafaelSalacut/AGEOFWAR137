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
    "img" : 'graphics\stickman.png'
    "imgScale" : (100,100) # width, height
}
'''


Melee_Caveman = {
    "hp" : 3,
    "mspd" : 2,
    "aspd" : 5,
    "dmg" : 1,
    "bounty" : 1,
    "exp" : 1,
    "cost" : 5,
    "img" : 'graphics/unit_melee/stickman.png',
    "imgScale" : (100,100)
}
Melee_Footman = {
    "hp" : 5,
    "mspd" : 2,
    "aspd" : 5,
    "dmg" : 2,
    "bounty" : 3,
    "exp" : 3,
    "cost" : 5,
    "img" : 'graphics/stickman.png',
    "imgScale" : (100,100)
}
Melee_Soldier = {
    "hp" : 8,
    "mspd" : 2,
    "aspd" : 5,
    "dmg" : 3,
    "bounty" : 9,
    "exp" : 9,
    "cost" : 5,
    "img" : 'graphics/stickman.png',
    "imgScale" : (100,100)
}
Melee_Robot = {
    "hp" : 12,
    "mspd" : 2,
    "aspd" : 5,
    "dmg" : 4,
    "bounty" : 27,
    "exp" : 27,
    "cost" : 5,
    "img" : 'graphics/stickman.png',
    "imgScale" : (100,100)
}


Tank_DinoRider = {
    "hp" : 30,
    "mspd" : 2,
    "aspd" : 3,
    "dmg" : 10,
    "bounty" : 1,
    "exp" : 1,
    "cost" : 5,
    "img" : 'graphics/unit_tank/tank_stickman.png',
    "imgScale" : (140,200)
}

Ranged_Unit = {
    "hp" : 1,
    "mspd" : 3,
    "aspd" : 0,
    "dmg" : 0,
    "bounty" : 0,
    "exp" : 0,
    "cost" : 5,
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
    "img" : 'graphics/unit_tank/tank_stickman.png',
    "imgScale" : (140,200)
}

UNITS = {
    "Caveman" : Melee_Caveman,
    "Footman" : Melee_Footman,
    "Soldier" : Melee_Soldier,
    "Robot" : Melee_Robot,
    "Slingshotter" : Ranged_Unit,
    "Archer" : Ranged_Unit,
    "Sniper" : Ranged_Unit,
    "Stormtrooper" : Ranged_Unit,
    "DinoRider" : Tank_DinoRider,
    "Cavalier" : Tank_Unit,
    "Tank" : Tank_Unit,
    "Mecha" : Tank_Unit,
}


Base_Cave = {
    "hp" : 30,
    "expCost" : 100,
    "img" : 'graphics/bases/cave.png',
    "imgScale" : (100,100)
}
Base_Castle = {
    "hp" : 40,
    "expCost" : 100,
    "img" : 'graphics/bases/cave.png',
    "imgScale" : (100,100)
}
Base_Camp = {
    "hp" : 50,
    "expCost" : 100,
    "img" : 'graphics/bases/cave.png',
    "imgScale" : (100,100)
}
Base_Citadel = {
    "hp" : 60,
    "expCost" : 100,
    "img" : 'graphics/bases/cave.png',
    "imgScale" : (100,100)
}



BUILDINGS = {
    "Cave" : Base_Cave,
    "Castle" : Base_Castle,
    "Camp" : Base_Camp,
    "Citadel" : Base_Citadel
}

Stone = {
    "vx" : 0,
    "vy" : 0,
    "img" : 'graphics/projectiles/stone.png',
    "imgScale" : (50,50)    
}

PROJECTILES = {
    "Stone" : Stone
}