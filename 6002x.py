#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:04:38 2019

@author: salmaalsinan
"""


#Knapsack problem 
%Greedy algorith

class Food(object):
      def __init__(self,n,v,w):
          self.name=n
          self.value=v
          self.calories=w
        
      def getValue(self):
          return self.value
        
      def getCost(self):
          return self.calories
        
      def density(self):
          return self.getValue()/self.getCost()
        
      def __str__ (self):
        
          return self.name +':<'+str(self.value)\
                  +', ' +str(self.calories) + '>'
                    

def buildMenue(names, values, calories):
 
    menu=[]
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                         calories[i]))
        
    return menu


def greedy(items,maxCost, KeyFunction):
    
    itemsCopy= sorted(items,key=KeyFunction,
                      reverse= True)
    
    result=[]
    totalValue,totalCost =0.0,0.0
    
    for i in range (len(itemsCopy)):
        if (totalCost +itemsCopy[i].getCost())<=maxCost:
            result.append(itemsCopy[i])
            totalCost +=itemsCopy[i].getCost()
            totalValue +=itemsCopy[i].getValue()
            
    return(result, totalValue)
    
    
def testGreedy (items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    
    print('Total value of items taken =', val)
    
    for item in taken:
        print('  ',item)


def testGreedys(foods,maxUnits):
    print('use greedy by value to allocate', maxUnits,
          calories)
    testGreedy(foods,maxUnits,Food.getValue)
    print('\nUse greedy by cost to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, 
               lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate', maxUnits,
          'calories')
    testGreedy(foods,maxUnits,Food.density)
    
names= ['wine', 'beer', 'pizza', 'burger','fries','cola','apple','donut','cake']

values=[89,90,95,100,90,79,50,10]

calories= [123,154,258,354,365,150,95,195]

foods= buildMenue(names,values,calories)

testGreedys(foods,750)

testGreedys(foods,1000)
      
        #--------------#

#Disicion Trees


def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the items of that solution"""
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        #Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getCost())
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def testMaxVal(foods, maxUnits, printItems = True):
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = maxVal(foods, maxUnits)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)

testGreedys(foods, 750)
print('')
testMaxVal(foods, 750)


import random

def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i),
                          random.randint(1, maxVal),
                          random.randint(1, maxCost)))
    return items

for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45):
    print('Try a menu with', numItems, 'items')
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal(items, 750, False)
#    
    

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

#for i in range(121):
#    print('fib(' + str(i) + ') =', fib(i))


def fastFib(n, memo = {}):
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result

for i in range(121):
    print('fib(' + str(i) + ') =', fastFib(i))

%--------------%
   return menu

def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
       Returns a tuple of the total weight of a solution to the
         0/1 knapsack problem and the items of that solution"""
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        #Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getCost())
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

import random

def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i),
                          random.randint(1, maxVal),
                          random.randint(1, maxCost)))
    return items

def fastMaxVal(toConsider, avail, memo = {}):
    """Assumes toConsider a list of subjects, avail a weight
         memo supplied by recursive calls
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the subjects of that solution"""
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        #Explore right branch only
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake =\
                 fastMaxVal(toConsider[1:],
                            avail - nextItem.getCost(), memo)
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:],
                                                avail, memo)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result

def testMaxVal(foods, maxUnits, algorithm, printItems = True):
    print('Menu contains', len(foods), 'items')
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = algorithm(foods, maxUnits)
    if printItems:
        print('Total value of items taken =', val)
        for item in taken:
            print('   ', item)
            
#for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50):
#    items = buildLargeMenu(numItems, 90, 250)
#    testMaxVal(items, 750, maxVal, False)
    
#Change code to keep track of number of calls
def countingFastMaxVal(toConsider, avail, memo = {}):
    """Assumes toConsider a list of subjects, avail a weight
         memo supplied by recursive calls
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the subjects of that solution"""
    global numCalls
    numCalls += 1
    
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        #Explore right branch only
        result = countingFastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake =\
                 countingFastMaxVal(toConsider[1:],
                            avail - nextItem.getCost(), memo)
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = countingFastMaxVal(toConsider[1:],
                                                avail, memo)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result
    
for numItems in (2, 4, 8, 16, 32, 64, 128, 256, 512, 1024):
    numCalls = 0
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal(items, 750, countingFastMaxVal, False)
    print('Number of calls =', numCalls)

#-----------#
class Node(object):
    def __init__(self,name):
        self.name=name
    
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__ (self,src, dest):
        self.stc = src
        self.dest=dest
    
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    
    def __str__(self):
        return self.src.getName() + '->' \
                +self.dest.getName()
                
class Digraph(object):
    
    def __init__(self):
        self.edge ={}
        
    def addNode(self,node):
        
        if node in self:
            raise ValueError('Duplicate Node')
            
        else:
            self.edges[node] =[]
            
    def addEdge(self,edge):
        src = edge.getSource()
        dest =edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError ('node not in graph')
        self.edges[src].append(dest)
    
    def children0f(self,node):
        return self.edges[node]
    
    def hasNode(slef,node):
        return node in self.edges
    
    def getNode(self,name):
        for n in self.edges:
            if n.getName()== name:
                return n
        raise NameError(name)
        
    def __str__(self):
        result =''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result +srr.getName() + '->'\
                        + dest.getName()+ '\n'
        
        return result[:-1] 
        

class Graph(Digraph):
    def addEdge(self,edge):
        Digraph.addEdge(self,edge)
        rev =Edge(edge.getDestination(),edge.getSource())
        Diagraph.addEdge(self,rev)


#--------------#
        
d1 = {}
for i in range(10000):
    x = random.randrange(10) 
    d1[x] = d1.get(x, 0) + 1
d2 = {}
for i in range(10000):
    x = int(random.random()*10)
    d2[x] = d2.get(x, 0) + 1
d3 = {}
for i in range(10000):
    x = random.randint(0, 10)
    d3[x] = d3.get(x, 0) + 1
     
#---------------#
import random
random.seed

def rollDie():
    return random.choice([1,2,3,4,5,6])

def testRoll(n=10):
    result=''
    for i in range(n):
        result=result+str(rollDie())
    print(result)
    
def runSim(goal,numTrials):
    total=0
    for i in range(numTrials):
        result=''
        for j in range(len(goal)):
            result += str(rollDie())
            
        if result ==goal:
            total +=1
    print('actual prob =',
         round(1/(6**len(goal)),8))
    estProb =round(total/numTrials,8)
    print('Estimated prob =',
            round(estProb, 8))
      
runSim('1111',1000)


def fracBoxCars(numTests):
    numBoxCars=0
    for i in range(numTests):
        if rollDie()== 6 and rollDie()==6:
            numBoxCars +=1
    return numBoxCars/numTests
    
print('freq of double 6',
      str(fracBoxCars(100000)*100)+'%')


#-------------------------#

import random
mylist = []

for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
print(mylist)

#-----------------#

import math
def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    m=0
    if len(L) ==0:
        return float('NaN')
    
    else:
    
        lengths= list(map(len,L))
        N = len(lengths) * 1.0
        mu = sum(lengths) / N
        s = 0
        for t in lengths:
            s += (t - mu) ** 2
        s = math.sqrt(s / N)
        return s
    
#----------------
import random, pylab
dist=[]

for i in range(100000):
    dist.append(random.gauss(0,30))
    
pylab.hist(dist,30)

#---------------------#

import pylab, random
random.seed(0)

####################
## Helper functions#
####################
def flipCoin(numFlips):
    '''
    Returns the result of numFlips coin flips of a biased coin.

    numFlips (int): the number of times to flip the coin.

    returns: a list of length numFlips, where values are either 1 or 0,
    with 1 indicating Heads and 0 indicating Tails.
    '''
    with open('coin_flips.txt','r') as f:
        all_flips = f.read()
    flips = random.sample(all_flips, numFlips)
    return [int(flip == 'H') for flip in flips]


def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

    
#############################
## CLT Hands-on		     #
##				     #
## Fill in the missing code #
## Do not use numpy/pylab   #
#############################
meanOfMeans, stdOfMeans = [], []
sampleSizes = range(10, 500, 50)

def clt():
    for sampleSize in sampleSizes:
        sampleMeans = []
        for t in range(20):
            sample = flipCoin(sampleSize) ## FILL THIS IN
            sampleMeans.append(getMeanAndStd(sample)[0])
        ## FILL IN TWO LINES
        ## WHAT TO DO WITH THE SAMPLE MEANS?
        meanOfMeans.append(getMeanAndStd(sampleMeans)[0])
        stdOfMeans.append(getMeanAndStd(sampleMeans)[1])

clt()
pylab.figure(1)
pylab.errorbar(sampleSizes, meanOfMeans,
               yerr = 1.96*pylab.array(stdOfMeans),
               label = 'Est. mean and 95% confidence interval')
pylab.xlim(0, max(sampleSizes) + 50)
pylab.axhline(0.65, linestyle = '--',
              label = 'True probability of Heads')
pylab.title('Estimates of Probability of Heads')
pylab.xlabel('Sample Size')
pylab.ylabel('Fraction of Heads (minutes)')
pylab.legend(loc = 'best')
pylab.show()

#-------------#
def throwNeedles(numNeedles):
    success = 0
    for n in range(numNeedles):
        x = random.random()
        if (1+x)**2 < 2.0:
            success += 1
    sqrt2 = 1+(float(success)/numNeedles)
    return sqrt2    


#-------------------#
    
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    if numTrials >= 1:
        results = []
        for i in range(numTrials):
            bucket = ['R', 'R', 'R', 'G', 'G', 'G']
            draws = []
            for j in range(3):
                choice = random.choice(bucket)
                draws.append(choice)
                bucket.remove(choice)
            results.append(draws)
        counter = 0
        for k in results:
            if k[0] == k[1] == k[2]:
                counter += 1
        return counter/float(numTrials)           
    else:
        return 'numTrials must be greater than 0' 
