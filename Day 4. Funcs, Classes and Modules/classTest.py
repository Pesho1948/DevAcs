from sys import path

path.append(r'C:\Users\petar\Desktop\Python\DevAcs\Day 4. Funcs, Classes and Modules\storage')
from classes import Switch, Router

dev_1 = Switch("10.1.1.1", "Switch", "Catalyst")
dev_2 = Router("10.1.1.2", "Router", "ASR")

print(dev_1.dev_info(), '\n' , dev_2.dev_info())
