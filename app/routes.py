from app.models import db, Product
from flask import render_template
from app import app
from app.api import getProducts


# THIS IS ONLY TO ADD YOUR YOUR DB!!!!
# ADD THIS TO YOUR INDEX.HTML:
# <a href="{{ url_for('sendIt') }}" class="btn btn-dark">Add to Cart!</a>

@app.route('/')
def sendIt():
    for i in range(1,50):
        x = getProducts(i)
        p = Product(title=x['title'], description=x['description'], price=x['price'], rating=x['rating'], category=x['category'], thumbnail=x['thumbnail'], img_01=x['img_01'])
        p.saveProduct()
        print("ADDED TO DB")
    return render_template('index.html')





@app.route('/db')
def productDB():
    y = Product.query.all()
    prodlist = [p.to_dict() for p in y]
    return {
        'status': 'ok',
        'data' : prodlist,
        'item_count' : len(prodlist)
    }

@app.route('/db/<int:product_id>')
def indPost(product_id):
    product = Product.query.get(product_id)
    if product:
        p = product.to_dict() # Assuming to_dict() method returns a dictionary with product data
        return ({
            'status': 'ok',
            'data': p,
            'item_count': 1 # Since you are returning a single product
        })
    else:
        return ({
            'status': 'error',
            'message': 'Product not found'
        }), 404 # Return a 404 status code if product not found
    
    