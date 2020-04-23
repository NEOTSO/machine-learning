import pandas as pd
from sklearn.feature_selection import VarianceThreshold

def _VarianceThreshold():
    data = pd.read_csv('./data/factor_returns.csv')
    data_filtered = data.iloc[:, 1:-2]
    print(data_filtered.shape)
    transfer = VarianceThreshold(threshold=10)
    data_new = transfer.fit_transform(data_filtered)
    print(data_new.shape)

if __name__ == '__main__':
    _VarianceThreshold()