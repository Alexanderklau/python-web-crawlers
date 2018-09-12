from PIL import Image,ImageFilter

kitten = Image.open("cook.png")
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save("cook(1).png")
blurryKitten.show()