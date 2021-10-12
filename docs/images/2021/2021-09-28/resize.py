from PIL import Image
import os


#size_300 = (300)
size_700 = (700,700)
size_1000 = (1000, 1000)

for f in os.listdir('.'):
   if f.endswith('.JPG'):
       i = Image.open(f)
       fn, fext = os.path.splitext(f)

       i.thumbnail((size_1000))
       i.save('{}{}'.format(fn, fext))

        # i.thumbnail(size_300)
        # i.save('{}_300{}'.format(fn, fext))
