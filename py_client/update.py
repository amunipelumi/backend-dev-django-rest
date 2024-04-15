
import requests

endpoint = 'http://localhost:8000/api/products/3/update/' 

data = {
    'title':'This is number 3',
    'price':19.84
}

response = requests.put(endpoint, json=data) 

print(response.status_code, '\n')
print(response.json(), '\n') 
