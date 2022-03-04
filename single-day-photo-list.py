import os
import os.path
import random
from PIL import Image
from datetime import date

vanomad_images = os.listdir("/Users/omnisonic/Documents/code/MyWebDev/Python Static Sites/Pelican/vanomad/content/images/2021")

vanomad_images.append(os.listdir("/Users/omnisonic/Documents/code/MyWebDev/Python Static Sites/Pelican/vanomad/content/images"))

dir = "/Users/omnisonic/pCloud Drive/Automatic Upload/iPhoneSE2G/"
listAll = os.listdir(dir)
dayList = []
# dayRndm = random.choice(listAll)
# date = dayRndm.split(' ')[0] # the split() split at the space and discards after the space so only the date on not the timestamp
alreadyExists = True
while alreadyExists:
    dayRndm = random.choice(listAll)
    date = dayRndm.split(' ')[0]
    if date in vanomad_images:
        print(f"{date} already exists, trying again for another date")
        continue
    alreadyExists = False


for item in listAll:
    if "mov" in item:
        continue
    if date in item:  
        dayList.append(item)
print(len(listAll))

print(dayList)

if len(dayList) > 15:
    newList = []
    for item in range(15):
        newList.append(random.choice(dayList))
    dayList = newList    

print(f'this is the new newlist len {len(dayList)}')

# process the image
size_700 = (700,700)
size_1000 = (1000, 1000)

savePath = 'content/images/'
os.mkdir(f'{savePath}{date}')  # make a new folder named by the date of collected photos
for f in dayList:
    if f.endswith('.jpeg'):
        i = Image.open(f'{dir}{f}')
        fn, fext = os.path.splitext(f)

        i.thumbnail((size_1000))
        #    i.save(str(savePathDir) + '{}{}'.format(fn, fext))
        i.save(f'{savePath}{date}/{fn}{fext}')


###### Todo: Here we will build the markdown page for pelican to process


###### ---before i can integrate the page build script i need to do fix the exif issue.----#####