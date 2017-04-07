# ##
# You can and should use the Step activation function for the OR perceptron.
# Multilayer neural networks are trained using backpropagation. A requirement
# for backpropagation is a differentiable activation function due to its use of
# gradient descent to update the weights. The step function is not differentiable
# at x=0, and its derivative is 0 elsewhere; thus, gradient descent won't be able
# to update the weights and backpropagation will fail. The sigmoid function does
# not have this problem, so use it for the multilayer neural network.
#
# step activation function
#
# JUSTIN:
# perceptron is supervised, how will we decide that our output is expected, without
# any sort of target output given? Should we create our own expected array by
# examining if '1' is in the input?
#
# PROF:
# The picture I included in the assignment didn't include a bias because I didn't
# want you to use one for this, or Bias = 0, in other words.
# You will need to train your perceptron.

#in.txt() and out.txt()

import itertools

NUM_INPUTS = 4

def createTrainingDataFile():

  numTrainingSets = 2**NUM_INPUTS

  trainingData = [None] * (numTrainingSets) # each input has 2 options: 1 or 0

  #for i in range(numTrainingSets):
  #  pass

  i = 0
  for x1 in range(2):
    for x2 in range(2):
      for x3 in range(2):
        for x4 in range(2):
          input = [x1, x2, x3, x4]
          trainingData[i] = input
          i += 1

  print(trainingData)
  print(len(trainingData))


  # trainingData = [x for x in itertools.permutations('11110000', 4)]
  # print(len(trainingData))

  pass

def readDataFromFile():
  pass

def trainData():
  pass

def classifyData():
  pass

def writeSolutionToFile():
  pass


def main():

  #read tranining data from file
  createTrainingDataFile()

  #train perceptrons to get weights

  #use weights to classify input file

  #write classifications to file

  print ("curry")
  pass

if __name__ == "__main__":
  main()