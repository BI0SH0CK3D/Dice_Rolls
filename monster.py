# create generic monster class outside of script
class Monster(object):

	def __init__(self, name, max_health):

		self.name = name
		self.max_health = max_health
		self.current_health = self.max_health

	def take_damage(self, amount):

		self.current_health -= amount
		return self.current_health


# simulate polyhedral dice with optional bonuses
def roll(number, sides, bonus = 0):

	number_rolled = 0
	bonus_damage = number * bonus
	for i in range(number):
		number_rolled += random.randint(1, sides)
	return number_rolled + bonus_damage

# print(roll(1,20,4))

# hodor = Monster("Hodor", 15)
# hodor.take_damage(roll(1,12))
# print hodor.current_health