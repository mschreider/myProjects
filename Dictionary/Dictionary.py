import json
from difflib import get_close_matches


##datapath = "/Users/soccermatt8/Documents/Atom/data.json"
##data = json.load(open(datapath))

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        answer = input("Did you mean %s instead? Type Y if you did, N if you didn't: " % get_close_matches(word, data.keys())[0])
        if answer == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif answer == "N":
            return "the word doesn't exist. Please double check it."
        else:
            return "We didn't understand your query."
    else:
        return "the word doesn't exist. Please double check it."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
