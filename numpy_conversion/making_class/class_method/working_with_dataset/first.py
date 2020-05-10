class DataShell:
    def __init__(self,dataList):
        self.data = dataList

    def show(self):
        return self.data

    def avg(self):
        avg = sum(self.data)/float(len(self.data))
        return avg 

integer_list = [1,2,3,4,5,6,7,8,9,10]
my_data_shell = DataShell(integer_list)
print(my_data_shell.show())
print(my_data_shell.avg())
