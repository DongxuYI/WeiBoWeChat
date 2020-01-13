# Python Copy File - Sample Code

from shutil import copyfile
from sys import exit


# adding exception handling
for i in range(21, 10354):
    try:
       copyfile("C:/Users/YI/Desktop/spider/poetry/20.xls", "C:/Users/YI/Desktop/spider/poetry/"+str(i)+".xls")
    except:
        pass
