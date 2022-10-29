class Vehicle():
    def __init__(self, brand, model, color, plate):
        self.brand = brand
        self.model = model
        self.color = color
        self.plate = plate

    def getBrand(self):
        return self.brand

    def setBrand(self, brand):
        self.brand = brand

    def getModel(self):
        return self.model
    
    def setModel(self, model):
        self.model = model

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getPlate(self):
        return self.plate

    def setPlate(self, plate):
        self.plate = plate

vehicle = Vehicle('brand', 'model', 'color', 'plate')