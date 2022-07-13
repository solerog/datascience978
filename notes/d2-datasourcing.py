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

import requests

# # url = 'https://api.github.com/users/solerog'
# url = 'https://openlibrary.org/api/books?bibkeys=ISBN:0201558025,LCCN:93005405&format=json&jscmd=data'
# response = requests.get(url).json()

# print(response)

isbn = '0-7475-3269-9'
key = f'ISBN:{isbn}'

response = requests.get(
    'https://openlibrary.org/api/books',
    params={
        'bibkeys': key,
        'format': 'json',
        'jscmd': 'data'
    },
).json()

print(response[key]['title'])
