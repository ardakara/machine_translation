# CS 124 Assignment 7
# Machine Translation
# 
# Arda Kara
# Jason Ma

dictionary = dict()

def readDictionary(file):
  dictFile = open(file, 'r')
  lines = dictFile.read().split('\n')
  for line in lines:
    wordpair = line.split('#')
    if len(wordpair) > 1:
      dictionary[wordpair[0]] = wordpair[1]
  dictFile.close()

def readFile(file):
  sourceFile = open(file, 'r')
  file = sourceFile.read()
  sourceFile.close()
  return file
      
def translateWords(string):
  words = string.split(' ')
  result = ''
  for word in words:
    result += dictionary[word] + ' '
  return result
    
readDictionary('dictionary.txt')
source = readFile('source.txt')
print translateWords(source)