from PIL import Image, ImageDraw, ImageFont

dog = Image.open('Dog.jpg')
draw = ImageDraw.Draw(dog)

points = (2000, 1000)
string = "I love Dogs"
font1 = ImageFont.truetype('arial.ttf', 70)

draw.text(points, string, 'Black', font=font1)

dog.show()