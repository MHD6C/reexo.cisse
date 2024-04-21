class Voiture:
    marque = "inconnue"
    def setmarque(self,m) -> None:
        self.marque = m
car = Voiture()
car.setmarque("Mercedes")
print(car.marque)
    