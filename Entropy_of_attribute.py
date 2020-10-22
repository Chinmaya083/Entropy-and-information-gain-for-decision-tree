import numpy as np
import pandas as pd

def get_entropy_of_attribute(df, attribute):
        entropy_of_attribute = 0
        attr = df[attribute].unique()
        attr = attr.tolist()
        target = dict()
        attr_entropy = dict () # Entropy of each individual attribute value
        total_attr = df.shape[0]
        for i in attr :
            attr_entropy[i] = 0
            y = df.loc[df[attribute] == i]
            total = y.shape[0] #denominator in e term
            temp = y['play'].unique().tolist()
            for j in temp :
                target [j] = 0
            for j in y['play'] :
                target [j] += 1
            for j in target.values() :
                attr_entropy[i] += (j / total) * (-np.log2(j / total))
            attr_entropy[i] *= (total / total_attr)
        for i in attr_entropy :
            entropy_of_attribute += attr_entropy[i]
        return abs(entropy_of_attribute)