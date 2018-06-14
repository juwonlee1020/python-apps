import json
from difflib import get_close_matches
data = json.load(open("data.json", 'r'))
capital_words = [w for w in data.keys() if not w[0].islower()]
def find_def(word):
    if word not in capital_words:
        word = word.lower()
    if(word in data):
        print_def(data[word])
    elif len(get_close_matches(word, data.keys(), n=3, cutoff=0.8)) > 0:
        similar_word = get_close_matches(word, data.keys(), n=3, cutoff=0.8)[0]
        print("Did you mean %s instead?" % similar_word)
        ans = input("If yes, enter 'Y'. If not, enter 'N'")
        if ans.lower() == "y":
            return(print_def(data[similar_word]))
        elif ans.lower() == 'n':
            return("The word doesn't exist. Please check again.")
        else:
            return("We didn't understand your query")
    else:
        return("The word doesn't exist. Please check again.")

def print_def(definition_list):
    for definition in definition_list:
        return definition

word = input("Enter word: ")
while(word != "exit"):
    print(find_def(word))
    word = input("Enter word: ")