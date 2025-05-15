from PIL import Image
import numpy as np
from To_blocks import to_blocks
from DCT import dct2
from Quanting import quanting_luma
from ZigZag import zigzag
from DC_coding import dc_coding
from AC_coding import ac_coding
from Pack_data import pack_data_Y

N = 8  # Размер блоков
quality = 95  # Качество изображения
qualityp = quality
image = Image.open("2048_with_diz.png").convert("L")

y_ch = np.array(image, dtype=np.float32)
height, width = y_ch.shape[:2]

y_block = to_blocks(y_ch, N)

luma_array = []
for n in y_block:
    for block in n:
        y_dct = dct2(block)
        y_quant = quanting_luma(y_dct, quality)
        y_list = zigzag(y_quant)
        luma_array.append(y_list)

is_luma = True
luma_dc_coded = dc_coding(luma_array, is_luma)
luma_ac_coded = ac_coding(luma_array, is_luma)

packed = pack_data_Y(
    image_size=(height, width),
    quality=50,
    luma_dc_coded=luma_dc_coded,
    luma_ac_coded=luma_ac_coded,
)

with open(f"output", 'wb') as f:
    f.write(packed)

