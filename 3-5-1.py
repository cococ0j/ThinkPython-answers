#3-5-1
def print1():#print a row with + and -
    print("+","-","-","-","-","+","-","-","-","-","+")
    
def print2():#print a row with |
    print("|"," "," "," "," ","|"," "," "," "," ","|")
    
def do_three(f):#a function can repeat f for three times.
    f()
    f()
    f()
    
print1()
do_three(print2)
print1()
do_three(print2)
print1()
