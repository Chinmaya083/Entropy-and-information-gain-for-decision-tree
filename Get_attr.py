from Information_gain import *
import numpy as np
import pandas as pd

def get_selected_attribute(df):
        informationGain = {}
        selected_column = ''
        n = df.shape[1]
        attr = df.iloc[:, : n - 1]
        for i in attr:
            informationGain[i] = get_information_gain(df, i)
        selected_column = max(informationGain, key = informationGain.get) 
        '''
        Return a tuple with the first element as a dictionary which has IG of all columns 
        and the second element as a string with the name of the column selected

        example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
        '''
        return (informationGain, selected_column)