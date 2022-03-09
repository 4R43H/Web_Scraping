import requests
from bs4 import BeautifulSoup
import arabic_reshaper
from bidi.algorithm import get_display

r = requests.get('https://divar.ir/s/tehran')

soup = BeautifulSoup(r.text, 'html.parser')
agahi_ha = soup.find_all(class_="kt-post-card__description")
onvan_ha = soup.find_all(class_="kt-post-card__title")

total = []
for agahi in agahi_ha:
    total.append(agahi.text)

reshaped_total = []
for i in range(0, len(total)):
    x1 = arabic_reshaper.reshape(total[i])
    x2 = get_display(x1)
    reshaped_total.append(x2)

total1 = []
for onvan in onvan_ha:
    total1.append(onvan.text)

reshaped_total2 = []
for j in range(0, len(total1)):
    x3 = arabic_reshaper.reshape(total1[j])
    x4 = get_display(x3)
    reshaped_total2.append(x4)

list_nahaie = []
for k in range (0, len(reshaped_total)):
    list_nahaie.append((reshaped_total2[k], reshaped_total[k]))

x = dict(list_nahaie)

for item in x:
    if x[item] == 'ﯽﻘﻓﺍﻮﺗ':
        print (item)