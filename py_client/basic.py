import requests

endpoint0 = 'http://localhost:8000/api'  # 'http://127.0.0.1:8000/'
endpoint1 = 'https://httpbin.org/anything'

response = requests.post(endpoint0, json={
    'title':'Kiki',
    'content':'Hello World!', 
    # 'price':123, 
    # 'sale_price':100
}) # 

print(response.status_code, '\n')
print(response.json(), '\n') 
