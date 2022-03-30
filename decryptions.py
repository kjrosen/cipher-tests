from os import remove
from random import randint

from encoders import TEST_TEXT
from encoders import ALPHABET
from encoders import BABBINGTON_ALPHABET
from encoders import TEST_KEYS

# from encoders import simplify_plaintext
from encoders import subsitution_cipher
from encoders import shift_cipher
from encoders import vigenere_cipher

LETTER_USAGE = {
    "a":8.5, "b":2.1, "c":4.5, "d":3.4, "e":11.2, "f":1.8, "g":2.5, "h":3.0,
    "i":7.5, "j":0.2, "k":1.1, "l":5.5, "m":3.0, "n":6.7, "o":7.2, "p":3.2,
    "q":0.2, "r":7.6, "s":5.7, "t":7.0, "u":3.6, "v":1.0, "w":1.3, "x":0.3,
    "y":1.8, "z":0.3
}

MOST_USED = [
        "e","a","r","i","o","t","n","s","l","c","u","d","p","h","m","g","b",
        "y","f","w","k","v","x","z","q","j"]

def frequency_analysis(cipher_text):
    '''runs an interface to replace common characters in a cipher with plaintext
    
    given a string cipher text
    counts each instance of each character in the cipher text 

    returns a cipher alphabet with usage percentage
    '''

    cipher_alphabet = {}
    ##builds a cipher alphabet and counts the instances of each character
    for character in cipher_text:
        cipher_alphabet[character] = cipher_alphabet.get(character,0) + 1

    ##adjusts the character count into a character usage percentage
    for character in cipher_alphabet:
        cipher_alphabet[character] = (cipher_alphabet[character]/len(cipher_text)) * 100

    ##prints the cipher alphabet compared usage
    for char in cipher_alphabet:
        print(char,cipher_alphabet[char])
    
    return cipher_alphabet


##TODO: add checks for double characters
def check_doubles(cipher_text):
    '''indicate double characters in a cipher text'''
    doubles = ""

    i = 0
    while i < len(cipher_text):
        if cipher_text[i] == cipher_text[i + 1]:
            ##change the color? ##bold?
            doubles += cipher_text[i] + cipher_text[i + 1]
            i += 2
        else:
            doubles += cipher_text
            i += 1
            
    return doubles


##TODO: add checks for characters repeatedly placed next to each other
def repeat_correspondance(cipher_text, repeat_n):
    '''finds repeated instances when n characters follow each other'''

    show_ngrams = cipher_text
    chains = []
    ##use markov chains to great ngrams
    for i in range(len(cipher_text) - (repeat_n - 1)):
        ngram = cipher_text[i: i + repeat_n]

    ##iterate through the ngrams, counting identacal ngrams
    for ngram in chains:
        if chains.count(ngram) > 1:
            show_ngrams.replace(ngram,ngram)##TODO the color
            
    ##return the cipher_text with the repeated ngrams highlighted
    return show_ngrams


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


test_sub = subsitution_cipher(TEST_TEXT,BABBINGTON_ALPHABET)
test_shift = shift_cipher(TEST_TEXT,randint(0,26))
test_vigenere = vigenere_cipher(TEST_TEXT,TEST_KEYS[randint(0,2)])

print(f"\nSubsitution Cipher:\n{test_sub}\n\nShift Cipher:\n{test_shift}")
print(f"\nVigenere Cipher:\n{test_vigenere}\n")