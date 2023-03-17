import sys

if len(sys.argv) != 4:
    print("Usage: python script.py <sourceFile> <comparisonFile>")
    exit()

sourceFile = sys.argv[1]
comparisonFile = sys.argv[2]
newFile = sys.argv[3]

with open(sourceFile, 'r', encoding='utf-8') as source, \
        open(comparisonFile, 'r', encoding='utf-8') as comparison, \
        open(newFile, 'w', encoding='utf-8') as newfile:
    dictionary = set(word.strip().lower() for word in comparison)

    for word in source:
        word = word.strip().lower()
        if word not in dictionary:
            newfile.write(word + '\n')