class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.BrandName = brand_name
        self.ModelName = model_name
        self.Price = price
        self.laptop_name=brand_name + " " + model_name
    def apply_discount(self,num):
        off_price= (num/100)*self.Price
        return self.Price-off_price

laptop1=Laptop("hp","au114tx",63000)
print(laptop1.apply_discount(40))