from obj.character import Character
from obj.Roomcell import RoomCell
from obj.Map import Map
import IOLoader

def start():
	map = IOLoader.loadMap()
	#print(map.coordinates[1][1].content)
	
	pc = Character(1, 30, 2, 3, 4, 5, 6, map.getStart())
	#print (char.health)
	#char.addHealth(-20)
	#print (char.health)
	test()
	
def test():
	pass