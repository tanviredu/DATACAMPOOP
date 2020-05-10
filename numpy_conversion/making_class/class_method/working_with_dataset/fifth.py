class DataShell:

    def __init__(self,filepath):
        self.filepath = filepath
        self.data_as_csv = pd.read_csv(filepath)

    def rename_column(self,column_name,new_column_name):
        self.data_as_csv.columns = self.data_as_csv.columns.str.replace(column_name,new_column_name)

    
    def gets_stats(self):
        self.data_as_csv.describe()

us_data_shell = DataShell(us_life_expectancy)
print(us_data_shell.gets_stats())