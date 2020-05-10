import numpy as np 
import pandas as pd 

class DataShell:
    def __init__(self,filepath):
        self.filepath = filepath
        self.data_as_csv = pd.read_csv(filepath)

us_data_shell = DataShell(us_life_expectency)

print(us_data_shell.data_as_csv)