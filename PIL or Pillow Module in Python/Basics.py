from PIL import Image
import os

#image1 = Image.open('bird.jpg')
#image1.show()

for f in os.listdir('.'):
    if f.endswith('.jpg'):
        jpgs = Image.open(f)
        fname , fext = os.path.splitext(f)
        jpgs.save('pngs/{}.png'.format(fname))


