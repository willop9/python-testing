import urllib
from bs4 import BeautifulSoup

mysite = urllib.request.urlopen('http://www.google.com').read()
soup = BeautifulSoup(mysite)

description = soup.find("meta", {"name": "description"}) # meta tag description
text = description['content'] # text of content attribute

print(text)