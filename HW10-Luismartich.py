
"""
Luis Martich
CS 100 2019F Section 107
HW 10, Nov 1st, 2019
"""

import string

# Problem 1
def initialLetterCount(wordList):
    words = open(wordList, 'r')
    List = words.read().split()
    wordList = []
    for i in List:
        wordList.append(i.strip(string.punctuation))
    dicT = {}
    first = " "
    for item in wordList:
      first = first + item[0]
      dicT[item[0]] = first.count(item[0])
    return (dicT)
print(initialLetterCount('poem.txt'), '\n')


# Problem 2
def initialLetters(wordList):
    words = open(wordList, 'r')
    List = words.read().split()
    wordList = []
    for i in List:
        wordList.append(i.strip(string.punctuation))
    dicT = {}
    for item in wordList:
      if not item[0] in dicT:
        dicT[item[0]] =[item]
      elif item not in dicT[item[0]]:
        dicT[item[0]].append(item)        
    return (dicT)
print(initialLetters('poem.txt'), '\n')


# Problem 3
def shareALetter(wordList):
    words = open(wordList, 'r')
    List = words.read().split()
    wordList = []
    for i in List:
        wordList.append(i.strip(string.punctuation))
    dicT = {}
    for item in wordList:
      if item not in dicT: 
        value = []
        for p in item:
          for token in wordList:
            if p in token:
              if token not in value:
                value.append(token)
        dicT[item] = value
    return(dicT)
print(shareALetter('poem.txt'), '\n')




