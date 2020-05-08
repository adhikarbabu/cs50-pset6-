def main():

    from sys import argv
    import csv
    import re

    while len(argv) < 3:
        print("Usage: python dna.py data.csv sequence.txt")

    fileCSV = open(argv[1], "r")
    fileTXT = open(argv[2], "r")

    dna_string = fileTXT.read()

    count = [0, 0, 0, 0, 0, 0, 0, 0]
    count[0] = pattern("AGATC",dna_string)
    count[2] = pattern("AATG",dna_string)
    count[5] = pattern("TATC",dna_string)
    count[1] = pattern("TTTTTTCT",dna_string)
    count[3] = pattern("TCTAG",dna_string)
    count[4] = pattern("GATA",dna_string)
    count[6] = pattern("GAAA",dna_string)
    count[7] = pattern("TCTG",dna_string)

    smallList = [str(count[0]), str(count[2]), str(count[5])]
    largeList = [str(count[0]), str(count[1]), str(count[2]), str(count[3]), str(count[4]), str(count[5]), str(count[6]), str(count[7])]

    reader = csv.reader(fileCSV)
    for row in reader:
        if row[1:] == smallList:
            print(row[0])
            exit(0)
        if row[1:] == largeList:
            print(row[0])
            exit(0)
    print("No match")

def pattern (substring, mainstring):

    z = mainstring.count(substring)
    if z == 0:
        temp = 0
    else:
        for temp in range (z,0,-1):
            if substring*temp in mainstring:
                break
    return temp

main()
