class DataShell:
    family = "DataShell"

    def __init__(self,name,filepath):
        self.name = name 
        self.filepath = filepath

class CsvDataShell(DataShell):
    def __init__(self,name,filepath):
        self.data = pd.read_csv(filepath)
        self.stats = self.data.describe()

class TsvDataShell(DataShell):

    def __init__(self,name,filepath):
        self.data = pd.read_table(filepath)
        self.stats = self.data.describe()

us_data_shell = CsvDataShell("US", us_life_expectancy)
print(us_data_shell.stats)

# Instantiate TsvDataShell as france_data_shell, print france_data_shell.stats
france_data_shell = TsvDataShell("France", france_life_expectancy)
print(france_data_shell.stats)
