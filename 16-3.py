
class Time():
    """
    represent time with hour,minute,second
    """
    
def print_time(time):
    print('%.2d:%.2d:%.2d'%(time.hour,time.minute,time.second))

def is_after(t1,t2):
    tuple1 = (t1.hour,t1.minute,t1.second)
    tuple2 = (t2.hour,t2.minute,t2.second)
    return tuple1 > tuple2

def carry_second(t):
#use recursion to avoid using for and while.
    if t.second >= 60:
        t.minute += 1
        t.second = t.second - 60
        return carry_second(t)
    else:
        return t

def increment_second(t, dsecond):
    t.second += dsecond
    result = carry_second(t)
    return result
    

def main():
    time = Time()
    time.hour = 10
    time.minute = 10
    time.second = 0
    print_time(time)
    print_time(increment_second(time,121))
    
if __name__ == "__main__":
    main()
