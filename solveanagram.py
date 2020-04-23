# A selection of methods to solve anagrams


import itertools
import nltk
from nltk.corpus import words
import time
import enchant
from collections import Counter
import sys


wordQuestion = "Please enter the letters you wish to use: "
scramble = str(input(wordQuestion))
start_time = time.time()

fileToUse = "files/" + str(len(scramble)) + "words.txt"
with open(fileToUse, 'r') as f:
    wordDictionary = f.read()
    f.close
wordDictionary = [x.lower() for x in wordDictionary.split('\n')]
sep = ""
for y in list(itertools.permutations(scramble, len(scramble))):
    if sep.join(y) in wordDictionary:
        print(sep.join(y))
print("Time taken: ", time.time() - start_time)




wordQuestion = "Please enter the letters you wish to use: "
scramble = str(input(wordQuestion))
start_time = time.time()

with open('files/english3.txt', 'r') as f:
    dictionary = f.read()
    f.close()
dictionary = [x.lower() for x in dictionary.split('\n')]

sep = ""
for y in list(itertools.permutations(scramble, len(scramble))):
    if sep.join(y) in dictionary:
        print(sep.join(y))
print("Time taken: ", time.time() - start_time)



wordQuestion = "Please enter the letters you wish to use: "
scramble = str(input(wordQuestion))
start_time = time.time()
d = enchant.Dict("en_GB")
sep = ""
for y in list(itertools.permutations(scramble, len(scramble))):
    if d.check(sep.join(y)):
        print(sep.join(y))
print("Time taken: ", time.time() - start_time)




wordQuestion = "Please enter the letters you wish to use: "
scramble = str(input(wordQuestion))
start_time = time.time()
english_vocab = set(w.lower() for w in nltk.corpus.words.words())
sep = ""
for y in list(itertools.permutations(scramble, len(scramble))):
    if (sep.join(y) in english_vocab):
        print(sep.join(y))
print("Time taken: ", time.time() - start_time)


