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


def falchion(number):
	data = []
	for i in range(number):
		damage = 0
		attack_roll = roll(1,20)
		if attack_roll >= 19:
			damage += roll(2,10)
			data.append(damage)
		else:
			damage += roll(1,10)
			data.append(damage)
	return data

def greataxe(number):
	data = []
	for i in range(number):
		damage = 0
		attack_roll = roll(1,20)
		if attack_roll == 20:
			damage += roll(3,10)
			data.append(damage)
		else:
			damage += roll(1,10)
			data.append(damage)
	return data

falchion_data = falchion(500)
greataxe_data = greataxe(500)

print "Average Falchion Damage:", sum(falchion_data)/len(falchion_data)
print "Average Greataxe Damage:", sum(greataxe_data)/len(greataxe_data)