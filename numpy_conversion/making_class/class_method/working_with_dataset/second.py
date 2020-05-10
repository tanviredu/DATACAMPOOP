import numpy as np 
import pandas as pd 

class DataShell:

    def __init__(self,inputFile):
        self.file = inputFile

    def generate_csv(self):
        self.data_as_csv = pd.read_csv(self.file)
        return self.data_as_csv

data_shell = DataShell(us_life_expectancy)
df = data_shell.generate_csv()
print(df)