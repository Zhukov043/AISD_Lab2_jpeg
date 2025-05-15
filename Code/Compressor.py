from PIL import Image
from Converter import converter
from Downsampling import downsampling
from To_blocks import to_blocks
from DCT import dct2
from Quanting import quanting_luma, quanting_chr
from ZigZag import zigzag
from DC_coding import dc_coding
from AC_coding import ac_coding
from Pack_data import pack_data

N = 8   #Размер блоков
quality = 0   #Качество изображения

image = Image.open("Lenna.png").convert("RGB")

ycbcr = converter(image)
height, width = ycbcr.shape[:2]

DS_image = downsampling(ycbcr)

y_ch = DS_image['y']
cb_ch = DS_image['cb']
cr_ch = DS_image['cr']

y_block = to_blocks(y_ch, N)
cb_block = to_blocks(cb_ch, N)
cr_block = to_blocks(cr_ch, N)

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


cb_array = []
for n in cb_block:
    for block in n:
        cb_dct = dct2(block)
        cb_quant = quanting_chr(cb_dct, quality)
        cb_list = zigzag(cb_quant)
        cb_array.append(cb_list)

is_luma = False
cb_dc_coded = dc_coding(cb_array, is_luma)
cb_ac_coded = ac_coding(cb_array, is_luma)


cr_array = []
for n in cr_block:
    for block in n:
        cr_dct = dct2(block)
        cr_quant = quanting_chr(cr_dct, quality)
        cr_list = zigzag(cr_quant)
        cr_array.append(cr_list)

is_luma = False
cr_dc_coded = dc_coding(cr_array, is_luma)
cr_ac_coded = ac_coding(cr_array, is_luma)

packed = pack_data(
        image_size=(height, width),
        quality=quality,
        luma_dc_coded=luma_dc_coded,
        luma_ac_coded=luma_ac_coded,
        cb_dc_coded=cb_dc_coded,
        cb_ac_coded=cb_ac_coded,
        cr_dc_coded=cr_dc_coded,
        cr_ac_coded=cr_ac_coded
    )

with open("output", 'wb') as f:
    f.write(packed)
