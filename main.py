import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')





# for tweet in tweets:
#     # print(tweet)
#     tweet = tweet.replace("!", " ")
#     tweet = tweet.replace("?", " ")
#     tweet = tweet.replace("\"", " ")
#     tweet = tweet.replace("\'", " ")
#     tweet = tweet.replace(".", " ")
#     tweet = tweet.replace(",", " ")
#     tweets_clean.append(tweet)
#     # tweets_clean.append(tweet.replace("", " "))
#     # tweets_clean.append(tweet.replace("!", " "))
#     # tweets_clean.append(tweet.replace("!", " "))


def remove_URL(sample):
    """Remove URLs from a sample string"""
    return re.sub(r"http\S+", "", sample)


def generate_dictionary(text):
    word_to_index = dict()
    index_to_word = dict()
    corpus = []
    count = 0
    vocab_size = 0

    for sentence in text:

        for word in sentence.split():
            if not "http" in word and not "com/" in word and not "gov/" in word and not "tv/" in word and not "org/" in word:
                word = word.lower()
                corpus.append(word)
                if word_to_index.get(word) == None:
                    word_to_index.update({word: count})
                    index_to_word.update({count: word})
                    count += 1
    vocab_size = len(word_to_index)
    length_of_corpus = len(corpus)

    return word_to_index, index_to_word, corpus, vocab_size, length_of_corpus

stop_words = set(stopwords.words("english"))
stop_word_list = []
for w in stop_words:
    stop_word_list.append(w)
print(stop_words)

punc_string = "! \" # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \\ ] ^ _ ` { | } ~ .. ... !!! !!!! ?? ???"
punc_list = punc_string.split(" ")
print(punc_list)



trumpdf = pd.read_csv('realdonaldtrump.csv')
trumpdf2 = pd.read_csv('trumptweets.csv')
print(trumpdf.columns)
print(trumpdf2.columns)
tweets = []
tweets_clean = []
sentences = []
sentences_clean = []
words = []
words_clean = []


for index, row in trumpdf.iterrows():
    tweets.append(row['content'])
for index, row in trumpdf2.iterrows():
    tweets.append(row['content'])

for tweet in tweets:
    tweet = remove_URL(tweet)
    sentences.append(nltk.sent_tokenize(tweet))
    words.append(nltk.word_tokenize(tweet))


for word in words:
    if word in stop_word_list or word in punc_list:
        print(word)

    if word not in stop_word_list and word not in punc_list:
        words_clean.append(word)
# word_to_index, index_to_word, corpus, vocab_size, length_of_corpus = generate_dictionary(tweets_clean)

