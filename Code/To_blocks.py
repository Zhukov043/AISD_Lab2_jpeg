import numpy as np

def to_blocks(channel, N):
    h, w = channel.shape

    blocks_h = h // N
    blocks_w = w // N
    if h%N != 0:
        channel = np.pad(channel, ((0, (N - (h % N)) % N), (0, (N - (w % N)) % N)),
                        mode='constant', constant_values=0)
        blocks_h += 1
        blocks_w += 1

    blocks = []
    for i in range(blocks_h):
        row_blocks = []
        for j in range(blocks_w):
            block = channel[
                i * N : (i + 1) * N,
                j * N : (j + 1) * N
            ]
            row_blocks.append(block)
        blocks.append(row_blocks)

    return blocks