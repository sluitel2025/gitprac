import csv
import helper3

table1 = helper3.read_file("classact3.csv")
print(table1)

def write_file(filename, table):
    with open(filename, "w") as outfile:
        writing = csv.writer(outfile)
        writing.writerows(table)

write_file("data2.csv", table1)

def count_letters(word):
    count_dict = {}
    for letter in word:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    return count_dict

word = input("enter a word to count letters: ")
print(count_letters(word))