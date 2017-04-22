def remove_duplicates(t):
    t.sort()
    t1 = []
    i = 0
    a = len(t) - 1 
    while i < len(t)-1:
        if t[i] != t[i+1]:
            t1.append(t[i])
        i = i + 1
    return t1 + [t[a]]

t = ["a",'b','c','d','c','c']
remove_duplicates(t)
