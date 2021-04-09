
string_url = input("past url here ")

def get_pcode():
    remove = "https://my.pcloud.com/publink/show?code="
    pcode = string_url.strip(remove)
    print(pcode)
get_pcode()     
