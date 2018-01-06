from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html)
		title = bsObj.head.title
	except AttributeError as e:
		return None
	return title
title = getTitle("http://vtop.vit.ac.in")
if title == None:
	print("Title could not be found")
else:
	print(title)
