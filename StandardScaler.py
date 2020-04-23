#!/usr/bin/python
# -*- coding: utf-8 -*-
from sklearn.preprocessing import StandardScaler
import pandas as pd

def _StandardScaler():
    data = pd.read_csv('./data/dating.txt').iloc[:, :3]
    print(data)
    transfer = StandardScaler()
    data_new = transfer.fit_transform(data)
    print(data_new)

if __name__ == "__main__":
    _StandardScaler()