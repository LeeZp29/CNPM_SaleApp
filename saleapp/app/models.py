from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app import db, app


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Float, default=0)
    image = Column(String(100), nullable=True)
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Desktop')
        # c3 = Category(name='Tablet')
        #
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()

        products = [{
            "name": "iPhone 7 Plus",
            "description": "Apple, 32GB, RAM: 3GB, iOS13",
            "price": 17000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
            "category_id": 1
        }, {
            "name": "iPad Pro 2020",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690528735/cg6clgelp8zjwlehqsst.jpg",
            "category_id": 2
        }, {
            "name": "iPad Pro 2021",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690528735/cg6clgelp8zjwlehqsst.jpg",
            "category_id": 2
        }, {
            "name": "iPad Pro 2022",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690528735/cg6clgelp8zjwlehqsst.jpg",
            "category_id": 2
        }, {
            "name": "iPad Pro 2023",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690528735/cg6clgelp8zjwlehqsst.jpg",
            "category_id": 2
        }, {
            "name": "iPad Pro 2024",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690528735/cg6clgelp8zjwlehqsst.jpg",
            "category_id": 2
        }, {
            "name": "iPad Pro 2021",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690528735/cg6clgelp8zjwlehqsst.jpg",
            "category_id": 2
        }, {
            "name": "iPad Pro 2022",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690528735/cg6clgelp8zjwlehqsst.jpg",
            "category_id": 2
        }]

        for p in products:
            prod = Product(**p)
            db.session.add(prod)

        db.session.commit()