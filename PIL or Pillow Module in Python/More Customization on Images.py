from PIL import Image, ImageFilter
import os

#image1 = Image.open('bird.jpg')
#image1.show()

#new_size = (500,500)

#for f in os.listdir('.'):
#    if f.endswith('.jpg'):
 #       jpgs = Image.open(f)
 #       fname , fext = os.path.splitext(f)
#      jpgs.thumbnail(new_size)
 #       jpgs.save('500size/{}{}'.format(fname, fext))


dog = Image.open('Dog.jpg')
#dog.convert(mode='L').save("Dog_Grayscale.jpg")

#dog.rotate(450).save("Dog_Grayscale.jpg")

dog.filter(ImageFilter.GaussianBlur(20)).save("Dog_Grayscale.jpg")