from Entropy_of_dataset import *
from Entropy_of_attribute import *
import numpy as np
import pandas as pd

def get_information_gain(df,attribute):
    e_s = get_entropy_of_dataset(df)
    e_attr = get_entropy_of_attribute(df, attribute)
    return e_s - e_attr #information gain