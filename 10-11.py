
def change_to_tuplelist():
#using the built-in function enumerate to create tuplelist                 
    tuple_list = []
    for index,letter in enumerate(t):
        tuple_list.append((index,letter))
    return tuple_list
    
def bisect(tuple_list,a):
    i = len(tuple_list) // 2
    if a < tuple_list[i][1]:
        return bisect(tuple_list[:i],a)
    elif a == tuple_list[i][1]:
        return tuple_list[i][0]
    elif a > tuple_list[i][1]:
        return bisect(tuple_list[i:],a)

if __name__ == "__main__":
    t = ['a','b','c','d','e','f','g']
    tuple_list = change_to_tuplelist()
    a = 'g'
    print(bisect(tuple_list,a))


