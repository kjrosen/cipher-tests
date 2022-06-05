from encoders import ALPHABET, BABBINGTON_ALPHABET
from encoders import subsitution_cipher, shift_cipher, vigenere_cipher


LETTER_USAGE = {
    "a":8.5, "b":2.1, "c":4.5, "d":3.4, "e":11.2, "f":1.8, "g":2.5, "h":3.0,
    "i":7.5, "j":0.2, "k":1.1, "l":5.5, "m":3.0, "n":6.7, "o":7.2, "p":3.2,
    "q":0.2, "r":7.6, "s":5.7, "t":7.0, "u":3.6, "v":1.0, "w":1.3, "x":0.3,
    "y":1.8, "z":0.3
}

MOST_USED = [
        "e","a","r","i","o","t","n","s","l","c","u","d","p","h","m","g","b",
        "y","f","w","k","v","x","z","q","j"]

TEST_SUB = subsitution_cipher("Hello World",BABBINGTON_ALPHABET)
TEST_SHIFT = shift_cipher("Hello World",8)
TEST_VIGENERE = vigenere_cipher("Hello World","testkey")


def print_usage_percents(usage):
    """print a frequency analysis dictionary in a readable way
    
    >>> print_usage_percents(LETTER_USAGE)
    a 8.5
    b 2.1
    c 4.5
    d 3.4
    e 11.2
    f 1.8
    g 2.5
    h 3.0
    i 7.5
    j 0.2
    k 1.1
    l 5.5
    m 3.0
    n 6.7
    o 7.2
    p 3.2
    q 0.2
    r 7.6
    s 5.7
    t 7.0
    u 3.6
    v 1.0
    w 1.3
    x 0.3
    y 1.8
    z 0.3
    """

    for char in usage:
        print(char, usage[char])


def frequency_analysis(ciphertext):
    """runs a frequency analysis on a given ciphertext
    
    returns a dictionary of each cipher character and its usage percentage
    
    >>> frequency_analysis(TEST_SHIFT)
    {'p': 10.0, 'm': 10.0, 't': 30.0, 'w': 20.0, 'e': 10.0, 'z': 10.0, 'l': 10.0}

    """

    cipher_alphabet = {}
    for character in ciphertext:
        cipher_alphabet[character] = cipher_alphabet.get(character,0) + 1

    ##adjusts the character count into a character usage percentage
    for character in cipher_alphabet:
        cipher_alphabet[character] = (cipher_alphabet[character]/len(ciphertext)) * 100
    
    return cipher_alphabet


def find_doubles(ciphertext):
    """finds and saves all duplicate characters in a ciphertext
    returns a list
        idx[0] is a list with all the characters doubled up
        idx[1] is the ciphertext with doubled characters capitalized

    >>> find_doubles(TEST_SHIFT)
    [['t'], 'pmTTwewztl']

    """

    doubles = []
    cipher = []

    last = ""

    for idx, char in enumerate(ciphertext):
        letter = char

        if char == last:
            doubles.append(char)
            cipher[idx-1] = cipher[idx-1].upper()
            letter = letter.upper()

        cipher.append(letter)
        last = char
            
    return [doubles, "".join(cipher)]


def finds_repeat_correspondance(ciphertext, nchars):
    """finds repeated instances of n number characters that appear next to each other more than once
    
    returns a dictionary
        keys are substrings of nchars that appear together more than once
        values are how often they appear

    >>> finds_repeat_correspondance(shift_cipher("Things are Happening so Bring a Sweater", 8), 3)
    [{'qvo': 3, 'voa': 2}, 'bpqvoaizmpixxmvqvoawjzqvoiaemibmz']
    
    """
    ngrams = {}

    for idx in range(len(ciphertext)):
        ngrams[ciphertext[idx: idx + nchars]] = ngrams.get(ciphertext[idx: idx + nchars], 0) + 1

    pops = []

    for key in ngrams.keys():
        if ngrams[key] < 2:
            pops.append(key)

    for pop in pops:
        ngrams.pop(pop)

    return [ngrams, ciphertext]


##TODO: as interface changes to a full web app this will serve as bluprint and then be replaced
def subsitution_solve(cipher_text, cipher_alphabet):
    '''interfaces with users to replace common characters with common used letters

    takes in a cipher alphabet with usage percentages
    returns decoded text'''

    sub_letter = MOST_USED[0]

    while True:
        most_cipher = 0  
        ##finds the most used cipher character to replace
        for char in cipher_alphabet:
            if cipher_alphabet[char] > most_cipher:
                most_cipher = cipher_alphabet[char]
                sub_char = char
        print(MOST_USED)
        print(sub_char, "=", sub_letter)
        solve = cipher_text.replace(sub_char, sub_letter)
        correctness = input(f"Does this make sense?\n\t{solve}\nyes or no > ")
        
        if correctness.startswith("yes"):
            MOST_USED.remove(sub_letter)
            sub_letter = MOST_USED[0]
            cipher_alphabet[sub_char] = -1
            cipher_text = solve
            print()
    
        else:
            sub_letter = MOST_USED[MOST_USED.index(sub_letter) + 1]
    
    return solve

def shift_solve(cipher_text):
    '''compares cipher character usage with true usage, finds the shift key
    
    takes an encrypted text, builds a usage dictionary, compares character usage
    interfaces with user to test shift keys
    returns decrypted text
    '''

    ##creates a dictionary of the cipher characters and and their percentage usage
    cipher_alphabet = frequency_analysis(cipher_text)

    for letter in cipher_alphabet:
        ##adjusts each percentage value to one decimal point
        cipher_alphabet[letter] = float("{:.1f}".format(cipher_alphabet[letter]))

    cipher_alphabet = sorted(cipher_alphabet)##alphabetically sort the alphabet
    
    ##compare a plainalphabets usage with the cipher's usage
    while True:
        print(f"Cipher text: {cipher_text}")
        for letter in LETTER_USAGE:
            print(f"Normal usages: {letter, LETTER_USAGE[letter]} \t Cipher usage: {letter, cipher_alphabet[letter]}")
        
        shift = input("Where does the shift alphabet start? > ")
        
        ##decipher using a reverse shift of where the alphabet may start
        solve = shift_cipher(cipher_text, 0 - ALPHABET.index(shift))
        keep_going = input(f"Does this make sense?\n\t{solve}\nyes or no? > ")
        if keep_going == "yes":
            break
        ##keep going until the right shift number is found

    return solve


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED!\n")