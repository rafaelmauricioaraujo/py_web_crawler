# http://py4e-data.dr-chuck.net/known_by_Fikret.html
# http://py4e-data.dr-chuck.net/known_by_Tyson.html
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def search(url, count, position):

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    
    # print('Retrieving: ', tags.get('href', None))
    # print(tags[position-1])
    url = tags[position-1].get('href', None)
    if count == 1:
        print(tags[position-1].contents[0])
    count = count - 1
    if count > 0:
        search(url, count, position)
        
        
        
        # url = tag.get('href', None)
        # print('Contents:',tag.contents[0])
    

url = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
search(url, count, position)


# print('TAG:',tag)
# print('URL:',tag.get('href', None))
# print('Contents:',tag.contents[0])
# print('Attrs:',tag.attrs)
