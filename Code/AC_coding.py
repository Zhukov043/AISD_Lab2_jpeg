from Huffman_table import AC_luma_Huffman, AC_chr_Huffman
from RLE import rle_encode
from DC_coding import coef_category
import numpy as np

def ac_coding(coefs, is_luma):
    ac_coefs = []
    for blocks in coefs:
        ac_coefs += blocks[1:]

    ac_coefs = [int(round(float(x))) for x in ac_coefs]
    rle_ac = rle_encode(ac_coefs)

    huffman_table = AC_luma_Huffman if is_luma else AC_chr_Huffman
    bitstream = ""

    for zero, amplitude in rle_ac:
        if amplitude == 0 and zero == 0:
            bitstream += huffman_table.get((0, 0), "")
            continue

        while zero >= 16:
            bitstream += huffman_table.get((15, 0), "")
            zero -= 16

        category, amplitude_bits = coef_category(amplitude)
        bitstream += huffman_table[(zero, category)] + amplitude_bits

    return bitstream

def decode_ac_coefficients(bitstream, is_luma):
    huffman_table = AC_luma_Huffman if is_luma else AC_chr_Huffman
    reverse_huffman = {v: k for k, v in huffman_table.items()}

    decoded_coeffs = []
    current_pos = 0

    while current_pos < len(bitstream):
        found = False
        for code_len in range(1, 32):
            if current_pos + code_len > len(bitstream):
                break
            code = bitstream[current_pos:current_pos + code_len]
            if code in reverse_huffman:
                run_length, category = reverse_huffman[code]
                current_pos += code_len
                found = True
                break

        # Обработка EOB
        if run_length == 0 and category == 0:
            decoded_coeffs.append(0)
            continue

        # Обработка ZRL
        if run_length == 15 and category == 0:
            decoded_coeffs.extend([0] * 16)
            continue

        # Декодирование значения
        value = 0
        if category > 0:
            amplitude_bits = bitstream[current_pos:current_pos + category]
            current_pos += category
            amplitude = int(amplitude_bits, 2)

            if amplitude < (1 << (category - 1)):
                value = amplitude - (1 << category) + 1
            else:
                value = amplitude

        if run_length > 0:
            decoded_coeffs.extend([0] * run_length)
        decoded_coeffs.append(value)

    return np.array(decoded_coeffs)

