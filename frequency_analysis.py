def frequency_analysis(text):
    ##these are the actual percentages for each letter in the alphabet
    ##as used in the english language
    alphabet_perc = {
        "a":8.5, "b":2.1, "c":4.5, "d":3.4, "e":11.2, "f":1.8, "g":2.5, "h":3.0, 
        "i":7.5, "j":0.2, "k":1.1, "l":5.5, "m":3.0, "n":6.7, "o":7.2, "p":3.2, 
        "q":0.2, "r":7.6, "s":5.7, "t":7.0, "u":3.6, "v":1.0, "w":1.3, "x":0.3, 
        "y":1.8, "z":0.3
        }

    ## need to find a way to get the correct percentages added here
    cipher_alphabet = {
        "a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, 
        "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, 
        "w":0, "x":0, "y":0, "z":0
        }
    
    text = text.replace(" ","") ##remove spaces and other mixemups
    text = text.replace(".","")
    text = text.replace(",","")
    text = text.replace("'","")
    text = text.lower()

    ##create list of unique letters used in the plaintext
    letters_used = list(set(text))
    ##count each letter from the alphabet list as it appears in the text
    letters_count = [text.count(letter) for letter in letters_used]
    '''while letters_used and letters_count are separate lists, 
    the indexes are the same. letters_count[0] refers to the count
    of the letter at letters_used[0]'''

    ##divide that count by the length of text, then multiply by 100 to get percentage
    ##letters_count now is now populated with the percentage of each letter
    for i in range(len(letters_count)):
        letters_count[i] = (letters_count[i]/len(text)) * 100

    ##put those percentages into the corresponding cipher_alphabet dictionary.
    for letter in letters_used:
        i = letters_used.index(letter)
        cipher_alphabet[letter] += letters_count[i]

    print(cipher_alphabet)


print(frequency_analysis("""an input text needs to be long enough to have value when it comes to frequency analysis because otherwise there arent enough letters to analyze"""))