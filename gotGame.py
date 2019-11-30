from time import sleep
import random
from os import system

class Hero:

	def __init__(self,house_name,name,gender,petname,health,defense,damage,hit_probability,gold,winGold,pet):
		self.house_name = house_name
		self.name = name
		self.gender = gender
		self.petname = petname
		self.health = health
		self.defense = defense
		self.damage = damage
		self.hit_probability = hit_probability
		self.gold = gold
		self.winGold = winGold
		self.pet = pet

	def getHouse_Name(self):
		return self.house_name

	def getName(self):
		return self.name

	def getGender(self):
		return self.gender

	def getPetName(self):
		return self.petname

	def getDamage(self):
		return self.damage

	def getDefense(self):
		return self.defense

	def getHit_probability(self):
		return self.hit_probability

	def getPet(self):
		return self.pet

	def getHealth(self):
		return self.health

	def setHealth(self,health):
		self.health = health

	def getGold(self):
		return self.gold

	def setGold(self,gold):
		self.gold = gold

	def getWinGold(self):
		return self.winGold

class Enemy:

	def __init__(self,house_name,name,health,defense,damage,hit_probability):
		self.house_name = house_name
		self.name = name
		self.health = health
		self.defense = defense
		self.damage = damage
		self.hit_probability = hit_probability

	def getHouse_Name(self):
		return self.house_name

	def getName(self):
		return self.name

	def getDamage(self):
		return self.damage

	def getDefense(self):
		return self.defense

	def getHit_probability(self):
		return self.hit_probability

	def getHealth(self):
		return self.health

	def setHealth(self,health):
		self.health = health

class Main:

	def __init__(self):
		self.game = Game()

	def start(self):
		self.menu()

	def menu(self):
		intro = """
		$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
		$                                 $
		$ <The Quest For The Iron Throne> $
		$                                 $
		$ 1) Play                         $
		$ 2) How To Play                  $
		$ 0) Exit                         $
		$                                 $
		$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""
		
		hwtplay = """
		Select a House name a hero and pet then fight for IRON THRONE!!!
		!!!VALAR DOHAERIS!!!"""
		
		while(True):
			self.game.clear()
			print(intro)
			choice = str(input(">"))
			if(choice in ["1","2","0"]):
				if(choice == "1"):
					self.game.start()
				elif(choice == "2"):
					print(hwtplay)
					input("Press any key to continue...")
				else:
					break

class Game:

	def __init__(self):
		self.lannister = ["Tywin Lannister", 90, 0.80, 25, 0.50, 200, "Lion"]
		self.stark = ["Arya Stark", 100, 0.80, 40, 0.40, 50, "Direwolf"]
		self.targeryan = ["Daenerys Targaryen", 90, 0.90, 40, 0.60, 150, "Dragon"]
		self.arryn = ["Robin Arryn", 85, 0.95, 35, 0.50, 175, "Falcon"]
		self.baratheon = ["Stannis Baratheon", 95, 0.85, 50, 0.50, 100, "Stag"]
		self.greyjoy = ["Euron Greyjoy", 85, 0.95, 25, 0.50, 60, "Kraken"]
		self.martell = ["Oberyn Martell", 80, 0.85, 45, 0.50, 125, "Sand Snake"]
		self.tully = ["Edmure Tully", 90, 0.95, 35, 0.40, 125, "Trout"]
		self.tyrell = ["Loras Tyrell", 90, 0.90, 40, 0.50, 150, "Horse"]
		self.houses = [self.lannister,self.stark,self.targeryan,self.arryn,self.baratheon,self.greyjoy,self.martell,self.tully,self.tyrell]
		self.isPetAlive = True
		self.hero = None
		self.enemy = None
		self.gameover = False

	def setHero(self,hero):
		name = str(input("Rename hero:"))
		while(name == ""):
			name = str(input("Rename hero:"))
		gender = str(input("Enter Gender(Male/Female/Others):"))
		while(gender == ""):
			gender = str(input("Enter Gender(Male/Female/Others):"))
		petname = str(input("Rename pet:"))
		while(petname == ""):
			petname = str(input("Rename pet:"))
		self.hero = Hero(hero[0].split(" ")[1].upper(),name,gender,petname,100,hero[2],hero[3],hero[4],100,hero[5],hero[6])
		self.houses.remove(hero)
		self.levels()

	def setEnemy(self):
		self.clear()
		index = random.randint(0,len(self.houses)-1)
		enemy = self.houses[index]
		stat = "Your Enemy\nName:{}\nHealth:{}\nDefense:{}\nDamage:{}\nHit Probability:{}\n".format(enemy[0],enemy[1],enemy[2],enemy[3],enemy[4])
		print(stat)
		self.houses.remove(enemy)
		self.enemy = Enemy(enemy[0].split(" ")[1].upper(),enemy[0],enemy[1],enemy[2],enemy[3],enemy[4])

	def isInt(self,var):
		try:
			var = int(var)
			return True
		except:
			print("Enter Integer")
			return False

	def purchaseHealth(self):
		print("\nYour Health:",self.hero.getHealth())
		print("Your Gold:",self.hero.getGold())
		choice = str(input("Purchase Health (1 Gold = 1 Health) (y/n):"))
		if(choice in ["y","n"]):
			if(choice == "y"):
				amount = str(input("Enter amount:"))
				while(not self.isInt(amount)):
					amount = str(input("Enter amount:"))
				amount = int(amount)
				if(amount > self.hero.getGold()):
					amount = self.hero.getGold()
					self.hero.setGold(0)
				else:
					self.hero.setGold(self.hero.getGold() - amount)
				self.hero.setHealth(self.hero.getHealth() + amount)
				if(self.hero.getHealth() > 100):
					amount = self.hero.getHealth() - 100
					self.hero.setGold(self.hero.getGold() + amount)
					self.hero.setHealth(100)

	def levels(self):
		for level in range(8):
			self.setEnemy()
			input("Continue Stage...")
			self.clear()
			print("Stage",(level+1))
			print("<><><><><><>")
			print("Hero Status")
			herostatu = "Name:{}\nGender:{}\nHealth:{}\nGold:{}\nPet Name:{}\nIs Pet Alive:{}\n\n".format(self.hero.getName(),self.hero.getGender(),self.hero.getHealth(),self.hero.getGold(),self.hero.getPetName(),self.isPetAlive)
			print(herostatu)
			stat = "|Hero Health:{} |--------| Enemy Health:{}|\n".format(self.hero.getHealth(),self.enemy.getHealth())
			print(stat)
			while(True):
				self.fight()
				if(self.hero.getHealth() <= 0):
					if(self.isPetAlive):
						print("Your pet sacrifices itself for you...")
						self.enemy.setHealth(0)
						self.hero.setHealth(100)
						self.isPetAlive = False
					else:
						print("Game Over")
						self.refresh()
						break
				if(self.enemy.getHealth() <= 0):
					print("You kill the enemy...")
					self.hero.setGold(self.hero.getGold() + self.hero.getWinGold())
					break
			if(self.gameover):
				break
			if(level == 7):
				print("You reach the IRON THRONE!!!\n!!!VALAR DOHAERIS!!!")
				self.refresh()
				break
			self.purchaseHealth()
		if(self.gameover):
			input("Return Hero Selection")
			self.gameover = False

	def refresh(self):
		self.gameover = True
		self.houses = [self.lannister,self.stark,self.targeryan,self.arryn,self.baratheon,self.greyjoy,self.martell,self.tully,self.tyrell]
		self.isPetAlive = True

	def fight(self):
		enemyProb = random.randint(1,100)
		heroProb = random.randint(1,100)
		if(enemyProb <= 100*self.enemy.getHit_probability()):
			self.hero.setHealth(self.hero.getHealth() - (self.enemy.getDamage()*self.hero.getDefense()))
			stat = "{}({}) ==>> {}({})".format(self.enemy.getName(),self.enemy.getHealth(),self.hero.getName(),self.hero.getHealth())
			print(stat)
		if(heroProb <= 100*self.hero.getHit_probability()):
			self.enemy.setHealth(self.enemy.getHealth() - (self.hero.getDamage()*self.enemy.getDefense()))
			stat = "{}({}) ==>> {}({})".format(self.hero.getName(),self.hero.getHealth(),self.enemy.getName(),self.enemy.getHealth())
			print(stat)
		if(enemyProb > 100*self.enemy.getHit_probability() and heroProb > 100*self.hero.getHit_probability()):
			print("No body hits")
		print()
		sleep(1)

	def start(self):
		selection = ">-Hero Selection-<"
		while(True):
			self.clear()
			print(selection)
			for index,name in enumerate(self.houses):
				print(str((index+1))+") " + name[0].split(" ")[1].upper())
			print("0) Back")
			choice = str(input(">"))
			if(choice in ["1","2","3","4","5","6","7","8","9"]):
				if(choice == "1"):
					if(self.showHeroOptions(self.lannister)):
						self.setHero(self.lannister)
				elif(choice == "2"):
					if(self.showHeroOptions(self.stark)):
						self.setHero(self.stark)
				elif(choice == "3"):
					if(self.showHeroOptions(self.targeryan)):
						self.setHero(self.targeryan)
				elif(choice == "4"):
					if(self.showHeroOptions(self.arryn)):
						self.setHero(self.arryn)
				elif(choice == "5"):
					if(self.showHeroOptions(self.baratheon)):
						self.setHero(self.baratheon)
				elif(choice == "6"):
					if(self.showHeroOptions(self.greyjoy)):
						self.setHero(self.greyjoy)
				elif(choice == "7"):
					if(self.showHeroOptions(self.martell)):
						self.setHero(self.martell)
				elif(choice == "8"):
					if(self.showHeroOptions(self.tully)):
						self.setHero(self.tully)
				elif(choice == "9"):
					if(self.showHeroOptions(self.tyrell)):
						self.setHero(self.tyrell)
			elif(choice == "0"):
				break

	def showHeroOptions(self,hero):
		while(True):
			self.clear()
			print("HOUSE OF",hero[0].split(" ")[1].upper())
			print("House Hero:",hero[0])
			print("Starting Health:",hero[1])
			print("Hit Defense:",hero[2])
			print("Hit Damage:",hero[3])
			print("Hit Probability:",hero[4])
			print("Gold:",hero[5])
			print("Pet:",hero[6])
			choice = str(input("select(y/n):"))
			if(choice in ["y","n"]):
				if(choice == "y"):
					return True
				else:
					return False

	def clear(self):
		system("cls")

def main():
	system("color a")
	game = Main()
	game.start()

main()