# import csv

# Reading CSV

# with open(
#         'data/addresses.csv'
# ) as csvfile:
#     reader = csv.reader(csvfile, skipinitialspace=True)
#     for row in reader:
#         # row is a `list`
#         print(row[1])

# Reading CSV with headers

# with open(
#         'data/biostats.csv'
# ) as csvfile:
#     reader = csv.DictReader(csvfile, skipinitialspace=True)
#     for row in reader:
#         # row is a collections.OrderedDict
#         print(row)
#         print(row['Name'], row['Sex'], int(row['Age']))

# Writing CSV
# beatles = [{
#     'first_name': 'John',
#     'last_name': 'lennon',
#     'instrument': 'guitar'
# }, {
#     'first_name': 'Ringo',
#     'last_name': 'Starr',
#     'instrument': 'drums'
# }]

# with open('data/beatles.csv', 'w') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=beatles[0].keys())
#     writer.writeheader()
#     for beatle in beatles:
#         writer.writerow(beatle)

from urllib import response
import requests

# # url = 'https://api.github.com/users/solerog'
# url = 'https://openlibrary.org/api/books?bibkeys=ISBN:0201558025,LCCN:93005405&format=json&jscmd=data'
# response = requests.get(url).json()

# print(response)

# isbn = '0-7475-3269-9'
# key = f'ISBN:{isbn}'

# response = requests.get(
#     'https://openlibrary.org/api/books',
#     params={
#         'bibkeys': key,
#         'format': 'json',
#         'jscmd': 'data'
#     },
# ).json()

# print(response[key]['title'])

import requests
from bs4 import BeautifulSoup

# url = 'https://api.github.com/users/solerog'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")

# # You now can query the `soup` object!
# soup.title.string
# soup.find('h1')
# soup.find_all('a')

url = 'https://www.imdb.com/list/ls055386972/'
response = requests.get(url, headers={'Accept-Language': 'en-GB'})
soup = BeautifulSoup(response.content, "html.parser")
movie_html = soup.find_all(class_="lister-item-content")
movies = []

for movie in movie_html:
    title = movie.h3.a.string
    duration = movie.p.find(class_="runtime").string.strip(" min")
    movies.append({'title': title, 'duration': duration})

print(*movies[0:10], sep='\n')
