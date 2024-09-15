from PIL import Image, ImageDraw, ImageFont, ImageFilter
# Open an image
img = Image.open("C:/Users/Rohit/OneDrive/Pictures/wall.png")

# ⁡⁢⁣⁢Draw and text image⁡
# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype("Arial.ttf", 36)
# draw.text((50,50), "Hello World", font=font, fill="Red")
# draw.rectangle([10,10,150,150], outline="White", width=10)
# img.show()

# ⁡⁢⁣⁢img resizing⁡
# img = img.resize((200,500))
# img.show()


# ⁡⁢⁣⁢img rotate⁡
# img = img.rotate(120)
# img.show()

# ⁡⁢⁣⁢img flip⁡
# img = img.transpose(Image.FLIP_LEFT_RIGHT)
# img.show()
# img = img.transpose(Image.FLIP_TOP_BOTTOM)
# img.show()

# ⁡⁢⁣⁢img filter⁡
# img = img.filter(ImageFilter.DETAIL)
# img.show()

# ⁡⁢⁣⁢convert image mode⁡
img_gray = img.convert("1")
img_gray.show()
