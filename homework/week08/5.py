from PIL import Image
img = Image.open("my_photo.jpg")
gray_img = img.convert('L')
gray_img.save("自拍照2.jpg")
img = Image.open("自拍照2.jpg")
print("色彩模式:", img.mode)
