# installed requests using the following pip
# pip install requests

# The added to the project
# Go into File → Settings → Project Settings → Project Interpreter.

import requests

baseURL = 'https://swapi.co/api/'

exampleURL = 'planets/6/'

fullURLRequest = baseURL + exampleURL
print(fullURLRequest)

# This is the get request that captures the return from the API
json_data = requests.get(fullURLRequest).json()
print(json_data)

# This uses the response as a dictionary to access a particular Key
print('Planet Name = ' + json_data['name'])
print('Terrain = ' + json_data['terrain'])
