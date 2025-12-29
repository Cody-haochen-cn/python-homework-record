from PIL import Image, ImageFilter
img = Image.open("my_photo.jpg")
contour_img = img.filter(ImageFilter.CONTOUR)
contour_img.save("自拍照4.jpg")
