# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:09:38 2022

@author: dbullock
"""
#import numpy
import numpy as np

#create a random 3x3 array
demoArray=np.random.rand(3,3)

#print to terminal
print (demoArray)

#import pandas
import pandas as pd

#convert the array to a pandas dataframe
randomDF=pd.DataFrame(demoArray)

#import display capability
from IPython.display import display
display(randomDF)
