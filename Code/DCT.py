import numpy as np

def dct_matrix(N):
    n = np.arange(N)
    k = n.reshape(N, 1)
    # Коэффициенты масштабирования
    C = np.where(n == 0, 1 / np.sqrt(2), 1) * np.sqrt(2 / N)
    # Ядро DCT
    return C * np.cos((2 * k + 1) * n * np.pi / (2 * N))


def dct2(block):
    D = dct_matrix(block.shape[0])
    return D @ block @ D.T  # Эквивалентно двум 1D DCT


def idct2(dct_block):
    D = dct_matrix(dct_block.shape[0])
    return D.T @ dct_block @ D