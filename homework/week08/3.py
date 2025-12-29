from PIL import Image
img = Image.open("my_photo.jpg")
print("图片格式:", img.format)
print("色彩模式:", img.mode)
print("图片大小:", img.size)
