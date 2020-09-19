## This is the journal module #app # 4

import os 

def load(name):
    data = []
    filename = get_full_pathname(name)
    if os.path.exists(filename):
        print("Open file")
        with open(filename, 'r') as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data

def save(name, journal_data):
    filename = get_full_pathname(name)
    print("Saving data")
    with open(filename, 'w') as fout:
            for entry in journal_data:
                fout.write(entry + "\n")

def add_entry(text, journal_data):
    journal_data.append(text)

def get_full_pathname(name):
    filename = os.path.abspath(os.path.join(".", name + ".txt"))
    return filename