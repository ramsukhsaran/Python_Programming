#firts import
import random # for ramdon things
import string # for string libariy
def pwd():# decelare function in python
      p=""
      count=0
      length=int(input("Enter how many long you want your password"))
      while count!=length:
          upper=[random.choice(string.ascii_uppercase)] # for upper case latter
          lower=[random.choice(string.ascii_lowercase)] # for lower case latter
          num=[random.choice(string.digits)]            # for number
          symbol=[random.choice(string.punctuation)]    # for symbol{!,@,#....etc}
          password=upper+lower+num+symbol
          p+=random.choice(password)
          continue
      if count==length:
          print("Your passwrd is:",p)

pwd()# calling function
