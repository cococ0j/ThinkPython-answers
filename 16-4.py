import copy

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
    t_new = Time()
    t_new = copy.deepcopy(t)
    if t_new.second >= 60:
        t_new.minute += 1
        t_new.second = t_new.second - 60
        return carry_second(t_new)
    else:
        return t_new

def increment_second(t, dsecond):
    time_new = Time()
    time_new = copy.deepcopy(t)
    time_new.second += dsecond
    result = carry_second(time_new)
    return result
    

def main():
    time = Time()
    time.hour = 10
    time.minute = 10
    time.second = 0
    print_time(time)
    print_time(increment_second(time,121))
    print_time(time)
    
if __name__ == "__main__":
    main()
