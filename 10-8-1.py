def has_duplicates(t):
    for i in range(len(t)):
        j = i + 1
        while j < len(t):
            if t[i] == t[j]:
                return True
            else:
                j = j + 1    
    return False

t = ['a','b','c','d','c']
has_duplicates(t)
