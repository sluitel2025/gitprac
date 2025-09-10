import csv

# infile = open("classact3.csv", "r")
# infile.close()

# auto handles closing
# with open("classact3.csv", "r") as infile:

def read_file(filename):
    table = []
    with open(filename, "r") as myfile:
        contents = csv.reader(myfile)

        for content in contents:
            to_float(content)
            table.append(content)
    return table

def to_float(values):
    for val in range(len(values)):
        try:
            con = float(values[val])
            values[val] = con
        except ValueError as e:
            print(e)