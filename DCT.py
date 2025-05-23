import numpy as np

# def get_dct_matrix():
#     n = 8
#     matrix = np.zeros((n, n))
#     for v in range(n):
#         for y in range(n):
#             if v == 0:
#                 matrix[v][y] = 1 / np.sqrt(n)
#             else:
#                 matrix[v][y] = np.sqrt(2 / n) * np.cos((y + 0.5) * v * np.pi / n)
#     return matrix


dct_matrix = np.array([
    [0.35355339, 0.35355339, 0.35355339, 0.35355339, 0.35355339, 0.35355339, 0.35355339, 0.35355339],
    [0.49039264, 0.41573481, 0.27778512, 0.09754516, -0.09754516, -0.27778512, -0.41573481, -0.49039264],
    [0.46193977,  0.19134172, -0.19134172, -0.46193977, -0.46193977, -0.19134172, 0.19134172, 0.46193977],
    [0.41573481, -0.09754516, -0.49039264, -0.27778512, 0.27778512, 0.49039264, 0.09754516, -0.41573481],
    [0.35355339, -0.35355339, -0.35355339, 0.35355339, 0.35355339, -0.35355339, -0.35355339, 0.35355339],
    [0.27778512, -0.49039264, 0.09754516, 0.41573481, -0.41573481, -0.09754516, 0.49039264, -0.27778512],
    [0.19134172, -0.46193977, 0.46193977, -0.19134172, -0.19134172, 0.46193977, -0.46193977, 0.19134172],
    [0.09754516, -0.27778512, 0.41573481, -0.49039264, 0.49039264, -0.41573481, 0.27778512, -0.09754516]
])


def dct2(block):
    block = np.dot(dct_matrix, np.dot(block, dct_matrix.transpose()))
    return block


def idct2(block):
    block = np.dot(dct_matrix.transpose(), np.dot(block, dct_matrix))
    return block