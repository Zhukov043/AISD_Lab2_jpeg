from PIL import Image

img = Image.open("Test2048.png")

#grayscale
gray = img.convert("L")
gray.save("2048_gray.png")

#чб без дизеринга
bw_no_dither = gray.point(lambda x: 255 if x > 128 else 0, mode='1')
bw_no_dither.save("2048_no_diz.png")

#чб с дизерингом
bw_dither = gray.convert("1")
bw_dither.save("2048_with_diz.png")