import time
import re

# Finds the potential words available based on an entry with asterisks as the missing charachters
wordQuestion = "Please enter the word you wish to find with an asterisk for any missing characters: "
wordInput = str(input(wordQuestion))
wordLength = len(wordInput)

fileToUse = "files/" + str(wordLength) + "words.txt"
with open(fileToUse, 'r') as f:
    dictionary = f.read()
    f.close

#searchString = wordInput.replace("*", "[\w\.-]")
#theAnswers = re.findall((searchString), dictionary)
#print(theAnswers)
#theAnswers = re.findall((wordInput.replace("*", "[\w\.-]")), dictionary)
print(re.findall((wordInput.replace("*", "[\w\.-]")), dictionary))


# Solves an anagram of a single word
'''
wordQuestion = "Please enter the anagram: "
scrambled = str(input(wordQuestion))
scrambledLength = len(scrambled)
results=[]

def anagram_check(word,check):
    for letter in word:
        if letter in check:
            check = check.replace(letter, '', 1)
        else:
            return 0
    return 1

def sorting(lst):
    lst.sort(key=len)
    return lst
start_time = time.time()
f=open("files/english3.txt", "r")
for x in f:
    x=x.strip()
    if len(x) == scrambledLength:
        if anagram_check(x,scrambled):
            print(x)
            results.append(x)
f.close()
print(sorting(results))
print("Time taken: ", time.time() - start_time)
'''

# Finds all possible combinations of words within a given character input from 2 characters up
'''
wordQuestion = "Please enter the letters you wish to use: "
scrambled = str(input(wordQuestion))
scrambledLength = len(scrambled)
results=[]

def anagram_check(word,check):
    for letter in word:
        if letter in check:
            check = check.replace(letter, '', 1)
        else:
            return 0
    return 1

def sorting(lst):
    lst.sort(key=len)
    return lst
start_time = time.time()
f=open("files/english3.txt", "r")
for x in f:
    x=x.strip()
    if len(x) <= scrambledLength and len(x) > 1:
        if anagram_check(x,scrambled):
            print(x)
            results.append(x)
f.close()
print(sorting(results))
print("Time taken: ", time.time() - start_time)
'''