def nest_sum(t):
    for element in t:
        if type(element) is int:
            t_new.append(element)
        else:
            nest_sum(element)
    return sum(t_new)
t = [1,2,[3,4],[5,6]]
nest_sum(t)
