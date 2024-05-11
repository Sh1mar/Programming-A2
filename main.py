from rentalClass import *

"""
TODO:

Option to go back  
"""

rentalProperty_Objects = []

"""
Purpose: 
    - Takes the rental type as an argument
    - Takes user input of the attributes of the rental property
    - Creates WholeRental or RoomRental object (based on rentalType argument)
    - Appends object to a list storing all rental property objects

Args:
    rentalType : int

Returns:
    None
"""
# MARK: Enter Retnals 
def enterRentals(rentalType: int) -> None:  
    rental_ID = input("Enter rental ID: ")

    address = str(input("Enter address: "))
    weeklyPrice = float(input("Enter weekly price: "))
    furnished = input("Is the property furnished? (True/False): ").lower() == 'true'
    description = input("Enter property description: ").capitalize()

    if rentalType == 1:
        noofRooms = int(input("Enter number of rooms: "))
        garageSpace = int(input("Enter garage space (if any): "))
        petsAllowed = input("Are pets allowed? (True/False): ").lower() == 'true'

        rentalProperty_Objects.append(["WholeRental", WholeRental(rental_ID, address, weeklyPrice, furnished, description, noofRooms,
                                                   garageSpace, petsAllowed)])

    else:
        couplesAllowed = input("Are couples Allowed? (True/False): ").lower() == "true"
        attachedBathroom = input("Is there a Attached Bathroom? (True/False): ").lower() == "true"

        rentalProperty_Objects.append(["RoomRental", RoomRental(rental_ID, address, weeklyPrice, furnished, description,
                                                                couplesAllowed, attachedBathroom)])

"""
Purpose: 
    -

Args:
    rentalType : int - xyz

Returns:
    str :  returns a string of rentalType class properties
"""
# MARK: Retrieve Rentals 
def retreiveRentals(rentalType: int) -> str:
    rentalInfo = ""
    for rentals in rentalProperty_Objects:
        if rentalType == 1 and rentals[0] == "WholeRental":
            rentalInfo += rentals[1].displayRental() + "\n"

        if rentalType == 2 and rentals[0] == "RoomRental":
            rentalInfo += rentals[1].displayRental() + "\n"

        if rentalType == 3:
            rentalInfo += rentals[1].displayRental() + "\n"

    return rentalInfo

# MARK: Update Rentals
"""
Purpose: 
    -Edits/Updates Rental Properties Objects Accordindly and validates the Feild
Args:
    rentalType : str  - 
    rentalSearch_ID : int - 
    feildChange : int -  

Returns:
    None
"""
def updateRentals(rentalType: str, Rentalsearch_ID: int, feildChange: int) -> None:
    for index, rentals in enumerate(rentalProperty_Objects):
        if rentals[1].get_Rental_ID() == Rentalsearch_ID and rentals[0] == rentalType:
            if feildChange == 1:
                new_Address = str(input("Enter New Address: "))
                rentals[1].set_Address(new_Address)

            elif feildChange == 2:
                new_WeeklyPrice = float(input("Enter weekly price: "))
                rentals[1].set_WeeklyPrice(new_WeeklyPrice)

            elif feildChange == 3:
                new_Furnished = input("Is the property furnished? (True/False): ").lower() == 'true'
                rentals[1].set_Furnished(new_Furnished)

            elif feildChange == 4:
                new_Description = input("Enter property description: ").capitalize()
                rentals[1].set_Description(new_Description)

            elif feildChange == 5 and rentalType == "WholeRental":
                new_NoofRooms = int(input("Enter number of rooms: "))
                rentals[1].set_NoOfRooms(new_NoofRooms)

            elif feildChange == 6 and rentalType == "WholeRental":
                new_GarageSpace = int(input("Enter garage space (if any): "))
                rentals[1].set_garageSpace(new_GarageSpace)

            elif feildChange == 5 and rentalType == "RoomRental":
                new_CouplesAllowed = input("Are couples Allowed? (True/False): ").lower() == "true"
                rentals[1].set_Couplesallowed(new_CouplesAllowed)

            elif feildChange == 6 and rentalType == "RoomRental":
                new_AttachedBathroom = input("Is there a Attached Bathroom? (True/False): ").lower() == "true"
                rentals[1].set_Attachbathroom(new_AttachedBathroom)

            elif feildChange == 7:
                new_PetsAllowed = input("Are pets allowed? (True/False): ").lower() == 'true'
                rentals[1].set_Petsallowed(new_PetsAllowed)

            else:
                print("Uncaught Exception!")


# MARK: Delete Rentals
"""
Purpose: 
    -
Args:
    rentalID: int - 
    rentalType: str -  

Returns:
    None 
"""
def deleteRentals(rentalID: int, rentalType: str) -> None:
    for index in range(len(rentalProperty_Objects)):
        if rentalProperty_Objects[index][0] == rentalType and rentalProperty_Objects[index][
            1].get_Rental_ID() == rentalID:
            rentalProperty_Objects.pop(index)

# MARK: Load Back Up
"""
Purpose: 
    -Load existing data from text file, makes rental property objects and appends then to the list

Args: 
    None

Returns:
    None 
"""
def loadRentals():
    file = open("Programming-A2/rentalProperties.txt", "r")

    lines = file.readlines()

    for line in lines:
        line = line.replace("\n", "")

        rental_data = line.split(",")
        rental_ID = rental_data[0]

        # print(rental_data,len(rental_data))

        # Adds the property from the text file to the objects list by creating an oject ONLY if it doesnt already exist
        if not(validateRental(rental_ID)):

            # Whole rental
            if len(rental_data) == 8:
                rental_ID, address, weeklyPrice, furnished, description, noofRooms, garageSpace, petsAllowed = rental_data
                rentalProperty_Objects.append(["WholeRental", WholeRental(rental_ID, address, weeklyPrice, furnished, description, noofRooms, garageSpace, petsAllowed)])
            # Room rental
            else:
                rental_ID, address, weeklyPrice, furnished, description, couplesAllowed, attachedBathroom = rental_data
                rentalProperty_Objects.append(["RoomRental", RoomRental(rental_ID, address, weeklyPrice, furnished, description, couplesAllowed, attachedBathroom)])
    file.close()

# MARK: Back Up
"""
Purpose: 
    -Load existing data from text file, makes rental property objects and appends then to the list

Args: 
    None

Returns:
    None 
"""
def backupRentals():
    file = open("Programming-A2/rentalProperties.txt", "w")
    new_property_text = ""

    for property in rentalProperty_Objects:
        property_type, property_object = property

        new_property_text += f"{property_object.get_Rental_ID()},{property_object.get_address()},{property_object.get_weekly_price()},{property_object.get_furnished()},{property_object.get_description()},"

        if property_type == "RoomRental":
            new_property_text += f"{property_object.get_couples_allowed()},{property_object.get_attached_bathroom()}\n"
        else:
            new_property_text += f"{property_object.get_noofrooms()},{property_object.get_garage_space()},{property_object.pets_allowed()}\n"

    file.write(new_property_text)
    file.close()

# MARK: Utility Functions 
"""
Purpose: 
    -
Args:
    search_ID : str 

Returns:
    bool:   xyz
"""
def validateRental(search_ID: str) -> int:
    for index in range(len(rentalProperty_Objects)):
        if search_ID == rentalProperty_Objects[index][1].get_Rental_ID():
            return True

    return False

"""
Purpose: 
    -Validates user Rental_ID when editing and updating properties

Args:
    rentalType : accepts a integer value 

Returns:
    str :   returns a string of rentalType class properties

"""
# Checks the Type of Rental Property input by the user
def checkRental_Type(search_ID: str) -> str:
    for [rental_type, property_object] in rentalProperty_Objects:
        rental_ID = property_object.get_Rental_ID()
        if rental_ID == search_ID:
            return rental_type

"""
Purpose: 
    -
Args: 
    None

Returns:
    int : Returns the index of the second occurence of the duplicated Rental ID 
"""
def checkDuplicateRentals() -> bool:
    
    for index_i in range(len(rentalProperty_Objects)):
        for index_j in range(len(rentalProperty_Objects)):
            if rentalProperty_Objects[index_i][1].get_Rental_ID() == rentalProperty_Objects[index_j][1].get_Rental_ID() and index_i != index_j:
                return index_j

#Test Cases Delete during Submission
def Testcases():
    # Test Cases

    # Create an instance of WholeRental
    whole_rental = WholeRental(
        rental_ID="WR001",
        address="123 Main St",
        weeklyPrice=500.0,
        furnished=True,
        description="A spacious whole rental",
        noofRooms=3,
        garageSpace=2,
        petsAllowed=True
    )

    # Create an instance of RoomRental
    room_rental = RoomRental(
        rental_ID="RR001",
        address="456 Elm St",
        weeklyPrice=300.0,
        furnished=False,
        description="A cozy room rental",
        couplesAllowed=True,
        attachedBathroom=True
    )

    rentalProperty_Objects.append(["WholeRental", whole_rental])
    rentalProperty_Objects.append(["RoomRental", room_rental])


# MARK: Main
"""
Purpose: 
    -
Args: 
    None

Returns:
    None 
"""
def main():
    #Testcases()
 
    loadRentals()
    print(" \nLoading Rentals from your last sessions Press [5] to display existing Rental Properties \n")
    print(rentalProperty_Objects)


    while True:
    
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
        print("             Student Accommodation Monash (SAM)              ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(
            "[1] Enter Rental Property Details \n[2] Retrieve details of Rental Properties \n[3] Edit and Update details of Rental Properties \n[4] Delete Rental Properties  \n[5] Display Avalaible Rental Properties\n[6] Output Avalaible Rental Properties to a File \n[7] Exit! ")

        while True:
            try:
                userChoice = int(input("Select option : "))
                if userChoice in [1, 2, 3, 4, 5, 6, 7]:
                    break
                else:
                    print("Invalid Input Please Try Again!")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")


        match userChoice:
            # Enter Rental Property Details
            case 1:

                while True:
                    rentalType = int(input(
                        "Enter the Type of Rental Property: \n[1]Whole Rental Property \n[2]Room Rental Property\n"))
                    if rentalType == 1 or rentalType == 2 or rentalType == 3:
                        
                        enterRentals(rentalType)
                        
                        duplicateID_index = checkDuplicateRentals()

                        if duplicateID_index != None: 
                            print("\nWarning! : Duplicate ID detected in Rental Properties!")
                            user_NewID = input("Enter new ID for Rental Property: ")
                            rentalProperty_Objects[duplicateID_index][1].set_RentalID(user_NewID)
                        
                        break
                    else:
                        print("Invalid Input Please Try Again!")

            # Retrieve details of Rental Properties
            case 2:

                if len(rentalProperty_Objects) == 0:
                    print("No Rental Propertires Created! \nPlease Enter Rental Property Details")
                else:
                    while True:
                        print("[1]Whole Rental Property \n[2]Room Rental Property\n[3]All Rental Properties \n")
                        rentalType = int(input("Enter the Type of Rentals do be Retreived:"))
                        if rentalType == 1 or rentalType == 2 or rentalType == 3:
                            print(retreiveRentals(rentalType))
                            break
                        else:
                            print("Invalid Input Please Try Again!")

            # Edit and Update details of Rental Properties
            case 3:

                # Checks wheater Rental Objects exist
                if len(rentalProperty_Objects) == 0:
                    print("No Rental Propertires Created! \nPlease Enter Rental Property Details")

                else:
                    # Displays a summary of the Rental Properties in the rentalProperties lsit
                    print("These are the Existing Rental Properties and their IDs: \n")

                    for rentals in rentalProperty_Objects:
                        print(f"Rental Type: {rentals[0]} Rental ID: {rentals[1].get_Rental_ID()}")

                    print("\nEnter the Rental Property ID to be edited/updated")

                    # User input to determine what type of property is to be edited/updated
                    while True:
                        searchRental = input("Enter the Rental_ID: ")
                        if validateRental(searchRental):
                            break
                        else:
                            print("Invalid Input Please Try Again!")

                    # Checks and displays the rental Type and prompts the user to the enter which feild is to be changed
                    rentalType = checkRental_Type(searchRental)

                    # Prompts the user to enter which feild is to be changed
                    print(f"\nThese are the available Feilds that can be edited/updated from {rentalType}")
                    print("[1] Address\n[2] Weekly Price \n[3] Furnshed(True/False) \n[4] Description")

                    if rentalType == "WholeRental":
                        print("[5] Number of Rooms\n[6] GarageSpace(if any)\n[7] Pets Allowed \n")
                    else:
                        print("[5] Couples Allowed(True/False) \n[6] Attached Bathrooms(True/False) \n")

                    while True:
                        try:
                            feildChange = int(input("Enter which Rental Feild is to be changed:"))

                            if feildChange in [1, 2, 3, 4, 5, 6, 7] and type(feildChange) == int:
                                break
                            else:
                                print(f"The option {feildChange} is not a valid,Try Again!")

                        except ValueError:
                            print("Invalid input! Please enter a valid integer.")

                    # Updates the Rental Object accordingly
                    updateRentals(rentalType, searchRental, feildChange)

                    print(f"{rentalType} with ID: {searchRental} has been successfully updated!")

            case 4:

                # Checks wheater Rental Objects exist
                if len(rentalProperty_Objects) == 0:
                    print("No Rental Propertires Created! \nPlease Enter Rental Property Details")

                else:
                    # Displays a summary of the Rental Properties in the rentalProperties lsit
                    print("These are the Existing Rental Properties and their IDs: \n")

                    for rentals in rentalProperty_Objects:
                        print(f"Rental Type: {rentals[0]} Rental ID: {rentals[1].get_Rental_ID()}")

                    print("\nEnter the Rental Property ID to be deleted")

                    # User input to determine what type of property is to be edited/updated
                    while True:
                        searchRental = input("Enter the Rental_ID: ")
                        if validateRental(searchRental) == True and searchRental[1] == "R" and (
                                searchRental[0] == "W" or searchRental[0] == "R"):
                            break
                        else:
                            print("Invalid Input Please Try Again!")

                    # Checks and displays the rental Type and prompts the user to the enter which feild is to be changed
                    rentalType = checkRental_Type(searchRental)

                    # Deletes the associated list in the data Strucuture
                    deleteRentals(searchRental, rentalType)
                    print(f"{rentalType} with ID: {searchRental} has been successfully Deleted!")

            case 5:

                if len(rentalProperty_Objects) == 0:
                    print("No Rental Propertires Created! \nPlease Enter Rental Property Details")
                else:
                    print(retreiveRentals(3))

            case 6:
                print("Backing Up Rentals...")
                backupRentals()
                print("Back up Successfully Created!")

            case 7:
                while True:
                    validatExit = str(input("Do you want to exit this application? (y/n):")).lower()
                    if validatExit == "y" or validatExit == "q":
                        exit()
                    else:
                        print("Invalid Input! Please Try again")

            case _:
                print("Invalid action, try again.")

if __name__ == "__main__":
    main()