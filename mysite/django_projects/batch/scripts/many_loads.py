import csv
from os import stat  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, Region, State, Site, Iso


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)
        name = row[0]
        description = row[1]
        justification = row[2]
        
        category, created = Category.objects.get_or_create(name=row[7])
        category.save()

        state, created = State.objects.get_or_create(name=row[8])
        state.save()

        region, created = Region.objects.get_or_create(name=row[9])
        region.save()

        iso, created = Iso.objects.get_or_create(name=row[10])
        iso.save()

        try:
            year = int(row[3])
        except:
            year = None

        try:
            longitude = int(row[4])
        except:
            longitude = None

        try:
            latitude = int(row[5])
        except:
            latitude = None

        try:
            area_hectares = int(row[6])
        except:
            area_hectares = None

        
        site = Site(
            name=name , description=description, justification=justification,
            year=year, longitude=longitude, latitude=latitude, area_hectares=area_hectares,
            category=category, state=state, region=region, iso=iso)
        site.save()