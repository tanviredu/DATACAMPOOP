# class DataShell:

#     def __init__(self):
#         pass

#     def print_static(self):
#         print("You just executed a class Method")

# my_data_shell = DataShell()
# my_data_shell.print_static()

# class DataShell:

#     def __init__(self,datalist):
#         self.data = datalist

#     def show(self):
#         print(self.data)


integer_list = [1,2,3,4,5,6,7,8,9,10]
# my_data_shell = DataShell(integer_list)
# my_data_shell.show()


class DataShell:
    def __init__(self,dataList):
        self.data = dataList
    
    def show(self):
        print(self.data)

    ## find the avg
    def avg(self):
        avg = sum(self.data)/float(len(self.data))
        print(avg)

my_data_shell = DataShell(integer_list)

my_data_shell.show()
my_data_shell.avg()