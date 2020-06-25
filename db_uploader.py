import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trost.settings")
django.setup()
#from partner.models import Counselor, Level, Theme, CounselKind, Duration, Product

CSV_PATH_COUNSELORS = './trost_crawling_1.csv'

#with open(CSV_PATH_COUNSELORS) as in_file:
#    data_reader = csv.reader(in_file)
#    next(data_reader, None)
#    level = []
   # for row in data_reader:
  #      name = row[0]
 #       gender =row[2]
#        counsel_count = row[4]
#        introduction = row[5]

#        print(name, gender, counsel_count, introduction)

        ###level into DB###
#        levels = row[1]
#        if levels not in level:
#            level.append(levels)
#    for i in level:
#        Level.objects.create(level=i)


