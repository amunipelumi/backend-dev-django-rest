
import requests


def pid_func():
    product_id = input('What is your product id:\n')

    try:
        product_id = int(product_id)
    except:
        print('Your product id is not valid!\n')
        pid_func()

    return product_id


product_id = pid_func()

if product_id:
    endpoint =f'http://localhost:8000/api/products/{product_id}/delete/' 
    response = requests.delete(endpoint) 

    print(response.status_code, '\n')

    if response.status_code == 204:
        print('item deleted successfully!')
        
    elif response.status_code == 404:
        print('item does not exist in database!')
    
