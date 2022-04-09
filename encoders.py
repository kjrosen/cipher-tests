from mimetypes import init
from operator import index

TEST_TEXT = """Hi my name is Ebony Dark'ness Dementia Raven Way 
and I have long ebony black hair -that's how I got my name- 
with purple streaks and red tips that reaches my mid-back 
and icy blue eyes like limpid tears 
and a lot of people tell me I look like Amy Lee 
-AN: if u don't know who she is get da hell out of here!-. 
I'm not related to Gerard Way but I wish I was because he's a major fucking hottie. 
I'm a vampire but my teeth are straight and white. I have pale white skin. 
I'm also a witch, and I go to a magic school called Hogwarts in England 
where I'm in the seventh year -I'm seventeen-. 
I'm a goth -in case you couldn't tell- and I wear mostly black. 
I love Hot Topic and I buy all my clothes from there. 
For example today I was wearing a black corset with matching lace around it 
and a black leather miniskirt, pink fishnets and black combat boots. 
I was wearing black lipstick, white foundation, black eyeliner and red eye shadow. 
I was walking outside Hogwarts. It was snowing and raining so there was no sun, 
which I was very happy about. A lot of preps stared at me. I put up my middle 
finger at them."""
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
WHEELS = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", 
    "BDFHJLCPRTXVZNYEIWGAKMUSQO", "ESOVPZJAYQUIRHXLNFTGKDCMWB", 
    "VZBRGITYUPSDNHLXAWMJQOFECK", "EJMZALYXVBWFCRQUONTSPIKHGD",
    "YRUHQSLDPXNGOKMIEBFZCWVJAT", "FVPJIAOYEDRZXWGCTKUQSBNMHL"
    ]


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
    plain_text = plain_text.replace(":", "")

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
        cipher_text += shift_cipher(char, ALPHABET.index(full_key[i]))
        i += 1
    
    return cipher_text


def enigma_machine(plain_text,swaps,wheels):
    '''
    each swap represents two letters that swap out each other's input
    each rotator represents a sub cipher
    
    after each letter, rotator1 += 1
    when rotator1 goes all the way around once, rotator2 starts shifting
    when rotator2 goes all the way around once, rotator3 starts shifting

    TODO: something about a reflector so decoding is the same process as encoding
    '''
    ##simplify plaintext to get ride of annoyances
    plain_text = simplify_plaintext(plain_text)
    cipher_text = plain_text

    # swapAlpha = ALPHABET[:]
    ##deal with the pure swaps first. 
    # Use .upper() to ensure the second swap won't reswap first
    for pair in swaps:
        cipher_text = cipher_text.replace(pair[0], pair[1].upper())
        cipher_text = cipher_text.replace(pair[1], pair[0].upper())

    # cipher_text = list((cipher_text).lower())

    rotate1_num = 0 
    rotate2_num = 0
    rotate3_num = 0

    for wheel_i in range(3):
        cipher_text = subsitution_cipher(cipher_text, wheels[wheel_i])
    

    return cipher_text

print(enigma_machine(TEST_TEXT, ["nk", "xo", "me", "ju", "fl", "ps"], [WHEELS[0], WHEELS[4], WHEELS[7]]))



    