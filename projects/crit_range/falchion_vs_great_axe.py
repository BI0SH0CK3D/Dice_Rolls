""" 
This script aims to compare the average damage produced by a 1d10 weapon
that deals 3x critical damage on a 20 vs 2x critital damage on a 19 or 20.
The critical results in rolling proportionate amounts of additional dice, 
not multiplyng the results by the crit factor. i.e a 2x crit deals 2 dice
of 1-10 damage, not one roll of 1-10 and multiplying by 2
"""

import random 


def roll(number, sides, bonus = 0):

	number_rolled = 0
	bonus_damage = number * bonus
	for i in range(number):
		number_rolled += random.randint(1, sides)
	return number_rolled + bonus_damage


# create weapon class that takes
def weapon(number, weapon): 
    data = []
    
    # choose weapon - two dice on a 19-20 or three on only a 20
    if weapon == "Falchion" or 'Falchion':
        crit_min = 19
        crit_dice = 2
    elif weapon == "Greataxe" or 'greataxe':
        crit_min = 20
        crit_dice = 3
        
    # make an attack for each number in range
    for i in range(number):
        damage = 0
        attack_roll = roll(1,20)
        
        # if it is a critical hit, adjust damage acordingly
        if attack_roll >= crit_min:
            damage += roll(crit_dice, 10)
            data.append(damage)
        else:
            damage += roll(1,10)
            data.append(damage)
    return data

falchion_data = weapon(100000, "Falchion")
greataxe_data = weapon(100000, "Greataxe")

print("Average Falchion Damage:", sum(falchion_data)/len(falchion_data))
print("Average Greataxe Damage:", sum(greataxe_data)/len(greataxe_data))
