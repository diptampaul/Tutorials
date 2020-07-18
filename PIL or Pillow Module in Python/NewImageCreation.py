from PIL import Image

size = width, height = 400, 300

im = Image.new('RGB', size, 'hsl(250, 100%, 50%)')
im.show()