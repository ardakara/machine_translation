# CS 124 Assignment 7
# Machine Translation
# 
# Arda Kara
# Jason Ma

import string

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
  fileText = sourceFile.read()
  sourceFile.close()
  return fileText
      
def translateWords(string):
  words = string.split(' ')
  result = ''
  for word in words:
    result += dictionary[word] + ' '
  return result

# Convert all letters to lower case and remove punct
def normalize(source):
  normalize = ''
  for ch in source:
    upperIdx = string.ascii_uppercase.find(ch)
    if upperIdx >= 0:
      normalize += string.ascii_lowercase[upperIdx]
    else
      normalize += ch
  return normalize
      
      
  
readDictionary('dictionary.txt')
source = readFile('source.txt')
normalized = normalize(source)
print translateWords(normalized)

# need to restore punctuation somehow
# perhaps also restore capitalization?

