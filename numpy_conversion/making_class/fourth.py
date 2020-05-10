# class DataShell:

#     ## here we assign a n global class
#     ## variable
#     family = "DataShell"

#     def __init__(self,identifier):
#         self.identifier = identifier

# x = 100

# my_data_shell = DataShell(x)
# print(my_data_shell.family)

## overriding a class

class DataShell:
    family = "DataShell"

    def __init__(self,identifier):
        self.identifier = identifier

x = 100

my_data_shell = DataShell(x)
print(my_data_shell.family)
DataShell.family = "NotDataShell"
print(my_data_shell.family)
