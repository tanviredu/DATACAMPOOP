import numpy as np 
import pandas as pd 

class DataShell:
    def __init__(self,inputFile):
        self.file = inputFile

my_data_shell = DataShell(us_life_expectancy)

print(my_data_shell)