import random

# create a class of Goblins to kill
class Goblin(object):

	def __init__(self, name, max_health):

		self.name = name
		self.max_health = max_health
		self.current_health = self.max_health

	def take_damage(self, damage):
		
		self.current_health -= damage
		return self.current_health

# simulate polyhedral dice with optional bonuses
def roll(number, sides, bonus = 0):

	number_rolled = 0
	bonus_damage = number * bonus
	for i in range(number):
		number_rolled += random.randint(1, sides)
	return number_rolled + bonus_damage

# number of hits required to kill 1hd monster
def hits_to_kill_goblins(number_of_goblins, d8 = True):
	
	data = []
	# how many goblins to kill
	number_of_goblins = int(number_of_goblins)
	for i in range(number_of_goblins):
		hits_to_kill = 0
		# hp = 1d8+1
		victim = Goblin("Victim", roll.randint(1,8,1))
		while victim.current_health >= 1:
			# use 1d8 or 2d4?
			if d8 == True:
				victim.take_damage(roll(1,8))
				hits_to_kill += 1
			elif d8 == False:
				victim.take_damage(roll(2,4))
				hits_to_kill += 1
		# we want non decimals for later caldulations 2.9 hits is 2 hits
		data.append(int(hits_to_kill))
	return data

# run two simulations of 100 baddies
hits_per_kill_1d8 = hits_to_kill_goblins(100, d8 = True)
hits_per_kill_2d4 = hits_to_kill_goblins(100, d8 = False)


# make a dictonary of counts for each and display
_1d8_dict = {}
_2d4_dict = {}

for item in hits_per_kill_1d8:
	if item not in _1d8_dict:
		_1d8_dict[item] = 0
	_1d8_dict[item] += 1

for item in hits_per_kill_2d4:
	if item not in _2d4_dict:
		_2d4_dict[item] = 0
	_2d4_dict[item] += 1

print("1d8 data:")
print(_1d8_dict)
print("2d4 data:")
print(_2d4_dict)

