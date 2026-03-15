""" Design & create an online store for Products (name, price).
Track total products being created.
Create a static method to calculate discount on each product based on a % parameter. """

class Products:
    count = 0
    
    def __init__(self,name,price):
        self.name = name
        self.price = price
        Products.count = Products.count + 1

    @staticmethod
    def calculate_discount(price, discount):
        print(f"Discounted Price = {price - (price * discount/100)}")

p1 = Products("Phone",6999)
print(f"The Name of the Product is {p1.name} and the Price is {p1.price}")
p1.calculate_discount(p1.price,10)
#------------------------------------------------------------------------------#
p2 = Products("TV",3599)
print(f"The Name of the Product is {p2.name} and the Price is {p2.price}")
p2.calculate_discount(p2.price,12)
#------------------------------------------------------------------------------#
p3 = Products("Oven",5499)
print(f"The Name of the Product is {p3.name} and the Price is {p3.price}")
p3.calculate_discount(p3.price,14)
#------------------------------------------------------------------------------#
print(f"The Total Number of Products : {Products.count}")

