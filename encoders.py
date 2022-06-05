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

ALPHABET_INDEX = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4, 
    "f": 5, 
    "g": 6, 
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25
}

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
    "ekmflgdqvzntowyhxuspaibrcj", "ajdksiruxblhwtmcqgznpyfvoe",
    "bdfhjlcprtxvznyeiwgakmusqo", "esovpzjayquirhxlnftgkdcmwb",
    "vzbrgityupsdnhlxawmjqofeck", "ejmzalyxvbwfcrquontspikhgd",
    "yruhqsldpxngokmiebfzcwvjat", "fvpjiaoyedrzxwgctkuqsbnmhl"
    ]
TEST_WHEELS = [WHEELS[0], WHEELS[1], WHEELS[2]]
TEST_PLUGS = ["nk", "xo", "me", "ju", "fl", "ps"]


def simplify_plaintext(plaintext):
    """removes spaces and punctuation from a plain text for better encryption
    
    >>> simplify_plaintext("`~!@#$%^&*()_+=-\|]}[{;:'<,>.?/Hello World")
    'helloworld'

    """

    punctuation = ",./?><;':[]\{}|=-)(*&^%$#@!~`_+\n \t"
    for punct in punctuation:
        plaintext = plaintext.replace(punct, "")
    
    plaintext = plaintext.replace('"','')

    return plaintext.lower()


def subsitution_cipher(plaintext, cipher_alphabet):
    """encodes a given plaintext with a cipher alphabet, returns a ciphertext string
    
    cipher_alphabets are dictionaries with letters and/or words as keys, cipher chars as values
    
    >>> subsitution_cipher("Hello world", BABBINGTON_ALPHABET)
    'ⲱⲀ𐕚𐕚𐳻 𐳻Բ𐕚Ⲿ'

    """

    ##first replace the full words in the plain text
    ciphertext = ""
    plain_words = plaintext.split()

    for word in plain_words:
        simple_word = simplify_plaintext(word)##remove punctuation AFTER splitting 

        if simple_word in cipher_alphabet:##check for full word in the cipher alphabet
            ciphertext += cipher_alphabet[simple_word]

        else:
            for char in simple_word:##if not a keyword replace each letter
                ciphertext += cipher_alphabet[char]

    return ciphertext


def shift_cipher(plaintext, shift):
    """encodes a given plaintext n-number of letters shifted down the alphabet
    
    >>> shift_cipher("Hello World", 6)
    'nkrrucuxrj'
    
    """

    ciphertext = ""

    plaintext = simplify_plaintext(plaintext) 

    for char in plaintext:
        char_idx = ALPHABET_INDEX[char]

        if char_idx + shift > 25:
            ciphertext += ALPHABET[char_idx + shift - 26]

        else:
            ciphertext += ALPHABET[char_idx + shift]            
    
    return ciphertext


def vigenere_cipher(plaintext, key):
    """encodes a given plaintext with a rotating shift cipher based on the alphabetIdx of a given key
    
    repeats the key over the length of the plaintext, giving each char in plaintext a coresponding key char
    shift each char using the index of the key char as the shift number

    >>> vigenere_cipher("Hello World", "test")
    'aidehagkeh'
    
    """

    plaintext = simplify_plaintext(plaintext)
    key = simplify_plaintext(key)

    key = key * len(plaintext)

    ciphertext = ""
    for idx, char in enumerate(plaintext):
        ciphertext += shift_cipher(char, ALPHABET_INDEX[key[idx]])
    
    return ciphertext


def enigma_machine(plaintext, swaps, wheels):
    """encodes a given plaintext via an enigma machine

    first letters from the swaps trade places in the plaintext
    second each character goes through a wheel, shifting according to the letter on it
        same for the second wheel
        same for the third wheel
    
    the first wheel rotates one degree for the next character
    when the first wheel rotates 26x
        the second wheel begins rotating
        the same for the third

    >>> enigma_machine("Hello World", TEST_PLUGS, TEST_WHEELS)
    'mxsljdbibd'

    TODO: something about a reflector so decoding is the same process as encoding

    """

    swapedtext = simplify_plaintext(plaintext)
    ciphertext = ""

    # Use .upper() to ensure the second swap won't reswap first
    for pair in swaps:
        swapedtext = swapedtext.replace(pair[0], pair[1].upper())
        swapedtext = swapedtext.replace(pair[1], pair[0].upper())

    swapedtext = swapedtext.lower()


    rotate1_num = 0 
    rotate2_num = 26
    rotate3_num = 26

    def rotate_wheel(wheel):
        extra = wheel[0]
        wheel = wheel[1:]

        return wheel + extra


    for char in swapedtext:
        wheel1 = wheels[0][0]
        wheel2 = wheels[1][0]
        wheel3 = wheels[2][0]

        cipher = shift_cipher(char, ALPHABET_INDEX[wheel1])
        if rotate1_num < 26:
            wheels[0] = rotate_wheel(wheels[0])
            rotate1_num += 1
        elif rotate1_num == 25:
            rotate1_num = 26
            rotate2_num = 0

        cipher = shift_cipher(cipher, ALPHABET_INDEX[wheel2])
        if rotate2_num < 26:
            wheels[1] = rotate_wheel(wheels[1])
            rotate2_num += 1
        elif rotate2_num == 25:
            rotate2_num = 26
            rotate3_num = 0

        cipher = shift_cipher(cipher, ALPHABET_INDEX[wheel3])
        if rotate3_num < 26:
            wheels[2] = rotate_wheel(wheels[2])
            rotate3_num += 1
        elif rotate3_num == 25:
            rotate3_num = 26
            rotate1_num = 0

        ciphertext += cipher

    return ciphertext


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED!\n")
    