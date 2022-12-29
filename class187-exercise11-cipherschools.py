class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.BrandName = brand_name
        self.ModelName = model_name
        self.Price = price
obj1=Laptop("MSI","au114tx",63000)
obj2=Laptop("hp","pavilion",63000)
print(obj1.BrandName)
print(obj2.ModelName)