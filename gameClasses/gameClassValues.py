'''
hp -> health points; how much damage a unit can take
mspd -> move speed; how fast a unit moves
aspd -> attack speed; how fast a unit attacks
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
    "exp" : 0
}
'''


Melee_Caveman = {
    "hp" : 3,
    "mspd" : 2,
    "aspd" : 5,
    "dmg" : 1,
    "bounty" : 1,
    "exp" : 1
}
Melee_Footman = {
    "hp" : 0,
    "mspd" : 0,
    "aspd" : 0,
    "dmg" : 0,
    "bounty" : 0,
    "exp" : 0
}
Melee_Soldier = {
    "hp" : 0,
    "mspd" : 0,
    "aspd" : 0,
    "dmg" : 0,
    "bounty" : 0,
    "exp" : 0
}
Melee_Robot = {
    "hp" : 0,
    "mspd" : 0,
    "aspd" : 0,
    "dmg" : 0,
    "bounty" : 0,
    "exp" : 0
}

UNITS = {
    "Caveman" : Melee_Caveman,
    "Footman" : Melee_Footman,
    "Soldier" : Melee_Soldier,
    "Robot" : Melee_Robot,
}