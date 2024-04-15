
import requests
from getpass import getpass

auth_endpoint = 'http://localhost:8000/api/auth/' 
username = input('What is your username:\n')
password = getpass()

auth_response = requests.post(auth_endpoint, json={'username':username, 'password':password}) 
token = auth_response.json()['token']
print('\n', token, '\n')

if auth_response.status_code == 200:

    endpoint = 'http://localhost:8000/api/products/' 
    headers = {'Authorization':f'Bearer {token}'}
    response = requests.get(endpoint, headers=headers) 

    # print('\n', response.json(), '\n') 
    for item in response.json()['results']:
        print(item, '\n') 

    next_url = response.json()['next']
    while next_url:
        response = requests.get(next_url, headers=headers) 
        for item in response.json()['results']:
            print(item, '\n')
        next_url = response.json()['next']