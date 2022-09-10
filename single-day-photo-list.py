import os
import os.path
import random
from PIL import Image
from datetime import date
import config  #this is a seperate file that contains the path to the folder of photos

vanomad_images = os.listdir("./content/images/2021") # existing articles

vanomad_images.append(os.listdir("./content/images")) # existing articles

dir = config.photo_dir
listAll = os.listdir(dir)
list22 = []
for f in listAll: # looping thought to filter the date
    if f.startswith('2022'):
        list22.append(f)
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


for item in list22:
    if "mov" in item:
        continue
    if date in item:  
        dayList.append(item)
print(len(listAll))

def getDateNeighborPhotos(neighboringDate):
    list = []
    for date  in list22:
        if neighboringDate in date:
            list.append(date)
    return  list

# TODO: if the day list is less then 15 find another the next nearest date and get the remainder of photos.

# TODO: or if there are less then 15 photos in a day folder: go fecht the remainder from the nearest next date

# nearest date == date

print(dayList)
print(f'This is the date:  {date}')
def incrementDate(date):
    chars = [number for number in date]  #convert string to list
    last_two = date[8:10]  #get the portion of the date representing the day
    int_last_two = int(last_two) #turn the day in to an integer
    if int_last_two <29: # make sure integer is less the the days of a month
        int_last_two += 1 # add 1 to the day of the month
    if int_last_two > 28: # make sure integer is less the the days of a month
        int_last_two -= 1 # subtract 1 from the day of the month

    last_two = list(str(int_last_two))  #turn it back to a list
    if len(last_two) < 2:
       last_two.insert(0,'0')

    chars.pop()  #remove a char from original list
    chars.pop() #romve anothe char
    neighboringDate = chars + last_two  #conctatenate the two lists
    neighboringDateStr = ''
    neighboringDateStr = neighboringDateStr.join(neighboringDate)
    date = neighboringDateStr
    return date





while len(dayList) < 15:  # add DateNeighbor photos to daylist if list  is less then 15 
    print("list is less then 15, getting neighboring date photos")

    dayList += getDateNeighborPhotos(date) 
    date = incrementDate(date)
    print(f'this is the neighboring date: {date}')


if len(dayList) > 15:  # reduces list to max 15
    newList = []
    for item in range(15):
        newList.append(random.choice(dayList))
    dayList = newList    




print(f'this is the new newlist len {len(dayList)}')


print(dayList)

# process the image
size_700 = (700,700)
size_1000 = (1000, 1000)


def saveListOfDayPhotos():
    
    savePath = 'content/images/'
    os.mkdir(f'{savePath}{date}')  # make a new folder named by the date of collected photos
    for f in dayList:
        if f.endswith('.jpeg'):
            i = Image.open(f'{dir}{f}')
            fn, fext = os.path.splitext(f)

            i.thumbnail((size_1000))
            #    i.save(str(savePathDir) + '{}{}'.format(fn, fext))
            i.save(f'{savePath}{date}/{fn}{fext}')

saveListOfDayPhotos()
###### Todo: Here we will build the markdown page for pelican to process


###### ---before i can integrate the page build script i need to do fix the exif issue.----#####

