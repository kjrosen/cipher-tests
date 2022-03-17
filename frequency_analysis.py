def frequency_analysis(text):
    
    text.replace(" ", "")

    counting = []
    ##count each character in the text
    for char in text:
        counting.append(text.count(char))

    percents = []
    ##find percentage for each count
    for num in counting:
        percents.append((num/len(text)*10))

    ## need to find a way to get the correct percentages added here
    cipher_alphabet = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, 
    "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, 
    "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, 
    "z":0}

    for char in text:
        cipher_alphabet[char].
    
    ##save a variable of the percentage of each letter in the alphabet
    alphabet_perc = {"a":8.5, "b":2.1, "c":4.5, "d":3.4, "e":11.2, "f":1.8, "g":2.5, 
    "h":3.0, "i":7.5, "j":0.2, "k":1.1, "l":5.5, "m":3.0, "n":6.7, "o":7.2, "p":3.2, 
    "q":0.2, "r":7.6, "s":5.7, "t":7.0, "u":3.6, "v":1.0, "w":1.3, "x":0.3, "y":1.8, 
    "z":0.3}

    for char in text:
        pass
    
    ##compare the percentages between the text and the alphabet
    ##replace each character in the text with the alphabet letter closest in percentage

print(frequency_analysis("""This is the plaintext to be encoded 
It's important to make it long to make the frequency analysis useful"""))