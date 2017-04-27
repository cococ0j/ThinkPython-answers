#3-4-5
def do_twice(f,value):
    f(value)
    f(value)
    
def do_four(f,value):
    do_twice(f,value)
    do_twice(f,value)
    
do_four(print,"spam")
