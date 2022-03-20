from shift_vigenere import shift_cipher
from shift_vigenere import ALPHABET
from shift_vigenere import PLAIN_TEXT

LETTER_USAGE = {
    "a":8.5, "b":2.1, "c":4.5, "d":3.4, "e":11.2, "f":1.8, "g":2.5, "h":3.0,
    "i":7.5, "j":0.2, "k":1.1, "l":5.5, "m":3.0, "n":6.7, "o":7.2, "p":3.2,
    "q":0.2, "r":7.6, "s":5.7, "t":7.0, "u":3.6, "v":1.0, "w":1.3, "x":0.3,
    "y":1.8, "z":0.3
}

MOST_USED = (
        "e","a","r","i","o","t","n","s","l","c","u","d","p","h","m","g","b",
        "y","f","w","k","v","x","z","q","j")

def frequency_analysis(cipher_text):

    ##a list (so it can be ordered) of unique letters in the ciphertext
    letters_used = []
    for letter in cipher_text:
        if letter not in letters_used:
            letters_used.append(letter)

    ##count the instances of each letter used in the cipher text
    ##divide by the length of the ciphertext and multiply by 100 to get the percent
    letters_count = [
        ((cipher_text.count(letter)/len(cipher_text))*100) 
        for letter in letters_used]
    '''while letters_used and letters_count are separate lists, 
    the indexes are the same. letters_count[0] refers to the count
    of the letter at letters_used[0]'''

    cipher_usage = {
        "a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0,
        "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0,
        "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0,
        "y":0, "z":0}

    for letter in letters_used:
        ##add the letter count for the corresponding letter to the usage dictionary
        ##reformat the float into a string to limit the decimals
        ##re-reformat the percentage back into a float
        cipher_usage[letter] = float("{:.1f}".format(letters_count[letters_used.index(letter)]))

    '''for solving a shift cipher:
    
    apply a shift cipher using 
    the index of the most common used cipherletter as the shift
    OR
    more reliable would be showing the usage for a normal alphabet
    vs the usage in a ciphertext and match up the wax and wane patterns'''
    
    while True:
        for letter in LETTER_USAGE:
            print(f"Normal usages: {letter, LETTER_USAGE[letter]} \t Cipher usage: {letter, cipher_usage[letter]}")
        shift = input("Where does the shift alphabet start? > ")
        solve = shift_cipher(cipher_text,ALPHABET.index(shift))
        keep_going = input(f"Does this make sense?\n\t{solve}\nyes or no? > ")
        if keep_going == "yes":
            break

    return

frequency_analysis(shift_cipher(PLAIN_TEXT,7))