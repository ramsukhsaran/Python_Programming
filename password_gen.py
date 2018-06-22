import random
import string

def pwd():


    length=int(input("how many characters would like in your password"))
    pwd=""
    count=0
    while count!=length:
        upper=[random.choice(string.ascii_uppercase)]
        lower=[random.choice(string.ascii_lowercase)]
        num=[random.choice(string.digits)]
        symbol=[random.choice(string.punctuation)]
        password=upper+lower+num+symbol
        pwd+=random.choice(password)
        count+=1
        continue

    if count==length:
         print("your password:",pwd)
pwd() 
