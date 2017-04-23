import random

def read_file_into_list():
    fin = open('words.txt')
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)
    return t

def map():
    d = {}
    for word in t:
        l_word = list(word)
        l_word.sort()
        tuple_word = tuple(l_word)
        if tuple_word in d:
            l = d[tuple_word]
            l.append(word)
            d[tuple_word] = l
        else:
            l = []
            l.append(word)
            d[tuple_word] = l
    return d

def find_anag():
    vals = d.values()
    l = []
    for value in vals:
        if len(value) >= 2:
            l.append(value)
    return l

def sorting(l):
    #decorate
    t = []
    for element in l:
        t.append((len(element),random.random(),element))
    #sort
    t.sort(reverse=True)
    #undecorate
    for length,random_no,element in t:
        print(element)
 
    
if __name__ == "__main__":
    t =  read_file_into_list()
    d = map()
    l = find_anag()
    sorting(l)
    

