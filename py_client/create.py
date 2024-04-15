
import requests

endpoint = 'http://localhost:8000/api/products/' 

response = requests.post(endpoint, data={'title':'I am Awesome!'})  

print(response.status_code, '\n')
print(response.json(), '\n') 
