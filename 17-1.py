import copy

class Time():
    """
    represent time with hour,minute,second
    """
    def print_time(self):
        print('%.2d:%.2d:%.2d'%(self.hour,self.minute,self.second))
    
    def time_to_int(self):
        minute = self.hour * 60 + self.minute
        second = minute * 60 + self.second
        return second

def int_to_time(second):
    t = Time()
    minute,t.second = divmod(second,60)
    t.hour,t.minute = divmod(minute,60)
    return t

def mul_time(t,integer):
    second = time_to_int(t) * integer
    return int_to_time(second)

def average_time(t,mile):
    per_mile = 1.0 / mile
    return mul_time(t,per_mile)

def main():
    time = Time()
    time.hour = 1
    time.minute = 10
    time.second = 0
    mile = 60
    average_time(time,mile).print_time()

if __name__ == "__main__":
    main()
    
    
#Because the parameter of int_to_time is not an object in class Time.
