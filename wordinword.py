# Finds all possible combinations of words within a given character set between two letters and 31

# The longer the initial input the longer the process takes

# The second method takes exceptionally longer than the first.

# The third method uses the enchant system to find the words.

# The final method uses nltk, but is only for American spellings


import enchant
from collections import Counter
import sys
import time
import itertools
import nltk
from nltk.corpus import words

dictsToUse = {}

wordQuestion = "Please enter the letters you wish to use: "
stuff = str(input(wordQuestion))
start_time = time.time()

stuffLength = len(stuff)
for x in range (2,stuffLength+1):
    dictName = str(x) + "WordDictionary"
    fileToUse = "files/" + str(x) + "words.txt"
    with open(fileToUse, 'r') as f:
        dictsToUse[dictName] = f.read()
        f.close
sep, resulttext = "", ""
results = []
i = 0
for x in range(1, stuffLength):
    choices = list(itertools.permutations(stuff, x+1))
    j = 0
    dictName = str(x+1) + "WordDictionary"

    for y in choices:
        if sep.join(y) in dictsToUse[dictName]:
            if sep.join(y) not in results:
                results.append(sep.join(y))
                i += 1
                j += 1
    resulttext += "Total " + str(x+1) + " letter words = " + str(j) + "\n"
print(results)
print("\n")
print(resulttext)
print("Total words: " + str(i))
print("Time taken: ", time.time() - start_time)




'''
wordQuestion = "Please enter the letters you wish to use: "

stuff = str(input(wordQuestion))
start_time = time.time()
with open('files/english3.txt', 'r') as f:
    dictionary = f.read()
    f.close()
dictionary = [x.lower() for x in dictionary.split('\n')]

sep, resulttext = "", ""
results = []
i = 0
for x in range(1, len(stuff)):
    choices = list(itertools.permutations(stuff, x+1))
    j = 0
    #print(str(x+1) + " letter words")
    for y in choices:
        if sep.join(y) in dictionary:
            if sep.join(y) not in results:
                results.append(sep.join(y))
                i += 1
                j += 1
    resulttext += "Total " + str(x+1) + " letter words = " + str(j) + "\n"
print(results)
print("\n")
print(resulttext)
print("Total words: " + str(i))
print("Time taken: ", time.time() - start_time)




d = enchant.Dict("en_GB")
wordQuestion = "Please enter the letters you wish to use: "

stuff = str(input(wordQuestion))
start_time = time.time()

sep, resulttext = "", ""
results = []
i = 0
for x in range(1, len(stuff)):
    choices = list(itertools.permutations(stuff, x+1))
    j = 0
    print(str(x+1) + " letter words")
    for y in choices:
        if d.check(sep.join(y)):
            if sep.join(y) not in results:
                print(sep.join(y))
                results.append(sep.join(y))
                i += 1
                j += 1
    resulttext += "Total " + str(x+1) + " letter words = " + str(j) + "\n"
print(results)
print("\n")
print(resulttext)
print("Total words: " + str(i))
print("Time taken: ", time.time() - start_time)




english_vocab = set(w.lower() for w in nltk.corpus.words.words())

wordQuestion = "Please enter the letters you wish to use: "

stuff = str(input(wordQuestion))
start_time = time.time()

sep, resulttext = "", ""
results = []
i = 0
for x in range(1, len(stuff)):
    choices = list(itertools.permutations(stuff, x+1))
    j = 0
    print(str(x+1) + " letter words")
    for y in choices:
        if (sep.join(y) in english_vocab):
            if sep.join(y) not in results:
                print(sep.join(y))
                results.append(sep.join(y))
                i += 1
                j += 1
    resulttext += "Total " + str(x+1) + " letter words = " + str(j) + "\n"
print(results)
print("\n")
print(resulttext)
print("Total words: " + str(i))
print("Time taken: ", time.time() - start_time)
'''