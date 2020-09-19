import journal

def main():
    print("enter main")
    run_event_loop()
    

def run_event_loop():
    print("What would you like to do next with your journal?")
    cmd = 'EMPTY'
    journal_name = "default_journal"
    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd:
        cmd = input("Select your command: [A]dd, [L]ist, E[x]it")
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Please enter a valid number. ")

    print("completed")
    journal.save(journal_name, journal_data)

def list_entries(data):
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx +1 , entry))

def add_entry(data):
    text = input("Type your entry and press return when finished. ")
    journal.add_entry(text, data)


main()