import os
from obj.Roomcell import RoomCell
from obj.Map import Map

def loadMap():
	p = os.getcwd()
	map  = open(os.path.join(p,"Map.csv"), "r+")
	str = map.read()
	map = Map(str)
	return map