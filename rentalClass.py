from abc import ABC, abstractmethod

# Abstract base class for rental properties
class RentalProperty(ABC):

    """
    This abstract class represents a generic rental property.
    It serves as a template for whole and room rental properties(Parent Class).
    Author: Shimar Yasin Khan
    Date: 17/5/2024
    Version: 1.0
    """

    # Constructor - Initialize common attributes for all rental properties
    def __init__(self, rental_ID, address, weeklyPrice, furnished, description):
        self.rental_ID: str = rental_ID
        self.address: str = address
        self.weeklyPrice: float = weeklyPrice
        self.furnished: bool = furnished
        self.description: str = description

    # Setter Functions
    def set_RentalID(self, newRentalID):
        # Set the rental ID
        self.rental_ID = newRentalID

    def set_Address(self, newAddress):
        # Set the address
        self.address = newAddress

    def set_WeeklyPrice(self, newPrice):
        # Set the weekly price
        self.weeklyPrice = newPrice

    def set_Furnished(self, newFurnished):
        # Set whether the property is furnished
        self.furnished = newFurnished

    def set_Description(self, newDescription):
        # Set the description
        self.description = newDescription

    # Getter Functions
    def get_Rental_ID(self):
        # Get the rental ID
        return self.rental_ID

    def get_address(self):
        # Get the address
        return self.address

    def get_weekly_price(self):
        # Get the weekly price
        return self.weeklyPrice

    def get_furnished(self):
        # Get whether the property is furnished
        return self.furnished

    def get_description(self):
        # Get the description
        return self.description

    # Abstract method to display rental details
    @abstractmethod
    def displayRental(self):
        pass 

# Class for whole rental properties
class WholeRental(RentalProperty):

    """
    This class represents a whole rental property.
    It extends the RentalProperty class(Child Class) and adds specific attributes for whole rentals.
    Author: Shimar Yasin Khan
    Date: 17/5/2024
    Version: 1.0
    """

    # Constructor - Initialize specific attributes for whole rental properties
    def __init__(self, rental_ID, address, weeklyPrice, furnished, description, noofRooms, garageSpace, petsAllowed):
        super().__init__(rental_ID, address, weeklyPrice, furnished, description)
        self.noofRooms: int = noofRooms
        self.garageSpace: int = garageSpace
        self.petsAllowed: bool = petsAllowed

    # Getters
    def get_noofrooms(self):
        # Get the number of rooms
        return self.noofRooms

    def get_garage_space(self):
        # Get the garage space
        return self.garageSpace

    def pets_allowed(self):
        # Get whether pets are allowed
        return self.petsAllowed

    # Setters
    def set_NoOfRooms(self, newNoOfRooms):
        # Set the number of rooms
        self.noofRooms = newNoOfRooms

    def set_garageSpace(self, newGaragespace):
        # Set the garage space
        self.garageSpace = newGaragespace

    def set_Petsallowed(self, newPetsallowed):
        # Set whether pets are allowed
        self.petsAllowed = newPetsallowed

    # Display details of the whole rental property
    def displayRental(self):
        return (f"Rental ID : {self.rental_ID} \nAddress :{self.address} \nWeeklyPrice : {self.weeklyPrice} "
                f"\nFurnished : {self.furnished} \nDescription : {self.description} \nNumber of Rooms : {self.noofRooms} "
                f"\nGarage Space : {self.garageSpace} \nPets Allowed : {self.petsAllowed} \n ")

    # Destructor
    def __del__(self):
        print(f"Whole Rental : {self.rental_ID} Deleted \n")

# Class for room rental properties
class RoomRental(RentalProperty):

    """
    This class represents a room rental property.
    It extends the RentalProperty class(Child class) and adds specific attributes for room rentals.
    Author: Shimar Yasin Khan
    Date: 17/5/2024
    Version: 1.0
    """

    
    #Constructor - Initialize specific attributes for room rental properties
    def __init__(self, rental_ID, address, weeklyPrice, furnished, description, couplesAllowed, attachedBathroom):
        super().__init__(rental_ID, address, weeklyPrice, furnished, description)
        self.couplesAllowed: bool = couplesAllowed
        self.attachedBathroom: bool = attachedBathroom

    # Getters
    def get_couples_allowed(self):
        # Get whether couples are allowed
        return self.couplesAllowed

    def get_attached_bathroom(self):
        # Get whether there is an attached bathroom
        return self.attachedBathroom

    # Setters
    def set_Couplesallowed(self, newCouplesAllowed):
        # Set whether couples are allowed
        self.couplesAllowed = newCouplesAllowed

    def set_Attachbathroom(self, newAttachBathrooms):
        # Set whether there is an attached bathroom
        self.attachedBathroom = newAttachBathrooms

    # Display details of the room rental property
    def displayRental(self):
        return (f"Rental ID : {self.rental_ID} \nAddress :{self.address} \nWeeklyPrice : {self.weeklyPrice} "
                f"\nFurnished : {self.furnished} \nDescription : {self.description} \nCouples Allowed : {self.couplesAllowed} "
                f"\nAttached Bathroom : {self.attachedBathroom} \n ")

    # Destructor
    def __del__(self):
        print(f"Room Rental : {self.rental_ID} Deleted \n")