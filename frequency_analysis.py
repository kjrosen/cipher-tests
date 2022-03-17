def frequency_analysis(text):
    
    text.replace(" ", "")

    counting = []
    ##count each character in the text
    for char in text:
        counting.append(text.count(char))
    
    percents = []
    ##find percentage for each count
    for num in counting:
        percents.append(num/len(text))
    
    ##save a variable of the percentage of each letter in the alphabet
    alphabet_perc = {"a":8.5, "b":2.1, "c":4.5, "d":3.4, "e":11.2, "f":1.8, "g":2.5, 
    "h":3.0, "i":7.5, "j":0.2, "k":1.1, "l":5.5, "m":3.0, "n":6.7, "o":7.2, "p":3.2, 
    "q":0.2, "r":7.6, "s":5.7, "t":7.0, "u":3.6, "v":1.0, "w":1.3, "x":0.3, "y":1.8, 
    "z":0.3}

    for char in text:
        pass

    ##compare the percentages between the text and the alphabet
    ##replace each character in the text with the alphabet letter closest in percentage

print(frequency_analysis("Hello World"))