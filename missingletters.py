# Finds the potential words available based on an entry with asterisks as the missing charachters

import re

def main():
    wordQuestion = "Please enter the word you wish to find with an asterisk for any missing characters: "
    wordInput = str(input(wordQuestion))
    wordLength = len(wordInput)

    fileToUse = "files/" + str(wordLength) + "words.txt"
    with open(fileToUse, 'r') as f:
        dictionary = f.read()
        f.close
     
    searchString = wordInput.replace("*", "[\w\.-]")
    theAnswers = re.findall(searchString, dictionary)
    
    print(theAnswers)

if __name__ == '__main__':
    main()
