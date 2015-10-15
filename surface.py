from impactor import Impactor
import random
import math
import matplotlib.pyplot as plt

class Surface(object):

	def __init__(self):
		self.impacts = []

	def randomImpact(self):
		rand = random.randint(0, 999)
		#print(rand)
		if(rand == 0):
			return True
		return False

	def createImpact(self, time):
		x = random.randint(0, 500)
		y = random.randint(0, 500)
		n = Impactor((x, y), time)
		self.impacts.append(n)

	#n is current object in list, n2 is new impactor
	def checkOblit(self):
		if(len(self.impacts) < 1):
			return
		n2 = self.impacts[len(self.impacts) - 1]
		for i in range(0, len(self.impacts) - 2):
			n = self.impacts[i]
			if(n.getOblit() < 0):
				if(self.inOblitRange(n.getLoc(), n2.getLoc())):
					n.setOblit(n2.getCreation())

	def inOblitRange(self, l1, l2):
		#do fucking math here
		x = abs(l1[0] - l2[0])
		y = abs(l1[1] - l2[1])
		if((x ** 2) + (y ** 2) < (30 ** 2)):
			return True
		else:
			return False

	def checkSaturation(self):
		length = len(self.impacts)
		if(length < 10):
			return True
		half = int(math.floor(length/2))
		t1 = self.impacts[half].getCreation()
		t2 = self.impacts[length - 1].getCreation()
		c1 = self.countCrators(t1)
		c2 = self.countCrators(t2)
		change = (abs(float(c2 - c1)))/c2
		print('{}, {}, {}'.format(c1, c2, change))
		if(change > 0.05):
			return True
		else:
			return False

	def countCrators(self, time):
		count = 0
		for i in self.impacts:
			if i.getCreation() > time:
				break
			if i.getOblit() < 0 or i.getOblit() > time:
				count += 1
		return count



if __name__ == "__main__":
	time = 0
		#change to check for saturation
	surf = Surface()
	surf.createImpact(0)
	while(1):
		if(surf.randomImpact()):
			surf.createImpact(time)
			surf.checkOblit()
			print('{}'.format(surf.countCrators(time)))
			if(not surf.checkSaturation()):
				break
		time += 1

	ti = []
	num = []
	for i in surf.impacts:
		print i
		ti.append(i.getCreation())
		num.append(surf.countCrators(ti[len(ti) - 1]))

	plt.plot(ti, num)
	plt.show()