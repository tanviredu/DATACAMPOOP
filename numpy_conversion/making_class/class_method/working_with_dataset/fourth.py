class DataShell:

    def __init__(self,filepath):
        self.filepath = filepath
        self.data_as_csv = pd.read_csv(filepath)

    def rename_column(self,column_name,new_column_name):
        self.data_as_csv.columns = self.data_as_csv.columns.str.replace(column_name,new_column_name)
    
us_data_shell = DataShell(us_life_expectancy)
## print the data type
print(us_data_shell.data_as_csv.dtypes)

### rename the columns
us_data_shell.rename_column("code","country_code")
print(us_data_shell.data_as_csv.dtypes)