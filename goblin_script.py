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

hodor.take_damage(11)