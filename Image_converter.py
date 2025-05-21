from PIL import Image

img = Image.open("Lenna.png")

#grayscale
gray = img.convert("L")
gray.save("Lenna_gray.png")

#чб без дизеринга
bw_no_dither = gray.point(lambda x: 255 if x > 128 else 0, mode='1')
bw_no_dither.save("Lenna_no_diz.png")

#чб с дизерингом
bw_dither = gray.convert("1")
bw_dither.save("Lenna_with_diz.png")