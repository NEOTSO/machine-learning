#!/usr/bin/python
# -*- coding: utf-8 -*-
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def _MinMaxScale():
    data = pd.read_csv('./data/dating.txt').iloc[:, :3]
    print(data)
    transfer = MinMaxScaler()
    data_new = transfer.fit_transform(data)
    print(data_new)

if __name__ == "__main__":
    _MinMaxScale()