def count_vowels(word):
    
    '''
    counts the vowels in a string

    parameters:
    input(str): given by user

    return:
    int: count of vowels in string
    '''

    count = 0

    for char in word:
        if char in "aeiouAEIOU" in word:
            count += 1

    return count

while True:
    words = input("enter a word: ")
    vowel_count = count_vowels(words)

    