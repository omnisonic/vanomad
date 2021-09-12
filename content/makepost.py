from datetime import date
import os


# change this date for each post.  posts built on day / folder of images
post_images_dir = "./images/2021/" + input('what date / folder?')


# get the base from the posts' /images subfolder.  The subfolders will be the named after the date the photos were taken 
base_name = os.path.basename(post_images_dir)

ext_name  = '.md'

# splits the date (image folder name, same name as md file name into 3 variables for the delta)
post_y, post_m, post_d = base_name.rsplit('-')


#  counts the days since i started
d0 = date(2021, 4, 8)
dx = date(int(post_y), int(post_m),int( post_d))
delta = dx - d0

day_Nbr = str(delta.days)


post_title = 'Day ' + day_Nbr + ' - ' + input('what is the description or place?')

file_name = base_name + 'Day' + day_Nbr + ext_name
md_title = 'Title: ' + post_title
md_date = 'Date: ' +  base_name
md_category = 'Category: ' + input('what is the category?')
md_tags = 'Tags: ' + input('what tags?')


#write the file
f = open(file_name, 'w')
f.write(md_title + '\n'  + md_date + '\n' + md_category + '\n' + md_tags + '\n' + '\n')
f.close()

#loop through post images and generate html
for i in os.listdir(post_images_dir):
   if i.endswith('.jpeg'):
        f = open(file_name, 'a')
        f.write('<img src="{static}/images/2021/' + base_name + '/' + i + '"' + ' width="700">' + '\n' + '\n')
        f.close()
