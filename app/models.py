from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True )
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    category = db.Column(db.String(100))
    thumbnail = db.Column(db.String(300))
    img_01 = db.Column(db.String(300))

    def __init__(self, title, price, description, rating, category, thumbnail, img_01):
        self.title = title
        self.description = description
        self.price = price
        self.rating = rating
        self.category = category
        self.thumbnail = thumbnail
        self.img_01 = img_01

    
    def saveProduct(self):
        db.session.add(self)
        db.session.commit()

  
    def to_dict(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'description' : self.description,
            'price' : self.price,
            'rating' : self.rating,
            'category' : self.category,
            'thumbnail' : self.thumbnail,
            'img_01' : self.img_01, 
        }
