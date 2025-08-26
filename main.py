import random

class character:
    upperCharacter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerCharacter = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    specialCharacter = "~}!@#$%^&*()_-+={[]|\:;'<,>.?/"
    characters = upperCharacter+lowerCharacter+digits+specialCharacter

def PasswordGenerator(char):
    password = ""
    while len(password)<12:
        password += char[random.randint(0,len(char))]
    return password

def PasswordValidator(password):
    Digitpass = False
    Upperpass = False
    Lowerpass = False
    Specialpass = False
    for element in password:
        if element in character.upperCharacter:
            Upperpass = True
        if element in character.lowerCharacter:
            Lowerpass = True
        if element in character.digits:
            Digitpass = True
        if element in character.specialCharacter:
            Specialpass = True
    if Upperpass != True or Lowerpass != True or Digitpass != True or Specialpass != True:
        main()
    else: 
        print(password)

def main():
    password = PasswordGenerator(character.characters)
    PasswordValidator(password)

if __name__ == "__main__":
    main()
 