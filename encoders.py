from mimetypes import init

PLAIN_TEXT = """A good input text for keeping messages hidden is
keeping it short. But a good input text for decrypting ciphers is longer,
so if you can't keep it short at least don't include punctuation.
This way we have less hints about the structure of the plain text,
but the cipher text still has enough letters to analyze."""

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def simplify_plaintext(plain_text):
    '''removes spaces and punctuation from a plain text for better encryption'''
    plain_text = plain_text.replace(" ","")##remove spaces from the plaintext
    plain_text = plain_text.replace(".","")
    plain_text = plain_text.replace(",","")
    plain_text = plain_text.replace("'","")
    plain_text = plain_text.replace("-","")
    plain_text = plain_text.replace("!","")
    plain_text = plain_text.replace("?","")
    plain_text = plain_text.replace("\n","")

    return plain_text.lower()

def shift_cipher(plain_text,shift):
    '''takes a string of plain text, and an integer to shift over

    returns a cipher text encoded with the shifted alphabet'''

    cipher_text = ""##create a coded variable

    plain_text = simplify_plaintext(plain_text)##removes unnecessary characters
    ##iterate through the input text
    ##match each character with its alphabet letter, matched to the index
    ##add the value at the index + shift to the code variable
    ##allow for looping through the alphabet
    for char in plain_text:
        letter = ALPHABET.index(char)
        try:
            cipher_text += ALPHABET[letter + shift]
        except:
            cipher_text += ALPHABET[letter + shift - 26]
    
    return cipher_text

print(shift_cipher(PLAIN_TEXT,1))

def vigenere_cipher(plain_text,key):
    '''takes in a plaintext message and a key
    
    places the key over it repeatedly, and considers each letter
    from the key the start of a new alphabet shifted over
    
    returns a ciphertext with each letter replaced with that letter's index
    from the corresponding key-character's alphabet'''

    plain_text = simplify_plaintext(plain_text)#rids plaintext of extraneous characters
    key = simplify_plaintext(key)#keys also need to be simplified
    
    full_key = key##we'll repeat the key over the plaintext forever
    while len(full_key) < len(plain_text):
        full_key += key

    '''each letter in the plaintext is encoded with a shift cipher
    using the alphabet starting with the corresponding key letter'''
    i = 0
    cipher_text = ""
    for char in plain_text:##each letter in the key is its own shift
        cipher_text += shift_cipher(char,ALPHABET.index(full_key[i]))
        i += 1
    
    return cipher_text

print(vigenere_cipher(PLAIN_TEXT,"feather"))
