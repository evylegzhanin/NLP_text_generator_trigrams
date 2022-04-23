# Write your code here
import random
from nltk.tokenize import WhitespaceTokenizer
from collections import defaultdict

# Get a corpus of text
file_name = 'corpus.txt'
with open(file_name, "r", encoding="utf-8") as f:
    var_file = f.read()
# Creating tokens with 'space' delimiter
tk = WhitespaceTokenizer()
# Tokenizing the corpus
tokenized_seq = tk.tokenize(var_file)


def trigram(seq: 'list of tokens') -> 'list of trigrams':
    """Creates a list of all possible trigrams to process"""
    list_trigram = []
    for iter_trig in range(len(seq) - 2):
        list_trigram.append((' '.join([seq[iter_trig], seq[iter_trig + 1]]), seq[iter_trig + 2]))
    return list_trigram


def reorg_ngrams(ngrams: list) -> dict:
    """Reorganizes a list to a dictionary and calculates the frequency of each head-tail pair"""
    dct_ngram = defaultdict(lambda: defaultdict(int))
    for ngram in ngrams:
        dct_ngram[ngram[0]][ngram[1]] += 1
    return dct_ngram


def print_dct(dct, key):
    """Prints dictionary in a head-tail form"""
    print('Head:', key)
    for key, value in dct[key].items():
        print(f'Tail: {key}', ' ' * (10 - len(key)), f'Count: {value}')


def generate_sentence_trigrams(dct: dict) -> str:
    """Creates a sentence based on trigrams"""
    first_word = random.choice(list(dct))
    punct_marks = '.?!'
    # As a first word, choosing a word that starts with a capital letter and not ends with a punctuation mark
    while not first_word.split()[0].isupper() or first_word.split()[0][-1] in punct_marks:
        first_word = random.choice(list(dct))
    sentence = first_word.split()
    # Running a loop to create sentence with more than 4 words and ending with a punctuation mark
    while sentence[-1][-1] not in punct_marks or len(sentence) < 5:
        second_word = random.choices(list(dct[first_word].keys()), weights=list(dct[first_word].values()))[0]
        sentence.append(second_word)
        first_word = ' '.join(' '.join(sentence).split()[-2:])
    return ' '.join(sentence)


# Get a list of trigrams
list_trigrams = trigram(tokenized_seq)
# Convert the list of trigrams to a dictionary
new_dct = reorg_ngrams(list_trigrams)
# Set a number of sentences to print
number_of_sentences = 10
# Print sentences
for _ in range(number_of_sentences):
    print(generate_sentence_trigrams(new_dct))
