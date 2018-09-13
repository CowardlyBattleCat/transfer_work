from collections import (
    defaultdict,
    Counter,
    )
from os import (
    path,
    open,
    )
from sys import argv
from string import (
    punctuation,
    digits,
    )



def add(a, b):
    '''Return the sum of a and b'''
    return a + b

assert add(2, 3) == 5
assert add(0, 5.2) == 5.2
assert add(-4, 5) == 1



def invert_dictionary(d):
    dd_inv = defaultdict(list)
    for key, val in d.items():
        if val in dd_inv:
            dd_inv[val].append(key)
        else:
            dd_inv[val] = [key]
    return dd_inv

assert invert_dictionary({'a':1, 'b':2, 'c':1, 'd':3}) == {1: ['a', 'c'], 2:['b'], 3:['d']}

str_file_path = "./test_string_file.txt"

def count_words(txt):
    with open(txt, "r") as original_text:
        text = original_text.read()
        tran1 = str.maketrans('', '', punctuation)
        tran2 = str.maketrans('', '', digits)
    text_clean = text.lower().translate(tran1).translate(tran1)
    print(text_clean)
    count = Counter(text_clean.split())
    return count

#print(count_words(str_file_path))
count_words(str_file_path)

'''
    if ( sys.argv[1:] ):
        try:
            if ( os.path.isfile( sys.argv[1] ) ):
                str_file_path = ( sys.argv[1] )
        except TypeError:
            pass
'''
