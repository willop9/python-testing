import urllib.request
from bs4 import BeautifulSoup

mysite = urllib.request.urlopen('http://www.bbc.co.uk').read()
soup = BeautifulSoup(mysite, 'html5lib')

#description = soup.find("meta", {"name": "description"}) # meta tag description
#print(soup.prettify)
site2 = urllib.request.urlopen("file:./docs/page.html")
soup2 = BeautifulSoup(site2, 'lxml')
#print(soup2.get_text())
#print(soup2.prettify())
head_tag = soup2.head
#for child in head_tag.descendants:
 #   print(child)

print(len(soup2.contents))
print(soup2.contents[len(soup2.contents) -1].name)

print(len(head_tag.contents))

for child in head_tag.contents:
    print(head_tag.contents[child].name)