# Setter, Getter, Constructor Deconstructor

class RentalProperty: 
   def __init__(self,rental_ID,address,weeklyPrice,furnished,description):
      self.rental_ID : str = rental_ID 
      self.address :str  = address 
      self.weeklyPrice : float = weeklyPrice
      self.furnished : bool  = furnished
      self.description :str = description
   
   #Setter Functions 

   def setAddress(self, newAddress):
      self.address = newAddress

   def setWeeklyPrice(self, newPrice):
      self.weeklyPrice = newPrice

   def setFurnished(self, newFurnished):
      self.furnished = newFurnished

   def setDescription(self, newDescription):
      self.description = newDescription

   #Getter Functions
   def getRental_ID(self):
      return self.rental_ID

   def displayRoom(self):
      return None
   
class WholeRental(RentalProperty): 
   def __init__(self,rental_ID,address,weeklyPrice,furnished,description,noofRooms,garageSpace,petsAllowed):
      super().__init__(rental_ID,address,weeklyPrice,furnished,description)
      self.noofRooms : int = noofRooms
      self.garageSpace : int = garageSpace
      self.petsAllowed : bool = petsAllowed

   def displayRental(self):
      return f"Rental ID : {self.rental_ID} \nAddress :{self.address} \nWeeklyPrice : {self.weeklyPrice} \nFurnished : {self.furnished} \nDescription : {self.description} \nNumber of Rooms : {self.noofRooms} \nGarage Space : {self.garageSpace} \nPets Allowed : {self.petsAllowed} \n"

   def __del__(self):
       print(f"Whole Rental : {self.rental_ID} Deleted \n")

class RoomRental(RentalProperty): 
   def __init__(self,rental_ID,address,weeklyPrice,furnished,description,couplesAllowed,attachedBathroom):
      super().__init__(rental_ID,address,weeklyPrice,furnished,description)
      self.couplesAllowed : bool  = couplesAllowed
      self.attachedBathroom : bool = attachedBathroom

   def displayRental(self):
      return f"Rental ID : {self.rental_ID} \nAddress :{self.address} \nWeeklyPrice : {self.weeklyPrice} \nFurnished : {self.furnished} \nDescription : {self.description} \nCouples Allowed : {self.couplesAllowed} \nAttached Bathroom : {self.attachedBathroom} \n"

   def __del__(self):
       print(f"Room Rental : {self.rental_ID} Deleted \n")