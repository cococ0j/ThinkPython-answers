def histogram(s):
    h = {}
    for i in s:
        h[i] = h.get(i,0) + 1
    return h
def reverse_lookup(h,a):
    t = []
    for i in h:
        if a == h[i]:
            t.append(i)
    if t == []:
        raise ValuError
    else:
        return t
    
if __name__ == '__main__':
    s = "parrotter"
    h = histogram(s)
    print(reverse_lookup(h, 1))
