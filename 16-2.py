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

def alter_time_minute(t, dminute):
    t.minute += dminute
    

def main():
    time = Time()
    time.hour = 10
    time.minute = 10
    time.second = 0
    time2 = copy.deepcopy(time)
    alter_time_minute(time2, 10)
    print(is_after(time2,time))
    
if __name__ == "__main__":
    main()
