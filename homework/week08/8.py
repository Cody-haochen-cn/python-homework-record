from PIL import Image, ImageEnhance
img = Image.open("my_photo.jpg")
enhancer_b = ImageEnhance.Brightness(img)
img_bright = enhancer_b.enhance(5.0)
enhancer_c = ImageEnhance.Contrast(img_bright)
img_final = enhancer_c.enhance(10.0)
img_final.save("自拍照5.jpg")
