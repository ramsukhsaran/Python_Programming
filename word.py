import json
from difflib import get_close_matches
data=json.load(open('data.json'))    # loading json data from json file

def translate(word):  # Function for computing result

    word=word.lower()
    
    if word in data:
        return data[word]
    
    elif word.title() in data:    # if word has frist character is capital
        
        return data[word.title()]
    
    elif word.upper() in data:  # like some words always capital like USA,NASA  etc
        return data[word.upper()]
    
    elif len(get_close_matches(word,data.keys()))>0:    #if user enter wrong word for example if user enter rainn insted of rain
                                                        #so it is possibale to remove this debug of user by gussing correct word
        
        choice=input("Did you mean %s insted of  ? Enter Y if yes ,or N if no:"%get_close_matches(word,data.keys())[0])    # string formating  [0] mean frist word of return lists 
        
        if choice=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        
        elif choice=="N":
            
            return "The word doesn't exist. Please check it Again"
        
        else:
            return "we didn't understant your entry of word"
        
    else:
        return "the word donesn;t exist."

while(True):
    
    word=input('Enter word you want menaing for that:')
    output=translate(word)
    if type(output)==list:
        
         for i in output:
              print(i)
    else:
        print(output)


