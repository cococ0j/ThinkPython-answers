def print_spam():
    print("spam")

def do_twice(f):
    f()
    f()

do_twice(print_spam)
