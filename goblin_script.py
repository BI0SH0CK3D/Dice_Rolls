import random

def _2d4():
	damage = random.randint(1,4) + random.randint(1,4)
	#print "2d4:", damage
	return damage

class goblin(object):

	def __init__(self, name, max_health, current_health):

		self.name = name
		self.max_health = max_health
		self.current_health = current_health

	def take_damage(self, damage):

		self.current_health -= damage
		print "%s takes %s damage, %s hp remaining" % (self.name, damage, self.current_health)
		if self.current_health <= 0:
			print "%s is dead" % self.name


hodor = goblin("Hodor", 10, 10)

hits_to_kill = 0

print "Attacking goblin..."
print "%s has %s hp" %(hodor.name, hodor.current_health)

while hodor.current_health >= 1:
	hodor.take_damage(_2d4())
	print "%s has %s hp left" %(hodor.name, hodor.current_health)
	hits_to_kill += 1
print hits_to_kill, "hits to kill the goblin"