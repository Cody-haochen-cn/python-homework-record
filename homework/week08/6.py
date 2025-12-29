from PIL import Image
img = Image.open("my_photo.jpg")
r, g, b = img.split()
new_img = Image.merge("RGB", (b, r, g))
new_img.save("自拍照3.jpg")
