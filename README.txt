Title: Analysis of Textual Data 
Author: Kartik Dube 
Date: 2019-02-07 
Description: Build a model for textual data which analyses the given text and returns the following traits - Total number of words, total number of unique words, vocabulary quality.

Python Version: 3.6.8 

-----------------------
Library Used: nltk v3.4
-----------------------
NLTK is one of the leading platforms for working with human language data and Python, the module NLTK is used for natural language processing. NLTK is literally an acronym for Natural Language Toolkit.

## Installation

'''
pip install nltk
'''

-------------------------------
Library Used: langdetect v1.0.7
-------------------------------
Detect language of a text using naive Bayesian filter. 99% accuracy over 53 languages.

## Installation

'''
pip install langdetect
'''

------
Tokens
------
Tokens are individual words and characters from the text, converted into a list.

---------
Tokenizer
---------
A tokenizer converts the text into tokens. We chose RegexpTokenizer since it'll only tokenize words, excluding the characters lke ',' or '.' or '!', because the given assignment deals only with words.

-----------------
Lexical Diversity
-----------------
Lexical Diversity is calculated according:
Herdan's C (Herdan, 1960, as cited in Tweedie & Baayen, 1998; sometimes referred to as LogTTR)

------------------------------------
Graph for 10 Highest Frequency Words
------------------------------------
x-axis: 10-Samples
y-axis: Cumulative count









