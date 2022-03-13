from datetime import date
import os
from PIL import Image

folderDate = "2021-12-05" #date of article , same name as folder name

# change this date for each post.  posts built on day / folder of images
post_images_dir = f'/Users/omnisonic/Documents/code/MyWebDev/Python Static Sites/Pelican/vanomad/content/images/2021/{folderDate}' #"images/2021/" + folderDate
photoList = os.listdir(post_images_dir)
photoList.sort()
# get the base from the posts' /images subfolder.  The subfolders will be the named after the date the photos were taken 
# base_name = os.path.basename(post_images_dir)
ext_name  = '.md'

# splits the date (image folder name, same name as md file name into 3 variables for the delta)
post_y, post_m, post_d = folderDate.rsplit('-')

#  counts the days since i started
d0 = date(2021, 4, 8)
dx = date(int(post_y), int(post_m),int( post_d))
delta = dx - d0
day_Nbr = str(delta.days)

post_title = 'Day ' + day_Nbr + ' - '

file_name = folderDate + 'Day' + day_Nbr + ext_name
md_title = 'Title: ' + post_title
md_date = 'Date: ' +  folderDate
md_category = 'Category: '
md_tags = 'Tags: '
md_summary = ''


#write the file
f = open(f"content/{file_name}", 'w')
f.write(f'''{md_title}
{md_date} 
{md_category} 
{md_tags}
Summary:
''')
f.close()


#loop through post images and generate md / html
for file in photoList:
   if file.endswith('.jpeg'):
#       im = Image.open(i)
#        im.show()
#        imageText = input("what is this photo about?")

        f = open(f"content/{file_name}", 'a')
#        f.write(imageText + '  ' + '<img src="{static}/images/2021/' + folderDate + '/' + i + '"' + ' width="700">' + '\n' + '\n')
        html =f'''<img src="{{static}}/images/2021/{folderDate}/{file}" width="700">

        ---
        '''

        f.write('<img src="{static}/images/2021/' + folderDate + '/' + file + '"' + ' width="700">' + '\n' + '\n')
        f.close()
