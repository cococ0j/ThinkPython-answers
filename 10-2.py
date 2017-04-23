def capitalize_all(l):
    res = []
    for element in l:
        res.append(element.capitalize())
    return res
def capitalize_nest(l):
    l_new = []
    for element in l:
        if type(element) is str:
            l_new.append(element.capitalize())
        else:
            l_new.append(capitalize_all(element))
    return l_new

l = ["a",["b","c"],"d",["e","f"]]
capitalize_nest(l)
