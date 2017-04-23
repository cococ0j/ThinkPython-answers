def has_duplicates(t):
    d = {}
    for element in t:
        d[element] = d.get(element, 0) + 1
    for key in d:
        if d[key] > 1:
            return True
        
t = ["a","b","c","banana",1,2,3,"c"]
has_duplicates(t)
