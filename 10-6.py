def is_sorted(t):
    t_new = sorted(t)
    if t_new == t:
        return True
    else:
        return False
    
t = [1,4,3]
is_sorted(t)
