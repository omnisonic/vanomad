#import os

#path = os.getcwd() 


file_name = input("what shall we call this file?")

# this prompts for the meta info for the file

md_title = 'Title: ' + input('what is the title of this post?')
md_date = 'Date: ' + input('what is the date for this post? eg year-mo-dd')
md_category = 'Category: ' + input('what is the category?')
# these variables reconstruct image link url
head_url = '![image](https://api.pcloud.com/getpubthumb?code='
tail_url = '&linkpassword=undefined&size=600x600&crop=0&type=autok)'

# this opens the file and add the meta info.

f = open(file_name, 'w')
f.write(md_title + '\n'  + md_date + '\n' + md_category + '\n' + '\n')

f.close()



#this section gives prompt for pcloud link and then formats and appends the properly formatted link to the md file. 
#this uses a while loop to continously ask for links unless user enter 'done'.

while True:
    
    string_url = input("Paste url here:\n")
    if string_url == "done":
        break
    # this variable is for the text content to accompany each photo:
    p_text = input("Type in text to accompany this photo:\n")

    remove = "https://my.pcloud.com/publink/show?code="
    pcode = string_url.strip(remove)
    f = open(file_name, 'a')
    f.write(p_text + head_url + pcode + tail_url + '\n' + '\n')
    f.close()
#print(pcode)
exit()
