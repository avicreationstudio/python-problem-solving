from abc import ABC, abstractmethod

class Chassis(ABC):
    # here 👇 If I inherited `Chassis` class,
    # then for sure you should have a function named `tyreDetails` 
	# and it should have logic implemented
    @abstractmethod 
    def tyreDetails(self):
        pass
		
class Jeep(Chassis):
    def tyreDetails(self):
        self.details = ["MRF",100,23.23]
        return self.details
        
class Swift(Chassis):
	def tyreDetails(self):
		self.details = ["Apollo",30,10.03]
		return self.details

car1 = Swift()
car2 = Jeep()
