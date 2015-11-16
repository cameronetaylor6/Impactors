from impactor import Impactor
import random
import math
import matplotlib.pyplot as plt

class Surface(object):

	def __init__(self):
		self.impacts = []

	#determines if an impact occurs
	def randomImpact(self):
		rand = random.randint(0, 999)
		if(rand == 0):
			return True
		return False

	#creates an impact at designated time with random coordinates
	def createImpact(self, time):
		x = random.randint(0, 500)
		y = random.randint(0, 500)
		n = Impactor((x, y), time)
		self.impacts.append(n)

	#checks all intact craters to see if they are destroyed by a new impact
	#n is current object in list, n2 is new impactor
	def checkOblit(self):
		n2 = self.impacts[len(self.impacts) - 1]
		for i in range(0, len(self.impacts) - 2):
			n = self.impacts[i]
			if(n.getOblit() < 0):
				if(self.inOblitRange(n.getLoc(), n2.getLoc())):
					n.setOblit(n2.getCreation())

	#pythagorean theorem for checking distances from center to center
	def inOblitRange(self, l1, l2):
		x = abs(l1[0] - l2[0])
		y = abs(l1[1] - l2[1])
		if((x ** 2) + (y ** 2) < (30 ** 2)):
			return True
		else:
			return False

	#checks if saturation has occured (less than 5% change in number of intact craters in double the time)
	def checkSaturation(self):
		length = len(self.impacts)
		#edge case with small amounts of impacts
		if(length < 10):
			return True
		half = int(math.floor(length/2))
		t1 = self.impacts[half].getCreation()
		t2 = self.impacts[length - 1].getCreation()
		c1 = self.countCraters(t1)
		c2 = self.countCraters(t2)
		change = (abs(float(c2 - c1)))/c2
		if(change > 0.05):
			return True
		else:
			return False

	#returns the number of intact craters at specified time
	def countCraters(self, time):
		count = 0
		for i in self.impacts:
			if i.getCreation() > time:
				break
			if i.getOblit() < 0 or i.getOblit() > time:
				count += 1
		return count

	#returns the number of obliterated craters at specified time
	def countOblit(self, time):
		count = 0
		for i in self.impacts:
			if i.getCreation() > time:
				break
			if i.getOblit() >= 0 and i.getOblit() <= time:
				count += 1
		return count

	#returns the total number of craters at specified time
	def countTotal(self, time):
		count = 0
		for i in self.impacts:
			if i.getCreation() > time:
				break
			count += 1
		return count

if __name__ == "__main__":
	time = 0
	surf = Surface()
	surf.createImpact(0)
	x = []
	y = []
	
	while(1):
		if(surf.randomImpact()):
			surf.createImpact(time)
			surf.checkOblit()
			if(not surf.checkSaturation()):
				break
		#record coordinates for plotting crater grid
		if(time % 50000 == 0):
			x2 = []
			y2 = []
			for imp in surf.impacts:
				if(imp.getOblit() < 0):
					x2.append(imp.getLoc()[0])
					y2.append(imp.getLoc()[1])

			x.append(x2)
			y.append(y2)

		time += 1

	#plot the crater grids scatter
	for i in range(1, len(x)/2):
		plt.title("Intact Impact Craters after " + str(i*50) + ",000 years")
		plt.xlabel("x")
		plt.ylabel("y")
		plt.axis([0, 500, 0, 500])
		plt.scatter(x[i], y[i], s=1250)
		plt.scatter(x[i], y[i], s=15, c = "red")
		plt.savefig("output" + str(i) + ".jpg")
		plt.clf()

	#arrays keeping track of time and number of craters for line plots
	ti = []
	intact = []
	oblit = []
	total = []
	for i in range(0, int(math.floor(len(surf.impacts) /2))):
		ti.append(surf.impacts[i].getCreation())
		intact.append(surf.countCraters(ti[len(ti) - 1]))
		oblit.append(surf.countOblit(ti[len(ti) - 1]))
		total.append(surf.countTotal(ti[len(ti) - 1])) 

	for i in surf.impacts:
		print i

	#plotting the line graph
	plt.title("Surface Cratering Simulation")
	plt.xlabel("Time (Years)")
	plt.ylabel("Number of Craters")
	plt.figtext(.138, .86, "Time to saturation: " + str(time/2) + " years.")
	plt.figtext(.138, .83, "Intact craters: " + str(surf.countCraters(ti[len(ti) - 1])) + ".")
	plt.figtext(.138, .80, "Total obliterations: " + str(surf.countOblit(ti[len(ti) - 1])) + ".")
	plt.figtext(.138, .77, "Total impacts: " + str(surf.countTotal(ti[len(ti) - 1])) + ".")
	plt.plot(ti, intact, label = "Intact craters", linewidth = 2)
	plt.plot(ti, oblit, label = "Obliterated craters", linewidth = 2)
	plt.plot(ti, total, label = "Total craters", linewidth = 2)
	plt.legend(loc = 4)
	plt.savefig("results.jpg")