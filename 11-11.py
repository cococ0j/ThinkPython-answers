from pronounce import read_dictionary

def make_word_dict():
    fin = open("words.txt")
    d = {}
    for line in fin:
        word = line.strip()
        word = word.lower()
        d[word]= word
    return d

def homephones(a, b, phonetic):
    if a not in phonetic or b not in phonetic:
        return False
    if phonetic[a] == phonetic[b]:
        return True
    else:
        return False

def find_that_word(word,d,phonetic):
    word1 = word[1:]
    if word1 not in d:
        return False
    word2 = word[0]+word[2:]
    if word2 not in d:
        return False
    if not homephones(word,word1,phonetic):
        return False
    if not homephones(word,word2,phonetic):
        return False
    else:
        return True
 
if __name__ == '__main__':
    phonetic = read_dictionary()
    d = make_word_dict()
    for word in d:
        if find_that_word(word,d,phonetic):
            print(word)
    
