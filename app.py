import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        answer = input("Did you mean %s instead? Enter Y for yes, or N for no: " % get_close_matches(w, data.keys())[0])
        answer = answer.lower()

        if answer == 'y':
            return(data[get_close_matches(w, data.keys())[0]])
        elif answer == 'n':
            return("SOrry, we dit not understand you entry..")
        else:
            return('Ok, sorry!')
    else:
        return "word doesn't exist"

word = input("ENter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
