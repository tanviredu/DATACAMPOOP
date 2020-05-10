import numpy as np 
import pandas as pd 

class DataShell:
    def __init__(self,inputFile):
        self.file = inputFile


class CsvDataShell(DataShell):
    def __init__(self,inputFile):
        self.data = pd.read_csv(inputFile)

us_data_shell = CsvDataShell(us_life_expectancy)

print(us_data_shell.data)