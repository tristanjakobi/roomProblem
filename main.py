class Vertex:

	def __init__(self, x, y, facesList):
		self.x = x
		self.y = y
		self.facesList = facesList


class Face:
	def __init__(self, aVertex, bVertex, cVertex):
		self.aVertex = aVertex
		self.bVertex = bVertex
		self.cVertex = cVertex

class Line:
	def __init__(self, aVertex, bVertex):
		self.aVertex = aVertex
		self.bVertex = bVertex


@staticmethod
def linesIntersect(lineA, lineB):
	#lineares gleichungssystem
	