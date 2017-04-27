#3-4-3/4
def do_twice(f,value):
    f(value)
    f(value)
    
def print_twice(string):
    print(string)
    print(string)
    
do_twice(print_twice,"spam")
