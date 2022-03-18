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
    
    text.replace(" ","") ##remove spaces and other mixemups
    text.replace(".","")
    text.replace(",","")
    text = text.lower()

    letters_used = []
    ##go through the text and add each letter to a new alphabet list
    ##each letter only needs to be added once
    for char in text:
        if char not in letters_used:
            letters_used.append(char)

    letters_count = []
    ##count each letter from the alphabet list as it appears in the text
    for letter in letters_used:
        letters_count.append(text.count(letter))

    ##divide that count by the length of text, then multiply by 10 to get percentage
    for i in range(len(letters_count)):
        letters_count[i] = (letters_count[i]/len(text)) * 10

    ##put those percentages into the corresponding cipher_alphabet dictionary.
    '''this doesn't work right now. 
    key error using cipher_alphabet[letter] appears blank?'''
    for letter in letters_used:
        print(cipher_alphabet[letter])
        i = letters_used.index(letter)
        cipher_alphabet[letter] += letters_count[i]

    print(cipher_alphabet)


print(frequency_analysis("""an input text needs to be long enough to have value when it comes to frequency analysis because otherwise there aren't enough letters to analyze"""))