from PIL import Image

#pl = Image.open('Dog.jpg')
#cpl = Image.open('Dog_Grayscale.jpg')

#image_blend = Image.blend(pl, cpl, 0.5)
#image_blend.show()


pl = Image.open('PythonLogo.png')
cpl = Image.open('ChangedPythonLogo.png')

image_composite = Image.composite(pl, cpl, pl)
image_composite.show()