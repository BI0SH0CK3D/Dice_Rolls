"""
Rough draft of a model to find any significance in damage output using a 1d8 vs. 2d4 weapon.
I am will examine average damage, how often one does more damage than the other, how often they
tie and number of hits required to kill various monsters.

I will probably turn the rolls into a class called Roll for the hell of it, add PEP8 considerations 
and remove the current redundancies in the kill functions (though I am not sure how)
"""

from __future__ import division
import random



class goblin(object):

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

def kill_goblins_1d8(number_of_goblins):
	data = []
	number_of_goblins = int(number_of_goblins)
	for i in range(number_of_goblins):
		hits_to_kill = 0
		victim = goblin("Victim", random.randint(2,9))
		while victim.current_health >= 1:
			#print "HP", victim.current_health 
			victim.take_damage(_1d8())
			hits_to_kill += 1
		#print hits_to_kill
		data.append(hits_to_kill)
	return data


def kill_goblins_2d4(number_of_goblins):
	data = []
	number_of_goblins = int(number_of_goblins)
	for i in range(number_of_goblins):
		hits_to_kill = 0
		victim = goblin("Victim", random.randint(2,9))
		while victim.current_health >= 1:
			#print "HP", victim.current_health 
			victim.take_damage(_2d4())
			hits_to_kill += 1
		#print hits_to_kill
		data.append(hits_to_kill)
	return data
		#while victim.current_health >= 1:
			#victim.take_damage(str(_2d4()))

hits_per_kill_1d8 = kill_goblins_1d8(10)
hits_per_kill_2d4 = kill_goblins_2d4(10)

print "1d8", sum(hits_per_kill_1d8)/len(hits_per_kill_1d8)
print "2d4", sum(hits_per_kill_2d4)/len(hits_per_kill_2d4)
