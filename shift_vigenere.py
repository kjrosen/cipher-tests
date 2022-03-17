from mimetypes import init

##to do: think about if the key or the plaintext has a space
def vigenere_cipher():
    ##get a key
    key = input("What is the key? > ").lower()
    ##get a user generated plaintext to encode
    plain_text = input("What is your message? > ").lower()

    ##get rid of the spaces in both the key and the plaintext
    plain_text = plain_text.replace(" ", "")
    key = key.replace(" ", "")
    full_key = key

    ##create a new key that repeats itself until the length matches plaintext
    ##create an alphabet variable
    while len(full_key) < len(plain_text):
        full_key += key

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    alpha_index = []
    key_index = []
    i = 0
    cipher_text = ""
    ##note the alphabet index for each letter in the plaintext
    ##note the alphabet index for each value in the key
    for char in plain_text:
        alpha_index.append(alphabet.index(char))
        key_index.append(alphabet.index(full_key[i]))
        try:
            cipher_text += alphabet[key_index[i] + alpha_index[i]]
        except:
            cipher_text += alphabet[(key_index[i] + alpha_index[i]) - 26]
        i += 1
    
    ##replace each letter of the plaintext
    ##with the value at the index of its index added ...
    ##added to the index of the new key value at the same index of og letter
    return cipher_text

print(vigenere_cipher())

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