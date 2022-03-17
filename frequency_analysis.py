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
    alphabet_perc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    print(len(alphabet_perc))

    ##compare the percentages between the text and the alphabet
    ##replace each character in the text with the alphabet letter closest in percentage

print(frequency_analysis("Hello World"))