class DataShell:
    family = "DataShell"

    def __init__(self,name,filepath):
        self.name = name 
        self.filepath = filepath

class CsvDataShell(DataShell):

    def __init__(self,name,filepath):
        self.data = pd.read_csv(filepath)
        self.stats = self.data.describe()

us_data_shell = CsvDataShell("US",us_life_expectancy)
print(us_data_shell.stats)