# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 10:24:27 2019

@author: dubek
"""

import nltk
from nltk.tokenize import RegexpTokenizer
from langdetect import detect_langs
import math

#Selecting a File
fname = input("Enter the text file's destination:")
raw=open(fname).read()

#RegexpTokenizer: Tokenizes only words
tokens = nltk.RegexpTokenizer(r'\w+').tokenize(raw)
text = nltk.Text(tokens)

#Language
print("\nLanguages Found: ")
print(detect_langs(raw))

#Number of Words
print("\nTotal Number of Words: ") 
print(len(text))

#Number of Unique Words
print("\nNumber of Unique Words: ")
print(len(set(text)))

#Lexical Diversity
#Herdan's C (Herdan, 1960, as /
#cited in Tweedie & Baayen, 1998; sometimes referred to as LogTTR)
ld = math.log(len(text)) / math.log(len(set(text)))
print("\nLexical Diversity:")
print(ld)

#Graph of 10 Highest Frequenty Words
fdist1 = nltk.FreqDist(text) 
fdist1.plot(10, cumulative= True)

    
    
    
    
    