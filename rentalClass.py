# Setter, Getter, Constructor Deconstructor

class RentalProperty:
    def __init__(self, rental_ID, address, weeklyPrice, furnished, description):
        self.rental_ID: str = rental_ID
        self.address: str = address
        self.weeklyPrice: float = weeklyPrice
        self.furnished: bool = furnished
        self.description: str = description

    # Setter Functions - Assume that RentalID cannot be changed after being set

    def set_Address(self, newAddress):
        self.address = newAddress

    def set_WeeklyPrice(self, newPrice):
        self.weeklyPrice = newPrice

    def set_Furnished(self, newFurnished):
        self.furnished = newFurnished

    def set_Description(self, newDescription):
        self.description = newDescription

    # Getter Functions
    def get_Rental_ID(self):
        return self.rental_ID

    def get_address(self):
        return self.address

    def get_weekly_price(self):
        return self.weeklyPrice

    def get_furnished(self):
        return self.furnished

    def get_description(self):
        return self.description

    # Display Rentals
    def displayRoom(self):
        return None


class WholeRental(RentalProperty):
    def __init__(self, rental_ID, address, weeklyPrice, furnished, description, noofRooms, garageSpace, petsAllowed):
        super().__init__(rental_ID, address, weeklyPrice, furnished, description)
        self.noofRooms: int = noofRooms
        self.garageSpace: int = garageSpace
        self.petsAllowed: bool = petsAllowed

    # Setters

    def set_NoOfRooms(self, newNoOfRooms):
        self.noofRooms = newNoOfRooms

    def set_Garagespace(self, newGarageSpace):
        self.garageSpace = newGarageSpace

    def set_Petsallowed(self, newPetsallowed):
        self.petsAllowed = newPetsallowed

    # Getters
    # Displays Rentals
    def displayRental(self):
        return f"Rental ID : {self.rental_ID} \nAddress :{self.address} \nWeeklyPrice : {self.weeklyPrice} \nFurnished : {self.furnished} \nDescription : {self.description} \nNumber of Rooms : {self.noofRooms} \nGarage Space : {self.garageSpace} \nPets Allowed : {self.petsAllowed} \n"

    # Destructor
    def __del__(self):
        print(f"Whole Rental : {self.rental_ID} Deleted \n")

    # Getters
    def get_noofrooms(self):
        return self.noofRooms

    def get_garage_space(self):
        return self.garageSpace

    def pets_allowed(self):
        return self.petsAllowed

class RoomRental(RentalProperty):
    def __init__(self, rental_ID, address, weeklyPrice, furnished, description, couplesAllowed, attachedBathroom):
        super().__init__(rental_ID, address, weeklyPrice, furnished, description)
        self.couplesAllowed: bool = couplesAllowed
        self.attachedBathroom: bool = attachedBathroom

    # Setters
    def set_Couplesallowed(self, newCouplesAllowed):
        self.couplesAllowed = newCouplesAllowed

    def set_Attachbathroom(self, newAttachBathrooms):
        self.attachedBathroom = newAttachBathrooms

    def displayRental(self):
        return f"Rental ID : {self.rental_ID} \nAddress :{self.address} \nWeeklyPrice : {self.weeklyPrice} \nFurnished : {self.furnished} \nDescription : {self.description} \nCouples Allowed : {self.couplesAllowed} \nAttached Bathroom : {self.attachedBathroom}"

    # Destructor
    def __del__(self):
        print(f"Room Rental : {self.rental_ID} Deleted \n")

    # Getters
    def get_couples_allowed(self):
        return self.couplesAllowed

    def get_attached_bathroom(self):
        return self.attachedBathroom