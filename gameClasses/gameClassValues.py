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
    "img" : 'graphics\stickman.png'
}
'''


Melee_Caveman = {
    "hp" : 3,
    "mspd" : 2,
    "aspd" : 3,
    "dmg" : 1,
    "bounty" : 1,
    "exp" : 1,
    "img" : 'graphics\stickman.png'
}
Melee_Footman = {
    "hp" : 5,
    "mspd" : 2,
    "aspd" : 3,
    "dmg" : 2,
    "bounty" : 3,
    "exp" : 3,
    "img" : 'graphics\stickman.png'
}
Melee_Soldier = {
    "hp" : 8,
    "mspd" : 2,
    "aspd" : 3,
    "dmg" : 3,
    "bounty" : 9,
    "exp" : 9,
    "img" : 'graphics\stickman.png'
}
Melee_Robot = {
    "hp" : 12,
    "mspd" : 2,
    "aspd" : 3,
    "dmg" : 4,
    "bounty" : 27,
    "exp" : 27,
    "img" : 'graphics\stickman.png'
}

Ranged_Unit = {
    "hp" : 0,
    "mspd" : 0,
    "aspd" : 0,
    "dmg" : 0,
    "bounty" : 0,
    "exp" : 0,
    "img" : 'graphics\stickman.png'
}

Tank_Unit = {
    "hp" : 0,
    "mspd" : 0,
    "aspd" : 0,
    "dmg" : 0,
    "bounty" : 0,
    "exp" : 0,
    "img" : 'graphics\stickman.png'
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
    "DinoRider" : Tank_Unit,
    "Cavalier" : Tank_Unit,
    "Tank" : Tank_Unit,
    "Mecha" : Tank_Unit,
}