import os
import django
import pandas as pd
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import Country, City
url = 'https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html'
raw_data = pd.read_html(url)
time.sleep(3)

data = raw_data[0]
cities = list()
for i in range(len(data)):
    temp = tuple(data['cities'].iloc[i])
    cities.append(temp)
print(cities)

for city in cities:
    try:
        countryname = Country.objects.get(country_id=city[2])
        temp = City(name=city[1], country=countryname, population=city[3])
        temp.save()
    except:
        pass
    
cityinfo = City.objects.all()
print(cityinfo)
print("Done!")
