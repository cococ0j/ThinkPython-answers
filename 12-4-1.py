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
            d[tuple_word].append(word)
        else:
            d[tuple_word] = [word]
    return d

def find_anag():
    vals = d.values()
    for value in vals:
        if len(value) >= 2:
            print(value)
    
    
    
if __name__ == "__main__":
    t =  read_file_into_list()
    d = map()
    find_anag()
    
