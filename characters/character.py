class Character(object):
	def __init(self,name,hp):
		self.name = name;
		self.hp = hp;
	def attack(attacker,victim):
		dmg = (5 * attacker.str) - (4 * victim.defense);
		victim.hp = victim.hp - dmg;

