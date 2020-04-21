#!/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import CountVectorizer
import jieba

def count_vectorizer():
    data = ['和我预料的一样，在最后快系统确认那天夜里，悄悄的点了一个拒绝。', '那只能走闲鱼小法庭咯，最终结果我胜利。', '到此该同学始终强调自己不懂规则，但是不正面回应我键盘的事情。也不对发韵达的事情做解释。', '作为回报， 我用顺丰到付约33元给该同学一个教训，要明白先做人再做事。']
    data2 = []
    for sent in data:
        data2.append(cut_word(sent))
    transfer = CountVectorizer()
    data_new = transfer.fit_transform(data2)
    print(data_new)
    print(transfer.get_feature_names())

def cut_word(text):
    return ''.join(list(jieba.cut(text)))

if __name__ == "__main__":
    count_vectorizer()