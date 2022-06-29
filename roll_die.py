# -*- coding: utf-8 -*-
"""
Created on Sun May 22 18:54:08 2022

@author: Krystyna
"""

import random, pylab

def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, numBins) 
    if title:
        pylab.title(title) 
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel) 
    pylab.show()
    
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    list_long = []

    for i in range(numTrials):
        last = 0
        x = 1
        longest = 0
        for j in range(numRolls):
            roll = die.roll()
            if roll == last:
                x += 1
            elif x > longest:
                longest = x
                x = 1
            else:
                x = 1
            last = roll
        list_long.append(longest)
        
    mean, std = getMeanAndStd(list_long)
    
    makeHistogram(list_long, 10, "mean longest run", "number of trials", title=None)
    
    return mean
    
# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))
print(getAverage(Die([1,1]), 10, 1000))
