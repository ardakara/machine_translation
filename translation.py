#!/usr/bin/python

# CS 124 Assignment 7
# Machine Translation
# 
# Arda Kara
# Jason Ma

import string

dictionary = dict()
partsOfSpeech = dict()

def readDictionary(file):
  dictFile = open(file, 'r')
  lines = dictFile.read().split('\n')
  for line in lines:
    line = normalize(line)
    wordpair = line.split('#')
    if len(wordpair) > 2:
      dictionary[wordpair[0]] = wordpair[1]
      partsOfSpeech[wordpair[0]] = wordpair[2]
    else:
      print 'Error: malformed entry in dictionary. ' + line
  dictFile.close()

def readFile(file):
  sourceFile = open(file, 'r')
  fileText = sourceFile.read()
  sourceFile.close()
  return fileText

# returns a three-element list:
#   1. the string of the result, complete with punctuation added back in
#   2. a list of the words from the translation
#   3. a list of the parts of speech corresponding to the previous list
def translateWords(string):
  tokens = string.split()
  #result = ''
  translatedWords = [[]]
  pos = [[]]
  for token in tokens:
    # Sometimes, words will have punctuation attached.  Usually at the end.
    # In our case, we only have commas and periods to deal with, and never both.
    
    word = token
    punct = ''
    if token[-1] == ',':
      word = token[0:-1]
      punct = token[-1]
      
    if token[-1] == '.':
      word = token[0:-1]
      punct = token[-1]
    
    if word in dictionary:
      translated = dictionary[word]
      #result += dictionary[word] + punct + ' '
      translatedWords[-1].append(dictionary[word] + punct)
      pos[-1].append(partsOfSpeech[word])
      if punct == '.':
        translatedWords.append([])
        pos.append([])
    else:
      print 'Error: ' + word + ' not in dictionary.  Skipping word...'
  return [translatedWords[0:-1], pos[0:-1]]

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
      
def applyReorderingRules(translation):
  for i in xrange(0, len(translation[1])):
    sentence = translation[0][i]
    pos = translation[1][i]
    
    for j in xrange(0, len(pos) - 1):
      if pos[j] == 'noun' and pos[j+1] == 'verb':
        temp = sentence[j]
        sentence[j] = sentence[j+1]
        sentence[j+1] = temp
        pos[j+1] = 'noun'
        pos[j] = 'verb'

    translation[0][i] = sentence
    translation[1][i] = pos

def fixPeriods(translation):
  for sIdx in xrange(len(translation[0])):
    sentence = translation[0][sIdx]
    for i in xrange(len(sentence)):
      word = sentence[i]
      if '.' in word:
        sentence[i] = word[0:-1]
    translation[0][sIdx][-1] += '.'
    
readDictionary('dictionary.txt')
source = readFile('source.txt')
sourceSeg = source.split('.')
normalized = normalize(source)
translation = translateWords(normalized)

applyReorderingRules(translation)

fixPeriods(translation)

for i in xrange(0, len(translation[1])):
  print sourceSeg[i]
  print string.join(translation[0][i], ' ')
  
  print translation[0][i]
  print translation[1][i]
  print ''

# should we also restore capitalization?

