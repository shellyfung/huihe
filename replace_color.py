from PIL import Image

img = Image.open("4.png")
(w, h) = img.size
# print(w, h)

""" replace white to black """
for i in range(w):
    for j in range(h):
        try:
            r, g, b, alpha = img.getpixel((i, j))
            if r >= 100 and g >= 100 and b >= 100:
                r = 0
                g = 0
                b = 0
                img.putpixel((i, j), (r, g, b, alpha))
        except Exception as e:
            continue
img.save("33.png")
src = Image.open("33.png")

""" replace blue to white """
for i in range(w):
    for j in range(h):
        try:
            r, g, b, alpha = src.getpixel((i, j))
            if b > g and b > r:
                r = 255
                g = 255
                b = 255
                src.putpixel((i, j), (r, g, b, alpha))
        except Exception as e:
            continue
# src.show()
src.save("3.png")