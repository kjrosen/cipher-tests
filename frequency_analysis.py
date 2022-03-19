'''
most used letters in the english language:

"e":11.2 - "a":8.5 - "r":7.6 - "i":7.5 - "o":7.2 - "t":7.0 - "n":6.7 - 
"s":5.7 - "l":5.5 - "c":4.5 - "u":3.6 - "d":3.4 - "p":3.2 - "h":3.0 - "m":3.0
"g":2.5 - "b":2.1 - "y":1.8 - "f":1.8 - "w":1.3 - "k":1.1 - "v":1.0 - 
"x":0.3 - "z":0.3 - "q":0.2 - "j":0.2
'''

def frequency_analysis(cipher_text):
    most_used = (
        "e","a","r","i","o","t","n","s","l","c","u","d","p","h","m","g","b",
        "y","f","w","k","v","x","z","q","j")

    ##a list (so it can be ordered) of unique letters in the ciphertext
    letters_used = []
    letters_used = [
        letter for letter in cipher_text 
        if letter not in letters_used]

    ##count the instances of each letter used in the cipher text
    letters_count = [cipher_text.count(letter) for letter in letters_used]
    '''while letters_used and letters_count are separate lists, 
    the indexes are the same. letters_count[0] refers to the count
    of the letter at letters_used[0]'''

    ##find the most used letter in the cipher, and save the index
    # highest_index = letters_count.index(max(letters_count))
    # most_cipher = letters_used[highest_index]##now we now which letter is most used

    '''for solving a subsitute cipher:
    
    replace the most used with e
    then the second with a
    and so on through the alphabet'''
    ## 
    '''for solving a shift cipher:
    
    apply a shift cipher using 
    the index of the most common used cipherletter as the shift'''

    return

frequency_analysis("hnvvkpuwbaaleamvyrllwpuntlzzhnlzopkklupzrllwpunpazovyaibahnvvkpuwbaaleamvykljyfwapunjpwolyzpzsvunlyzvpmfvbjhuarllwpazovyahaslhzakvuapujsbklwbujabhapvuaopzdhfdlohclslzzopuazhivbaaolzaybjabylvmaolwshpualeaibaaoljpwolyaleazapssohzluvbnoslaalyzavhuhsfgl")