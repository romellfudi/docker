import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_data(n):
    return pd.DataFrame({'x': np.random.normal(size=n),
                         'y': np.random.normal(size=n)})

def print_generated_data(df):
    print(df)


