import urllib.request
from bs4 import BeautifulSoup
response=urllib.request.urlopen('https://www.mjkacc.com/#google_vignette')
html_doc=response.read()
soup=BeautifulSoup(html_doc,'html.parser')
strhtm=soup.prettify()
print(strhtm[:225])
