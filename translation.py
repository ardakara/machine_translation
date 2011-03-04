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
    line = normalize(line)
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
  tokens = string.split()
  result = ''
  for token in tokens:
    if len(token) == 0:
      continue
    # Sometimes, words will have punctuation attached.  Usually at the end.
    # In our case, we only have commas and periods to deal with, and never both.
    
    word = token
    punct = ''
    if token[-1] == '.' or token[-1] == ',':
      word = token[0:-1]
      punct = token[-1]
    
    if word in dictionary:
      translated = dictionary[word]
      result += dictionary[word] + punct + ' '
    else:
      print 'Error: ' + word + ' not in dictionary.  Skipping word...'
  return result

# Convert all letters to lower case
def normalize(source):
  normalize = ''
  for ch in source:
    upperIdx = string.ascii_uppercase.find(ch)
    if upperIdx >= 0:
      normalize += string.ascii_lowercase[upperIdx]
    else:
      normalize += ch
  return normalize
      
      
  
readDictionary('dictionary.txt')
source = readFile('source.txt')
normalized = normalize(source)
print translateWords(normalized)

# should we also restore capitalization?

