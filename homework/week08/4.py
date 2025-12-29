from PIL import Image
img = Image.open("my_photo.jpg")
img.thumbnail((128, 128))
img.save("自拍照1.jpg")
img = Image.open("自拍照1.jpg")
print("图片大小:", img.size)
