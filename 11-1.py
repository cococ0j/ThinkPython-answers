def make_word_dict():
    word_list = []
    word_dict = {}
    i = 0
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    for word in word_list:
        word_dict[i] = word
        i = i + 1
    return word_dict
        
def word_dict_sect(word_dict,a):
    vals = word_dict.values()
    if a in vals:
        return True
    else:
        return False

if __name__ == '__main__':
    word_dict = make_word_dict()
    
    print(word_dict_sect(word_dict, "aahs"))
    
