def most_frequent(s):
    d = {}
    for i in s:
        d[i] = d.get(i,0) + 1
    t = []    
    for letter in d:
        t.append((d[letter],letter))
    t.sort(reverse=True)
    return t

s = "jakljfldashfiuhxvcjjfaioejvhjhkajflhiweoeotyuihnxbzmnm"
print(most_frequent(s))
