# Write your code here
import random

from nltk.tokenize import WhitespaceTokenizer
from collections import defaultdict

file_name = r'D:\Python\TG\Text Generator\task\text_generator\corpus.txt'
with open(file_name, "r", encoding="utf-8") as f:
    var_file = f.read()
tk = WhitespaceTokenizer()
tokenized_seq = tk.tokenize(var_file)

set_up = set()
punct_marks = '.?!'
for i in range(len(tokenized_seq)):
    if tokenized_seq[i][0].isupper() and tokenized_seq[i][-1] not in punct_marks:
        set_up.add(tokenized_seq[i])


def bigram(seq):
    list_bigram = [] * (len(seq) - 1)
    for i in range(len(seq) - 1):
        list_bigram.append((seq[i], seq[i + 1]))
    return list_bigram


def trigram(seq):
    list_trigram = [] * (len(seq) - 2)
    for iter_trig in range(len(seq) - 2):
        list_trigram.append((' '.join([seq[iter_trig], seq[iter_trig + 1]]), seq[iter_trig + 2]))
    return list_trigram


def reorg_ngrams(ngrams):
    dct_ngram = defaultdict(lambda: defaultdict(int))
    for ngram in ngrams:
        dct_ngram[ngram[0]][ngram[1]] += 1
    return dct_ngram


def print_dct(dct, key):
    print('Head:', key)
    for key, value in dct[key].items():
        print(f'Tail: {key}', ' ' * (10 - len(key)), f'Count: {value}')


def generate_sentence_trigrams(dct):
    first_word = random.choice(list(dct))
    while not first_word.split()[0].isupper() or first_word.split()[0][-1] in punct_marks:
        first_word = random.choice(list(dct))
    sentence = first_word.split()
    while sentence[-1][-1] not in punct_marks or len(sentence) < 5:
        second_word = random.choices(list(dct[first_word].keys()), weights=list(dct[first_word].values()))[0]
        sentence.append(second_word)
        first_word = ' '.join(' '.join(sentence).split()[-2:])
        # print(sentence)
    return ' '.join(sentence)


dct_bigrams = bigram(tokenized_seq)
dct_trigrams = trigram(tokenized_seq)
new_dct = reorg_ngrams(dct_trigrams)
for _ in range(10):
    print(generate_sentence_trigrams(new_dct))