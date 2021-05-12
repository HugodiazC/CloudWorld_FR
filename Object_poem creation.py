
import re
import string


"""Clean  DATASET"""

def clean_text_round1(text):
    '''Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.'''
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text


def clean_text_round2(text):
    '''Get rid of some additional punctuation and non-sensical text that was missed the first time around.'''
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', '', text)
    return text

""" Insetar conjunto de DATOS >>> """
f = open('prueba.txt', encoding="utf-8")
Text_TOKEN = f.read()


#Convertir todo a minúsculas
TEXT_LOWER = Text_TOKEN.lower()


#Utilizar función para limpiar dataset de las stopwords
CLEAN_DATA1 = clean_text_round1(TEXT_LOWER)
CLEAN_DATA2 = clean_text_round1(CLEAN_DATA1)

#Tokenize el data set para poderlo manipular.
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
dataset_tokenize= word_tokenize(CLEAN_DATA2)
len(CLEAN_DATA2)

# Text Generation
"""Build a Markov Chain Function
We are going to build a simple Markov chain function that creates a dictionary:

The keys should be all of the words in the corpus
The values should be a list of the words that follow the keys """

from collections import defaultdict


def markov_chain(text):
    '''The input is a string of text and the output will be a dictionary with each word as
       a key and each value as the list of words that come after the key in the text.'''

    # Tokenize the text by word, though including punctuation
    words = text.split(' ')

    # Initialize a default dictionary to hold all of the words and next words
    m_dict = defaultdict(list)

    # Create a zipped list of all of the word pairs and put them in word: list of next words format
    for current_word, next_word in zip(words[0:-1], words[1:]):
        m_dict[current_word].append(next_word)

    # Convert the default dict back into a dictionary
    m_dict = dict(m_dict)
    return m_dict

project_dict = markov_chain(CLEAN_DATA2)

import random

def generate_sentence(chain, count=30):
    '''Input a dictionary in the format of key = current word, value = list of next words
       along with the number of words you would like to see in your generated sentence.'''

    # Capitalize the first word
    word1 = random.choice(list(chain.keys()))
    sentence = word1.capitalize()

    # Generate the second word from the value list. Set the new word as the first word. Repeat.
    for i in range(count-1):
        word2 = random.choice(chain[word1])
        word1 = word2
        sentence += ' ' + word2

    # End it with a period
    sentence += '.'
    return(sentence)

print(generate_sentence(project_dict))