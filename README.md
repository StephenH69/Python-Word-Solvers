# Python Word Solvers

A set of basic scripts to help solve word puzzles, including anagram solving, finding a word with characters missing (good for crosswords) and finding all the words within a given string.

The missing letter word finder uses a classic regex algorithm which then searches a file based on the number of characters in the word.

There are four methods in the anagram and word finder files, using different techniques.

### Full Word File
This uses a text file with almost 200,000 GB English words.



### Separate Word Files
This uses separate text files based on the length of the word which have been derived from the larger file using the file splitwordlist.py.




### Enchant
This uses the enchant package set to GB.






### NLTK
This uses the nltk corpus of words.



----------

Willing for others to give advice on how to make these run quicker as would like to use them as the basis for a web app.