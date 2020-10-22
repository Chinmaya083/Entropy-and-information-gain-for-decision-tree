import numpy as np
import pandas as pd
import random

def get_entropy_of_dataset(df):
    entropy = 0
    attr = df['play'].unique()
    attr = attr.tolist() # To get all unique class values
    p = dict() 
    total = df['play'].shape[0] # No. of rows in dataframe
    for i in attr :
        p[i] = 0
    for i in attr :
        for j in df['play'] :
            if(j == i):
                p[i] = p[i] + 1
    for i in p.keys() :
        if(p[i] == total): 
            return 0 # Entropy is 0 when sample is completely homogenous
        else:
            entropy = entropy + (-(p[i] / total) * np.log2(p[i] / total))
    return entropy