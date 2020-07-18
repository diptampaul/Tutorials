from PIL import Image

image1 = Image.open('PythonLogo.png')

size = width, height = image1.size

#print(image1.getcolors(width * height))

coordinate = x,y = 450, 400

#print(image1.getpixel(coordinate))


print(list(image1.getdata()))