import sys

class Impactor(object):

	def __init__(self, location, time):
		if not isinstance(time, int):
			print "Time is not an integer. Please use an integer."
			raise TypeError
		if not isinstance(location[0], int):
			print "Value is not an integer. Please use an integer."
			raise TypeError
		if not isinstance(location[1], int):
			print "Value is not an integer. Please use an integer."
			raise TypeError

		#tuple of x, y coordinates
		self.loc = location
		#time created
		self.creation = time
		#-1 if not destroyed, otherwise time destroyed
		self.obliterated = -1

	def getLoc(self):
		return self.loc

	def getCreation(self):
		return self.creation

	def getOblit(self):
		return self.obliterated

	def setOblit(self, time):
		if not isinstance(time, int):
			print "Time is not an integer. Please use an integer."
			raise TypeError
		self.obliterated = time

	def __str__(self):
		if(self.obliterated < 0):
			return ("Location:" + str(self.loc) + ". Time Created: " + str(self.creation) + ". Is still intact.")
		else:
			return ("Location:" + str(self.loc) + ". Time Created: " + str(self.creation) + ". Obliterated at:" + str(self.obliterated) + ".")

if __name__ == "__main__":
	dingus = Impactor((1,2), 50)
	dodongo = Impactor((4, 1), 100)
	print(dingus)
	print(dodongo)
	dingus.setOblit(100)
	print(dingus)
	print(dodongo)