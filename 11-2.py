def histogram(s):
    h = {}
    for i in s:
        h[i] = h.get(i,0) + 1
    return h
s = 'aabbccddeefff'
histogram(s)
