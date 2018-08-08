import csv

def hypothesis(theta0, theta1, x):
	return theta0 + theta1 * x

def changeInRateOfCostFunction(xVals, yVals, theta0, theta1, learningRate, isTheta1):
		m = len(xVals)
		errorSum = 0
		for i in range(m):
			predection = hypothesis(theta0, theta1, xVals[i])
			if isTheta1:
				error = (predection - yVals[i]) * xVals[i]
			else:
				error = (predection - yVals[i])
			errorSum = errorSum + error
		if isTheta1:
			return (theta1 - ((learningRate/m)*errorSum))
		else:
			return (theta0 - ((learningRate/m)*errorSum))

def gradientDescent(x, y, theta0, theta1, learningRate):
	precision = 0.00001
	while True:
		theta0New =\
			changeInRateOfCostFunction(x, y, theta0, theta1, learningRate, False)
		theta1New =\
			changeInRateOfCostFunction(x, y, theta0, theta1, learningRate, True)
		if precision > abs(theta0 - theta0New) and precision > abs(theta1 - theta1New):
			break
		else:
			theta0 = theta0New
			theta1 = theta1New

	return theta0, theta1

if __name__ == "__main__":
	bioDiversityFile = open('biodiversity.csv', 'r')
	reader = csv.reader(bioDiversityFile)
	counter = 0
	typeOfPlants = []
	bioDiversity = []
	for row in reader:
		if counter > 0:
			typeOfPlants.append(int(row[0]))
			bioDiversity.append(int(row[1]))
		counter = counter + 1

	learningRate = 0.001

	print(gradientDescent(typeOfPlants, bioDiversity, 0, 0, learningRate))
