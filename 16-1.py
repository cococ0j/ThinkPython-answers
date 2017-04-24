class Time():
    """
    represent time with hour,minute,second
    """
    
def print_time(time):
    print('%.2d:%.2d:%.2d'%(time.hour,time.minute,time.second))
    
def main():
    time = Time()
    time.hour = 10
    time.minute = 10
    time.second = 0
    print_time(time)
    
if __name__ == "__main__":
    main()
