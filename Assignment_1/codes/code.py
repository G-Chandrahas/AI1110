import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
simlen=10000000
#number of people in random sample.
n =  10

#Probability that the choosen person is right-handed.
p = 0.1666667

experiment=np.zeros(1)
acctual=np.zeros(1)
data_binom = binom.rvs(n,p,size=simlen) 
defects,stimulation = np.unique(data_binom , return_counts= True)
if (len(stimulation) == 7):
	stimulation = np.insert(stimulation,10,0)
	stimulation = np.insert(stimulation,10,0)
	stimulation = np.insert(stimulation,10,0)
	stimulation = np.insert(stimulation,10,0)
if (len(stimulation) == 8):
	stimulation = np.insert(stimulation,10,0)
	stimulation = np.insert(stimulation,10,0)
	stimulation = np.insert(stimulation,10,0)
if (len(stimulation) == 9):
	stimulation = np.insert(stimulation,10,0)
	stimulation = np.insert(stimulation,10,0)
if (len(stimulation) == 10):
	stimulation = np.insert(stimulation,10,0)
stimulation = np.cumsum(stimulation)/simlen
experiment[0]=stimulation[1]
acctual[0]=binom.cdf(1,n,p)

print("For answer  stimulation value is "+str(round(experiment[0],6))+" and acctual value is "+str(round(acctual[0],6)))