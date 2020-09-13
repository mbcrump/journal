## This is the journal module

import os 

def load(name):
    data = []
    filename = get_full_pathname(name)
    print(str(filename))
    if os.path.exists(filename):
        print("Inside our if...statement")
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data

def get_full_pathname(name):
    filename = os.path.abspath(os.path.join(".", name + ".txt"))
    return filename