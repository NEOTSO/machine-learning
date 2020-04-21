#!/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import CountVectorizer

def count_vectorizer():
    data = ['life is short, i like python', 'life is too long, i dislike python']

    transfer = CountVectorizer()
    data_new = transfer.fit_transform(data)
    print(data_new)
    print(transfer.get_feature_names())

if __name__ == "__main__":
    count_vectorizer()