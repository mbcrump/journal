import journal

def main():
    print("enter main")
    loadfile()


def loadfile():
    journal_name = "default_journal"
    journal_data = journal.load(journal_name)
    print(journal_data)

main()