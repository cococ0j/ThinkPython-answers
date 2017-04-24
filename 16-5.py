import copy

class Time():
    """
    represent time with hour,minute,second
    """
    
def print_time(time):
    print('%.2d:%.2d:%.2d'%(time.hour,time.minute,time.second))


def increment(t1, t2):
    second = time_to_int(t1) + time_to_int(t2)
    return int_to_time(second)

def time_to_int(t):
    minute = t.hour * 60 + t.minute
    second = minute * 60 + t.second
    return second

def int_to_time(second):
    t = Time()
    minute,t.second = divmod(second,60)
    t.hour,t.minute = divmod(minute,60)
    return t
    

def main():
    time = Time()
    time.hour = 10
    time.minute = 10
    time.second = 0
    duration = Time()
    duration.hour = 1
    duration.minute = 30
    duration.second = 0
    print_time(increment(time,duration))
    
if __name__ == "__main__":
    main()
