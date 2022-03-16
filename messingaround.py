from mimetypes import init

def vigenere_cipher():
    ##get a key
    key = input("What is the key? > ")
    ##get a user generated plaintext to encode

    ##create a new key that repeats itself until the length matches plaintext
    ##create an alphabet variable
    ##note the alphabet index for each letter in the plaintext
    ##note the new key value for each plaintext index
    ##note the alphabet index for each value in the key

    ##replace each letter of the plaintext
    ##with the value at the index of its index added ...
    ##added to the index of the new key value at the same index of og letter
    pass

def shift_cipher():
    ##ask the user for something to encode
    ##ask them for how shifted it should be
    plain_text = input("What is your secret message? > ")
    shift = int(input("How shifted is the cipher? > "))
    
    ##create a coded variable
    ##create an alphabet variable
    cipher_text = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    ##iterate through the input text
    ##match each character with its alphabet letter
    ##find the index for letter
    ##add the value at the index + shift to the code variable
    for char in plain_text:
        letter = alphabet.index(char)
        cipher_text += alphabet[letter + shift]
    
    return cipher_text

# print(shift_cipher())

def calculator():
    num1 = input("What's the first number? > ")
    
    try:
        num1 = int(num1)
    except:
        print("Okay wise guy, I'll give it a shot")
    
    fun = input("What are you doing to it? + - * / ")
    if fun != "+" and fun != "-" and fun != "*" and fun != "/":
        fun_type = None
        print("Yeah sure that'll work.")
    else:
        fun_type = 0
    
    num2 = input("What's the second number? > ")
    try:
        num2 = int(num2)
    except:
        print("Funny. Sure.")

    if type(num1) == str or type(num2) == str or fun_type == None:
        return "{} {} {}".format(num1,fun,num2)

    elif fun == "+":
        return num1 + num2
    elif fun == "-":
        return num1 - num2
    elif fun == "*":
        return num1 * num2
    elif fun == "/":
        return num1 / num2

# print(calculator())