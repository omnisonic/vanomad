from datetime import date
import os
from PIL import Image

folderDate = "2021-09-28" #date of article , same name as folder name
postPlace = "Medicine Bow NF Pole Mountain / Laramie Ranger District" # the place of this articles photos
postCategory = "Wyoming" # pelican article category
postTags = "National Forest -, dispursed camping" #pelican article tag(s) seperated by comma


# change this date for each post.  posts built on day / folder of images
post_images_dir = '/Users/omnisonic/Documents/code/MyWebDev/Python Static Sites/Pelican/vanomad/content/images/2021/2021-09-28' #"images/2021/" + folderDate

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

post_title = 'Day ' + day_Nbr + ' - ' +  postPlace

file_name = folderDate + 'Day' + day_Nbr + ext_name
md_title = 'Title: ' + post_title
md_date = 'Date: ' +  folderDate
md_category = 'Category: ' + postCategory
md_tags = 'Tags: ' + postTags


#write the file
f = open(file_name, 'w')
f.write(md_title + '\n'  + md_date + '\n' + md_category + '\n' + md_tags + '\n' + '\n')
f.close()

#loop through post images and generate md / html
for i in os.listdir(post_images_dir):
   if i.endswith('.JPG'):
#       im = Image.open(i)
#        im.show()
#        imageText = input("what is this photo about?")

        f = open(file_name, 'a')
#        f.write(imageText + '  ' + '<img src="{static}/images/2021/' + folderDate + '/' + i + '"' + ' width="700">' + '\n' + '\n')
        f.write('<img src="{static}/images/2021/' + folderDate + '/' + i + '"' + ' width="700">' + '\n' + '\n')
        f.close()
