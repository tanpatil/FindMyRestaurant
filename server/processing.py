"""
Pre-processing on data files. Condense reviews to only include restaurants.
"""

import pandas as pd
import gzip
import json
import ast

top = 49.3457868 # north lat
left = -124.7844079 # west long
right = -66.9513812 # east long
bottom =  24.7433195 # south lat

big_business = [
  'McDonald',
  'Burger King',
  'Five Guys',
  'Chipotle',
  'Jack In The Box',
  'Panera',
  'Domino',
  'Pizza Hut',
  'Olive Garden',
  'Sonic',
  'Wendy',
  'Taco Bell',
  'Shake Shack',
  'Arby',
  'Cheesecake Factory',
  'Whataburger',
  'Chili\'s',
  'IHOP',
  'Subway',
  'Little Caesar\'s',
  'Chick Fil A',
  'Smashburger',
  'Wingstop',
  'Starbucks',
  'Dunkin'
]

def isRestaurant(categories):
  for category in categories:
    if('Restaurant' in category):
      return True
  return False

def isInHouston(location):
  for line in location:
    if('Houston' in line):
      return True
  return False

def notYuge(name):
  for loc in big_business:
    if loc in name:
      return False
  return True

def processPlaces(n):
  count = 0
  g = gzip.open('data/places.clean.json.gz', 'r')
  places = []

  for l in g:
    place = ast.literal_eval(str(eval(l)))
    if(place['address'] != None and place['name'] != None):
      if isInHouston(place['address']):
        places.append(place['gPlusPlaceId'])
        obj = pd.json_normalize(place)
        if count == 0:
          obj.to_csv('data/places.csv', mode='a', index=False)
        else:
          obj.to_csv('data/places.csv', mode='a', header=False, index=False)
        count += 1
        if(count % 1000 == 0):
          print(count)
    if(count >= n):
      break
  print('Places Done')
  print(places)
  return places

def processUsers(n):
  g = gzip.open('data/users.clean.json.gz', 'r')
  count = 0

  for l in g:
    user = ast.literal_eval(str(eval(l)))
    obj = pd.json_normalize(user)
    obj.to_csv('data/users.csv', mode='a')

    count += 1
    if(count % 1000 == 0):
      print(count)

  print('Users Done')

def processReviews(n):
  count = 0
  g = gzip.open('data/reviews.clean.json.gz', 'r')
  places = processPlaces(6000)
  reviews = []

  for l in g:
    review = ast.literal_eval(str(eval(l)))
    if(review['gPlusPlaceId'] != None and review['categories'] != None and str(review['reviewText']) != 'None'):
      if((review['gPlusPlaceId'] in places) and isRestaurant(review['categories'])):
        obj = pd.json_normalize(review)
        if count == 0:
          obj.to_csv('data/out.csv', mode='a', index=False)
        else:
          obj.to_csv('data/out.csv', mode='a', header=False, index=False)
        count += 1
        if(count % 10 == 0):
          print(count)
    if(count >= n):
      break
  print(reviews)

processReviews(2000)