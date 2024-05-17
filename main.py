from rentalClass import *

"""

Assignment 2

Team Details: 
Savin De Alwis, Student No: 35221631
Januth Sumathiratne, Student No: 35221615
Shimar Khan, Student No: 34715282
Nishal Paranagama, Student No:34715231

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

    #Takes input for the data attributes common to both rental properties 
    rental_ID = input("Enter rental ID: ")
    address = str(input("Enter address: "))
    weeklyPrice = float(input("Enter weekly price: "))
    furnished = input("Is the property furnished? (True/False): ").lower() == 'true'
    description = input("Enter property description: ").capitalize()

    # Creates the Whole Rental Property 

    if rentalType == 1:

        # Takes input for data attributes unique to whole rental properties
        noofRooms = int(input("Enter number of rooms: "))
        noofBathrooms = int(input("Enter number of Bathrooms "))
        garageSpace = int(input("Enter garage space (if any): "))
        petsAllowed = input("Are pets allowed? (True/False): ").lower() == 'true'
        
        # Creates and Appends the Whole Rental Property to the rentelProperties Object
        rentalProperty_Objects.append(["WholeRental", WholeRental(rental_ID, address, weeklyPrice, furnished, description, noofRooms,
                                                   noofBathrooms,garageSpace, petsAllowed)])

    else:
        # Takes input for data attributes unique to whole rental properties

        couplesAllowed = input("Are couples Allowed? (True/False): ").lower() == "true"
        attachedBathroom = input("Is there a Attached Bathroom? (True/False): ").lower() == "true"

        # Creates and Appends the Whole Rental Property to the rentelProperties Object
        rentalProperty_Objects.append(["RoomRental", RoomRental(rental_ID, address, weeklyPrice, furnished, description,
                                                                couplesAllowed, attachedBathroom)])

"""
Purpose: 
    - Takes the rental type as an argument
    - Retreives the rental details based on the rentalType  

Args:
    rentalType : int

Returns:
    str
"""
# MARK: Retrieve Rentals 
def retreiveRentals(rentalType: int) -> str:
    rentalInfo : str = ""

    # Loops through the rental properties Objects
    for rentals in rentalProperty_Objects:

        #Validate the rental Type, in the following manner and adds the rentalType to rentalInfo string 
            # [1] : WholeRental 
            # [2] : RoomRental
            # [3] : All Rentals
        
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
    - This function updates various fields of rental properties based on user input.
    - It searches for the rental property using the provided rental type and ID. 
    - Then updates the specified field with the new value entered by the user.

Args:
    rentalType : str  
    rentalSearch_ID : int  
    feildChange : int 

Returns:
    None
"""
def updateRentals(rentalType: str, Rentalsearch_ID: int, feildChange: int) -> None:
    
    # Loops through the rental properties Objects
    for rentals in rentalProperty_Objects:

        #Checks gets rental Property Objects id and checks with Rentalsearch_ID parameter and that Rental Type matches wtih the rental Type parameter
        if rentals[1].get_Rental_ID() == Rentalsearch_ID and rentals[0] == rentalType:
            
            #Checks the feildChange based on these criteria: 
        #    MARK: ADD
            # And based on the criteria(above) asks the user the new feilds and calls the setter function accordingly. 

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
                rentals[1].set_noofRooms(new_NoofRooms)
            
            elif feildChange == 6 and rentalType == "WholeRental":
                new_NoofBathrooms= int(input("Enter number of Bathrooms: "))
                rentals[1].set_noofBathrooms(new_NoofBathrooms)
            
            elif feildChange == 7 and rentalType == "WholeRental":
                new_GarageSpace = int(input("Enter garage space (if any): "))
                rentals[1].set_garageSpace(new_GarageSpace)

            elif feildChange == 8 and rentalType == "WholeRental":
                new_PetsAllowed = input("Are pets allowed? (True/False): ").lower() == 'true'
                rentals[1].set_Petsallowed(new_PetsAllowed)

            elif feildChange == 5 and rentalType == "RoomRental":
                new_CouplesAllowed = input("Are couples Allowed? (True/False): ").lower() == "true"
                rentals[1].set_Couplesallowed(new_CouplesAllowed)

            elif feildChange == 6 and rentalType == "RoomRental":
                new_AttachedBathroom = input("Is there a Attached Bathroom? (True/False): ").lower() == "true"
                rentals[1].set_Attachbathroom(new_AttachedBathroom)

            else:
                print("Uncaught Exception!")


# MARK: Delete Rentals
"""
Purpose: 
    - This function deletes a rental property from the list of rental properties.
    - It searches for the rental property using the provided rental type and ID,
    - Then removes the corresponding property from the list.

Args:
    rentalID: int - 
    rentalType: str -  

Returns:
    None 
"""
def deleteRentals(rentalID: int, rentalType: str) -> None:

    # Loops through the index of of rental Property Objects
    for index in range(len(rentalProperty_Objects)):
        
        #Checks if the rental Type is the same as the rental class type in the list and that that rentalID of the rental Object is the same as the rental id parameter
        if rentalProperty_Objects[index][0] == rentalType and rentalProperty_Objects[index][
            1].get_Rental_ID() == rentalID:

            # If that is the case pops the rental object from the list, therefore deleting it
            rentalProperty_Objects.pop(index)

# MARK: Load Back Up
"""
Purpose: 
    - Load existing rental property data from a text file, create rental property objects.
    - And append them to the rental properties list if they do not already exist.
Args: 
    None

Returns:
    None 
"""
def loadRentals():

    try: 
        #Open the rentalProperties.txt file as read 
        file = open("rentalProperties.txt", "r")

        lines = file.readlines()

        # Loops through every line in lines, one by one
        for line in lines:
            line = line.replace("\n", "")

            rental_data = line.split(",")
            rental_ID = rental_data[0]

            # Adds the property from the text file to the objects list by creating an oject ONLY if it doesnt already exist
            if not(validateRental(rental_ID)):

                # Whole rental
                if len(rental_data) == 9:
                    rental_ID, address, weeklyPrice, furnished, description, noofRooms,noofBathrooms, garageSpace, petsAllowed = rental_data
                    rentalProperty_Objects.append(["WholeRental", WholeRental(rental_ID, address, weeklyPrice, furnished, description, noofRooms,noofBathrooms, garageSpace, petsAllowed)])
                # Room rental
                else:
                    rental_ID, address, weeklyPrice, furnished, description, couplesAllowed, attachedBathroom = rental_data
                    rentalProperty_Objects.append(["RoomRental", RoomRental(rental_ID, address, weeklyPrice, furnished, description, couplesAllowed, attachedBathroom)])
        file.close()

    except FileNotFoundError as fnfe: 
        print(f"File not found! {fnfe}")
    except Exception as e:
        print("Unkown exception occured!")


# MARK: Back Up
"""
Purpose: 
    -  Back up current rental property data to a text file.
     - It writes all rental properties from the rental properties list to the file,
     - Including their details, in a specific format, depending on the type of rental class

Args: 
    None

Returns:
    None 
"""
def backupRentals():
    if len(rentalProperty_Objects) == 0:
        print(f"{len(rentalProperty_Objects)} Rentals Properties to be backed up, please create Rental Properties")
    
    else: 
        try: 
            #Open the rentalProperties.txt file as write 
            file = open("rentalProperties.txt", "w")
            new_property_text = ""

            # Loops through properties in rental Object 
            for property in rentalProperty_Objects:
                property_type, property_object = property

                # Uses reach rental class getters and adds to the new_property_text
                new_property_text += f"{property_object.get_Rental_ID()},{property_object.get_address()},{property_object.get_weekly_price()},{property_object.get_furnished()},{property_object.get_description()},"

                # Checks the property_type and accordingly adds to the new property_text based on the rental type
                if property_type == "RoomRental":
                    new_property_text += f"{property_object.get_couples_allowed()},{property_object.get_attached_bathroom()}\n"
                else:
                    new_property_text += f"{property_object.get_noofRooms()},{property_object.get_noofBathrooms()},{property_object.get_garage_space()},{property_object.pets_allowed()}\n"

            file.write(new_property_text)
            print("Back up Successfully Created!")
            file.close()

        except FileNotFoundError as fnfe: 
            print(f"File not found! {fnfe}")
        except Exception as e:
            print("Unkown exception occured!")

# MARK: Utility Functions 
"""
Purpose: 
    -Validate if a rental property with the given ID already exists in the rental properties list.

Args:
    search_ID : str 

Returns:
    bool 
"""

def validateRental(search_ID: str) -> int:
    # Loops through the index of  rental Property Objects 
    for index in range(len(rentalProperty_Objects)):
        
        # Validates the search_ID and checks wheater it exists in the Rental Objects list
        if search_ID == rentalProperty_Objects[index][1].get_Rental_ID():
            return True

    return False

"""
Purpose: 
    - Validates user Rental_ID when editing and updating properties

Args:
    rentalType : accepts a integer value 

Returns:
    str 
"""

def checkRental_Type(search_ID: str) -> str:

    # Loops through the rental properties
    for [rental_type, property_object] in rentalProperty_Objects:
        
        rental_ID = property_object.get_Rental_ID()

        # Checks if the current rental ID matches the search ID
        if rental_ID == search_ID:
            # Returns the rental type if a match is found
            return rental_type

"""
Purpose: 
    - Check for duplicate rental properties by their ID in the rental properties list.
Args: 
    None

Returns:
    int : Returns the index of the second occurence of the duplicated Rental ID 
"""
def checkDuplicateRentals() -> bool:
    
    # Loop through each rental property by index
    for index_i in range(len(rentalProperty_Objects)):
        # Nested loop to compare each rental property with every other rental property
        for index_j in range(len(rentalProperty_Objects)):

            # Check if the rental IDs are the same and the indices are different
            if rentalProperty_Objects[index_i][1].get_Rental_ID() == rentalProperty_Objects[index_j][1].get_Rental_ID() and index_i != index_j:
                 
                 # Return the index of the second occurrence of the duplicated Rental ID
                return index_j

# MARK: Main
"""
Purpose: 
    - Main function to handle the user interface and control flow of the rental property management system.
    - It loads existing rentals, displays a menu for various operations, and processes user inputs
    - For creating, retrieving, updating, deleting, loading backups and backing up current rental properties.

Args: 
    None

Returns:
    None 
"""
def main():
    
    # Loads Existing rental properties from the "rentalProperties.txt" to the rentalObjects
    loadRentals()
    print(" \nLoading Rentals from your last sessions Press [5] to display loaded Rental Properties \n")

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
                
                # Checks wheater rental Objects List  exist
                if len(rentalProperty_Objects) == 0:
                    print("No Rental Propertires Created! \nPlease Enter Rental Property Details")
                else:
                    while True:
                        print("[1]Whole Rental Property \n[2]Room Rental Property\n[3]All Rental Properties \n")
                        #Gets the user input for the type of rental property to retrieve
                        rentalType = int(input("Enter the Type of Rentals do be Retreived:"))
                        
                        # Validatas the rental type input
                        if rentalType == 1 or rentalType == 2 or rentalType == 3:
                            # Calls and Prints the retreiveRentals function 
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
                        print("[5] Number of Rooms\n[6] Number of Bathrooms \n[7] GarageSpace(if any)\n[8] Pets Allowed \n")
                    else: # Rental Type is RoomRental
                        print("[5] Couples Allowed(True/False) \n[6] Attached Bathrooms(True/False) \n")

                    while True:
                        try:
                            feildChange = int(input("Enter which Rental Feild is to be changed:"))

                            if feildChange in [1, 2, 3, 4, 5, 6, 7, 8] and type(feildChange) == int:
                                break
                            else:
                                print(f"The option {feildChange} is not a valid,Try Again!")

                        except ValueError:
                            print("Invalid input! Please enter a valid integer.")

                    # Updates the Rental Object accordingly
                    updateRentals(rentalType, searchRental, feildChange)

                    print(f"{rentalType} with ID: {searchRental} has been successfully updated!")
            
            #Deletes Rental Properties 
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
                        if validateRental(searchRental) == True:
                            break
                        else:
                            print("Invalid Input Please Try Again!")

                    # Checks and displays the rental Type and prompts the user to the enter which feild is to be changed
                    rentalType = checkRental_Type(searchRental)

                    # Deletes the associated list in the data Strucuture
                    deleteRentals(searchRental, rentalType)
                    print(f"{rentalType} with ID: {searchRental} has been successfully Deleted!")

            #Displays all Avalaible Rental Properties 
            case 5:
                # Checks wheater Rental Objects exist

                if len(rentalProperty_Objects) == 0:
                    print("No Rental Propertires Created! \nPlease Enter Rental Property Details")
                else:
                    # Calls and prints the retrieveRental function for all rental properties in the rental objects list 
                    print(retreiveRentals(3))

            # Backs up the existing Rental Properties in the Rental Objects 
            case 6:
                #Simply Backs up Rentals
                print("Backing Up Rentals...")
                backupRentals()

            # Quits the application
            case 7:
                while True:
                    # Rechechs with the user if they are sure they want to exit the application
                    validate_Exit = str(input("Do you want to exit this application? (y/n):")).lower()
                    
                    # validates the validate_exit input
                    if validate_Exit == "y" or validate_Exit == "q":
                        exit()
                    else:
                        print("Invalid Input! Please Try again")

            case _:
                print("Invalid action, try again.")

# Run the main function
if __name__ == "__main__":
    main()