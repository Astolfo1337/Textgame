
class Character(object):
	def __init__ (self, level, maxhealth, stamina, attack, defense, acc, speed, coordinates):
		self.level = level
		self.health = [maxhealth, maxhealth]
		self.stamina = stamina
		self.attack = attack
		self.defense = defense
		self.acc = acc
		self.speed = speed
		self.coordinates = coordinates
		
	def addHealth(self, amount):
		temp = self.health[0] + amount
		if temp > self.health[1]:
			self.health[0] = self.health[1]
		else:
			self.health[0] = temp