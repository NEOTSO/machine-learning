import pandas as pd
from scipy.stats import pearsonr

def _VarianceThreshold():
    data = pd.read_csv('./data/factor_returns.csv')
    data_filtered = data.iloc[:, 1:-2]
    # print(data_filtered)
    # pe_ratio  pb_ratio    market_cap  return_on_asset_net_profit  ...            ev  earnings_per_share       revenue  total_expense
    print(pearsonr(data['pe_ratio'], data['pb_ratio']))
    print(pearsonr(data['revenue'], data['total_expense']))

if __name__ == '__main__':
    _VarianceThreshold()