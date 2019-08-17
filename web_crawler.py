# http://py4e-data.dr-chuck.net/comments_42.html
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
soma = 0

for tag in tags:
    #print('TAG:',tag)
    # print('URL:',tag.get('href', None))
    # print('Contents:',tag.contents[0])
    soma = soma + int(tag.contents[0])
    # print('Attrs:',tag.attrs)
print('soma: ', soma)
