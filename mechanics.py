import random 

# simulate polyhedral dice with optional bonuses
def roll(number, sides, bonus = 0):

	number_rolled = 0
	bonus_damage = number * bonus
	for i in range(number):
		number_rolled += random.randint(1, sides)
	return number_rolled + bonus_damage