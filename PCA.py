from sklearn.decomposition import PCA

def _PCA():
    data = [
        [2, 8, 4, 5],
        [6, 3, 0, 8],
        [5, 4, 9, 1]
    ]
    # transfer = PCA(n_components=2)
    transfer = PCA(n_components=0.95)
    data_new = transfer.fit_transform(data)
    print(data_new)

if __name__ == "__main__":
    _PCA()