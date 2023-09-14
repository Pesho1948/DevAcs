def test_1():
    '''
    Functions may not start with a number
    It may contain numbers, lower-upper chars _
                                            '''
    print("test")

test_1()

#functions with args and params
def calc(arg_1, arg_2): # here we pass the arguments 
    result = arg_1 - arg_2 # here we use them as parameters, to create a result
    return result

print(calc(arg_2=2, arg_1=1))

# We can use *args to pass multiple args to the function and store it as a tuple
def args(*args):
    print(args, type(args), len(args))
    for word in args:
        print("Hello ", word)

args("pesho", "alex", "gosho")

#kwargs uses keyword argument and stores them in a dict
def kwargs(**kwargs):
    print(list(kwargs.values()), type(kwargs))
    for args in kwargs:
        pass

kwargs(arg_1="pesho", banica="alex", toyota=1)

#Defining func with default arg

def default(arg_1, arg_2="default"):
    print(arg_1, arg_2)

default("Hi", "Pesho") # Will print Hi Pesho
default("Hi") #Hi default