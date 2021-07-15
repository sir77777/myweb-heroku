import os
import django
import pandas as pd
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import Country
url = 'https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html'
raw_data = pd.read_html(url)
time.sleep(3)

data = raw_data[1]

country_id = list(data['countries']['id'])
country_name = list(data['countries']['name'])
country_id_name = zip(country_id, country_name)
for id_name in country_id_name:
    temp = Country(name=id_name[1], country_id=id_name[0])
    temp.save()
    print(id_name)

countries = Country.objects.all()
print(countries)
print("Done!")
