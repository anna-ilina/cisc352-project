# CISC352 Artificial Intelligence
# Perceptron OR rule
# Assignment 4
# due April 4th 2017
# by Anna Ilina (10150979) and Jake Pittis (

import random

NUM_INPUTS = 4
LEARNING_RATE = 0.1

def createTestDataFile(filename, trainingData):
  with open(filename, 'w') as f:
    for testcase in trainingData:
      f.write("[")
      i = 0
      for i in range(NUM_INPUTS): # don't read the solution (last value in length 5 array)
        f.write(str(testcase[i]))
        if i != NUM_INPUTS - 1:
          f.write(" ")
      f.write("]\n\n")
  return


def createTrainingData():
  numTrainingSets = 2**NUM_INPUTS
  trainingData = [None] * (numTrainingSets) # each input has 2 options: 1 or 0
  i = 0
  for x1 in range(2):
    for x2 in range(2):
      for x3 in range(2):
        for x4 in range(2):
          orSolution = x1 or x2 or x3 or x4
          testcase = [x1, x2, x3, x4, orSolution]
          trainingData[i] = testcase
          i += 1
  return trainingData


def readDataFromFile(filename):
  with open(filename, 'r') as f:
    inputLinesFromFile = f.readlines()
  inputCases = []
  for line in inputLinesFromFile:
    if line != "" and line.isspace() == False: # skip blank lines
      inputSet = [None] * NUM_INPUTS
      i = 0
      for literal in line:
        if literal != "[" and literal != "]" and literal.isspace() == False:
          inputSet[i] = int(literal)
          i += 1
      inputCases.append(inputSet)
  return inputCases


def writeSolutionToFile(filename, solutionSet):
  with open(filename, 'w') as f:
    for solution in solutionSet:
      f.write("[")
      f.write(str(solution))
      f.write("]\n\n")
  return


def trainPerceptron(trainingData):

  # Initialize weights randomly
  weights = [None] * NUM_INPUTS
  for i in range(NUM_INPUTS):
    weights[i] = random.uniform(-1, 1)

  # Loop through the training dataset and adjust weights until the you get
  # through a run through the entire dataset with no incorrect classifications
  trainingComplete = False
  while trainingComplete == False:
    # Assume weights are good unless find a case where trained guess different from target
    trainingComplete = True

    for dataSet in trainingData:
      target = dataSet[NUM_INPUTS] # Last value is the correct 'OR' value

      # Compute answer (to use for Step Activation) using weights
      computed = 0
      for i in range(NUM_INPUTS):
        computed += weights[i] * dataSet[i]

      # Compute error
      error = float(target) - computed

      # Step activation: classify as 1 or 0 based on computed answer
      if computed > 0:
        computedAnswer = 1
      else:
        computedAnswer = 0

      # If classification incorrect, adjust weights
      if computedAnswer != target:
        trainingComplete = False
        for i in range(NUM_INPUTS):
          weights[i] += LEARNING_RATE * dataSet[i] * error

  print "done training"
  return weights

def classifyData(testCases, weights):
  solution = [None] * len(testCases)

  for j in range(len(testCases)):

    # Compute answer using weights (to be used for step activation)
    computed = 0
    for i in range(NUM_INPUTS):
      computed += weights[i] * testCases[j][i]

    # Step activation: classify as 1 or 0 based on computed answer
    if computed > 0:
      solution[j] = 1
    else:
      solution[j] = 0

  return solution


def main():

  testFile = "testFile.txt"
  inFile = "in.txt"
  outFile = "out.txt"

  #read tranining data from file
  trainingData = createTrainingData()

  print(trainingData)

  #train perceptrons to get weights
  weights = trainPerceptron(trainingData)

  # test that it's working - yes
  # createTestDataFile(testFile, trainingData)
  # testCases = readDataFromFile(testFile)
  # solution = classifyData(testCases, weights)
  # print testCases
  # print solution

  testCases = readDataFromFile(inFile)
  solution = classifyData(testCases, weights)
  writeSolutionToFile("out.txt", solution)

  print "solution output to \"out.txt\""

  return

if __name__ == "__main__":
  main()