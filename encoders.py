from mimetypes import init

TEST_TEXT = """A good input text for keeping messages hidden is
keeping it short. But a good input text for decrypting ciphers is longer,
so if you can't keep it short at least don't include punctuation.
This way we have less hints about the structure of the plain text,
but the cipher text still has enough letters to analyze."""
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
TEST_KEYS = ["key", "once upon a midnight dreary", "the quick brown fox jumps over the lazy dog"]
BABBINGTON_ALPHABET = {
    "a":"\N{COPTIC CAPITAL LETTER O}", "b":"\N{OLD HUNGARIAN CAPITAL LETTER EGY}",
    "c":"\N{OLD HUNGARIAN CAPITAL LETTER ES}", "d":"\N{COPTIC CAPITAL LETTER OLD COPTIC OOU}",
    "e":"\N{COPTIC CAPITAL LETTER ALFA}", "f":"\N{CAUCASIAN ALBANIAN LETTER EYN}",
    "g":"\N{COPTIC CAPITAL LETTER THETHE}", "h":"\N{COPTIC SMALL LETTER OOU}",
    "i":"\N{COPTIC CAPITAL LETTER IAUDA}", "j":" ", "k":"\N{GEORGIAN LETTER BAN}",
    "l":"\N{CAUCASIAN ALBANIAN LETTER SEYK}", "m":"\N{COPTIC OLD NUBIAN VERSE DIVIDER}",
    "n":"\N{CAUCASIAN ALBANIAN LETTER DZAY}", "o":"\N{OLD HUNGARIAN NUMBER FIVE}",
    "p":"\N{CAUCASIAN ALBANIAN LETTER GHEYS}", "q":"\N{GEORGIAN LETTER ON}", 
    "r":"\N{ARMENIAN CAPITAL LETTER BEN}", "s":"\N{COPTIC CAPITAL LETTER DALDA}",
    "t":"\N{CAUCASIAN ALBANIAN LETTER KAR}", "u":"\N{COPTIC SMALL LETTER SIMA}",
    "v":" ", "w":" ", "x":"\N{CAUCASIAN ALBANIAN LETTER YOWD}", 
    "y":"\N{CAUCASIAN ALBANIAN LETTER SHOY}", "z":"\N{COPTIC CAPITAL LETTER DIALECT-P HORI}", 
    "and":"\N{COPTIC SMALL LETTER DIALECT-P KAPA}", "for":"\N{GEORGIAN LETTER WE}", 
    "but":"\N{COPTIC CAPITAL LETTER AKHMIMIC KHEI}", "with":"\N{OLD HUNGARIAN CAPITAL LETTER A}", 
    "that":"\N{ARMENIAN CAPITAL LETTER KEN}", "if":"\N{ARMENIAN CAPITAL LETTER VEW}", 
    "as":"\N{GEORGIAN LETTER UN}", "of":"\N{GEORGIAN LETTER GHAN}", 
    "the":"\N{GEORGIAN LETTER TAR}", "by":"\N{GLAGOLITIC CAPITAL LETTER DOBRO}", 
    "so":"\N{GEORGIAN CAPITAL LETTER HOE}", "not":"\N{OLD HUNGARIAN CAPITAL LETTER EB}", 
    "when":"\N{COPTIC CAPITAL LETTER CRYPTOGRAMMIC GANGIA}", 
    "from":"\N{OLD HUNGARIAN CAPITAL LETTER ETY}", "this":"\N{GLAGOLITIC CAPITAL LETTER ONU}", 
    "is":"\N{GLAGOLITIC CAPITAL LETTER NASHI}", "in":"\N{COPTIC CAPITAL LETTER KHI}", 
    "say":"\N{GEORGIAN LETTER IN}", "me":"\N{GEORGIAN LETTER TAN}", 
    "my":"\N{GEORGIAN LETTER LAS}", "you":"\N{CAUCASIAN ALBANIAN LETTER QAY}", 
    "what":"\N{GEORGIAN LETTER DON}", "where":"\N{CAUCASIAN ALBANIAN LETTER TIWR}", 
    "which":"\N{CAUCASIAN ALBANIAN LETTER BET}", "there":"\N{GEORGIAN LETTER CHAR}", 
    "send":"\N{COPTIC CAPITAL LETTER OLD COPTIC HAT}", "receive":"\N{ARMENIAN SMALL LETTER FEH}", 
    "pray":"\N{GEORGIAN CAPITAL LETTER HE}"
    }

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


def subsitution_cipher(plain_text,cipher_alphabet):
    '''encodes a given text with a given cipher
    
    takes a string text and an alphabet dictionary
    returns a string stext
    '''
    ##first replace the full words in the plain text
    i = 0
    cipher_text = ""
    plain_words = plain_text.split()
    for word in plain_words:
        no_punct = simplify_plaintext(word)##remove punctuation temporarily
        if no_punct in cipher_alphabet:
            plain_words[i] = cipher_alphabet[no_punct]
        
        ##add each individual character to a cipher_text
        for char in word:
            cipher_text += char
        i += 1

    cipher_text = simplify_plaintext(cipher_text)##just in case
    
    ##then iterate through each character, replacing each letter for the corresponding 
    for char in cipher_text:
        try:
            cipher_text = cipher_text.replace(char,cipher_alphabet[char])
        except:
            continue

    return cipher_text


def shift_cipher(plain_text,shift):
    '''encodes a given text shifted down the alphabet a given number
    
    takes a string of plain text, and an integer to shift over
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


def vigenere_cipher(plain_text,key):
    '''encodes a given text with a rotating shift cipher based on a given key
    
    takes a string plain text and a string key
    returns a string cipher text'''

    ##rid both plaintext and key of extraneous characters
    plain_text = simplify_plaintext(plain_text)
    key = simplify_plaintext(key)

    ##repeat the key over the plaintext forever: each plainchar has its own shift key
    full_key = key
    while len(full_key) < len(plain_text):
        full_key += key

    i = 0
    cipher_text = ""
    ##run a standard shift cipher over each individual character shifted to the keychar 
    for char in plain_text:
        cipher_text += shift_cipher(char,ALPHABET.index(full_key[i]))
        i += 1
    
    return cipher_text