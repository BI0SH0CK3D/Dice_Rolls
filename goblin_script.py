#python3
"""
Rough draft of a model to find any significance in damage output using a 1d8 vs. 2d4 weapon.
I am will examine average damage, how often one does more damage than the other, how often they
tie and number of hits required to kill various monsters.

I will probably turn the rolls into a class called Roll for the hell of it, add PEP8 considerations 
and
"""
import random


class Goblin(object):

	def __init__(self, name, max_health):

		self.name = name
		self.max_health = max_health
		self.current_health = self.max_health

	def take_damage(self, damage):
		self.current_health -= damage
		# print "%s takes %s damage, %s hp remaining" % (self.name, damage, self.current_health)
		#if self.current_health <= 0:
			# print "%s is dead" % self.name
		return self.current_health

def _2d4():
	damage = random.randint(1,4) + random.randint(1,4)
	#print "2d4:", damage
	return int(damage)

def _1d8():
	damage = random.randint(1,8)
	#print "1d8:", damage
	return damage

# number of hits required to kill 1hd monster
def kill_goblins(number_of_goblins, d8 = True):
	data = []
	number_of_goblins = int(number_of_goblins)
	for i in range(number_of_goblins):
		hits_to_kill = 0
		victim = Goblin("Victim", random.randint(2,9))
		while victim.current_health >= 1:
			#print "HP", victim.current_health 
			if d8 == True:
				victim.take_damage(_1d8())
				hits_to_kill += 1
			elif d8 == False:
				victim.take_damage(_2d4())
				hits_to_kill += 1
		#print hits_to_kill
		data.append(int(hits_to_kill))
	return data


hits_per_kill_1d8 = kill_goblins(500000, d8 = True)
hits_per_kill_2d4 = kill_goblins(500000, d8 = False)

# print("1d8", sum(hits_per_kill_1d8)/len(hits_per_kill_1d8))
# print("2d4", sum(hits_per_kill_2d4)/len(hits_per_kill_2d4))

d8_dict = {}
d4_dict = {}

for item in hits_per_kill_1d8:
	if item not in d8_dict:
		d8_dict[item] = 0
	d8_dict[item] += 1

for item in hits_per_kill_2d4:
	if item not in d4_dict:
		d4_dict[item] = 0
	d4_dict[item] += 1

print d8_dict
print d4_dict