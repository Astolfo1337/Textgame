
from obj.Roomcell import RoomCell

class Map(object):
	def __init__(self, strMap):
		self.coordinates = self.convertToMap(strMap)

	def convertToMap(self, strMap):
		lines = strMap[5:][:-1].split("\n")
		map = []
		for l in lines:
			row = l.split(";")
			resRow = []
			for r in row:
				resRow.append(self.convertToRoom(r))
			map.append(resRow)
		return map
		
	def convertToRoom(self, strRoom):
		return RoomCell(strRoom)
	
	def getStart(self):
		x = 0
		
		for row in self.coordinates:
			y = 0
			for col in row:
				if col.content == "s":
					return [y,x]
				y += 1
			x += 1
		return [0,0]