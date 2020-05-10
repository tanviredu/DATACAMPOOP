# class DataShell:

#     def __init__(self):
#         pass 

# my_data_shell = DataShell()
# print(my_data_shell)


# class DataShell:
#     def __init__(self,integerInput):
#         self.data = integerInput

# x = 10
# my_data_shell = DataShell(x)

# print(my_data_shell.data)

class DataShell:
    def __init__(self,identifier,data):
        self.identifier = identifier
        self.data = data 

x = 100
y = [1,2,3,4,5]

my_data_shell = DataShell(x,y)
print(my_data_shell.identifier)
print(my_data_shell.data)
