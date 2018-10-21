from obj.character import Character
from obj.Roomcell import RoomCell
from obj.Map import Map
import IOLoader

def test():
	pass

def start():
	print("Textgame\n")
	print("Good day, my friend! Would you like to LOAD a game or start aNEW?")
	getAction = input("Your descision: ")
	map = IOLoader.loadMap()
	#print(map.coordinates[1][1].content)
	
	pc = Character(1, 30, 2, 3, 4, 5, 6, map.getStart())
	#print (char.health)
	#char.addHealth(-20)
	#print (char.health)
	mainProcess(pc, map)
	test()
	
def action(pc, currentMap, key):
	return pc, currentMap
	
def movePC(pc, currentMap):
	pass

def refreshMap(pc, currentMap):
	pass
	
def getInput():
	return input ('Your action: ')
	
def refreshUI(pc, currentMap):
	pass
	
def mainProcess(pc, currentMap):
	active = True
	while(active):
		key = getInput()
		pc, currentMap = action(pc, currentMap,key)
		refreshUI(pc, currentMap)