import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

print("Welcome to Abhijeet's Dictionary"+"\n")
print("Hope this helps you!")
user_word = input("Enter a word: ")
data= json.load(open("data.json"))

def dictionary(user_word):
    user_word= user_word.lower()
    if user_word in data:
        return data[user_word]
    elif user_word.capitalize() in data:
        return data[user_word.capitalize()]
    elif user_word.upper() in data:
        return data[user_word.upper()]
    elif user_word.capitalize() in data:
        return data[user_word.capitalize()]
    elif len(get_close_matches(user_word,data.keys())) > 0 :
        print("Do you mean %(1)s instead of %(2)s"%{"1":get_close_matches(user_word,data.keys())[0],"2":user_word})
        user_action = input("Press y for yes and N for No:")
        user_action = user_action.lower()
        if user_action == "y":
            return data[get_close_matches(user_word,data.keys())[0]]
        else:
            return("The Word %s doesn't exist" %user_word)
    else:
        return ("The Word %s doesn't exist" %user_word)

print(dictionary(user_word))