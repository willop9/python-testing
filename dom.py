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
body_tag = soup2.body
#for child in head_tag.descendants:
 #   print(child)

#print(len(soup2.contents))
#print(soup2.contents[len(soup2.contents)-1].name)

#print(len(head_tag.contents))

#for child in head_tag.children:
    #print(child.name)

#print(head_tag.contents)
#print('############################')
#print('iterating over direct children')
#print('number of cihldren in soup object',len(soup2.contents))
#for child in soup2.children:
    #print(child)

print('##########################')
print('Iterating over all descendants recursively')

#for child in body_tag.descendants:
    #print(child)

for child in soup.descendants:
    if(child.name is not None):
        print(child.name)
#scripts = []
#for script in soup2.find_all("script"):
 #   print(script.name)
  #  scripts.append(script)
#print("#######################################")
#for x in scripts:
 #       print(x.name)