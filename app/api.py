import requests, json

def getProducts(product):
    url= f'https://dummyjson.com/products/{product}'
    response = requests.get(url)
    if response.ok:
        api = response.json()
        product_info = {}
        product_info['title'] = api['title']
        product_info['description'] = api['description']  
        product_info['price'] = api['price'] 
        product_info['rating'] = api['rating']
        product_info['category'] = api['category']
        product_info['thumbnail'] = api['thumbnail']
        product_info['img_01'] = api['images'][0]
        return product_info
    else:
        return None
    
