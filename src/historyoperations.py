import os

def add_to_history_file(text):
    text = str(text)
    currententries = get_history_entries()
    if text in currententries:
        return
    with open("history", "a") as history:
        history.write(text+'\n')
        history.close()


def clear_history():
    historyfile = os.getcwd() + '/history'    
    if os.path.isfile(historyfile):
        os.remove(historyfile)

def get_history_entries():
    historyfilename = os.getcwd() + '/history' 
    if os.path.isfile(historyfilename) == False:
        return [] 
    historyfile = open(historyfilename, "r")
    entries = historyfile.read().split('\n')
    return entries