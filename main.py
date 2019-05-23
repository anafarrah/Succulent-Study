from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import time

from requests import get

BASE_URL: 'https://www.succulentsandsunshine.com/'
LIST_URL: 'https://www.succulentsandsunshine.com/types-of-succulents-plants/'

# plants={'URL':[]}

response = get(url)
print(response.text[:300])
