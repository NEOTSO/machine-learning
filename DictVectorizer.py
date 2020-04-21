#!/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn.feature_extraction import DictVectorizer

def dict_vectorizer():
    data = [
        { 'city': '北京', 'temperature': 50 },
        { 'city': '上海', 'temperature': 100 },
        { 'city': '广州', 'temperature': 70 }
    ]

    transfer = DictVectorizer(sparse=True)
    data_new = transfer.fit_transform(data)
    print(data_new)
    print(type(data_new))
    print(data_new.toarray())
    print(transfer.feature_names_)
    print(transfer.get_feature_names())

if __name__ == "__main__":
    dict_vectorizer()