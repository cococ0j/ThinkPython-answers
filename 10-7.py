def is_anagram(a,b):
    t_a = list(a)
    t_b = list(b)
    t_a.sort()
    t_b.sort()
    if t_a == t_b:
        return True
    else:
        return False
    
a = 'cat'
b = 'tac'
is_anagram(a,b)
