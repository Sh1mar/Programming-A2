from rentalClass import *

"""
Questions : Do we have to generat the Rental ID ourselves 
Method to update and edit properties like same with deletign the records 
"""

rentalProperty_Objects : list = []

#MARK: Enter Rentals
def enterRentals(rentalType : int) -> None:
   
   rental_ID = input("Enter rental ID: ")
   address = str(input("Enter address: "))
   weeklyPrice = float(input("Enter weekly price: "))
   furnished = input("Is the property furnished? (True/False): ").lower() == 'true'
   description = input("Enter property description: ")

   if rentalType == 1:
      noofRooms = int(input("Enter number of rooms: "))
      garageSpace = int(input("Enter garage space (if any): "))
      petsAllowed = input("Are pets allowed? (True/False): ").lower() == 'true'

      rentalProperty_Objects.append(["WholeRental" ,WholeRental(rental_ID,address,weeklyPrice,furnished,description,noofRooms,garageSpace,petsAllowed)])
   
   else: 
      couplesAllowed = input("Are couples Allowed? (True/False): ").lower() == "true"
      attachedBathroom = input("Is there a Attached Bathroom? (True/False): ").lower() == "true"

      rentalProperty_Objects.append(["RoomRental",RoomRental(rental_ID,address,weeklyPrice,furnished,description,couplesAllowed,attachedBathroom)])

#MARK: Retreive Rentals 
def retreiveRentals(rentalType : int) -> str: 

   rentalInfo = ""
   for rentals in rentalProperty_Objects:
      
      if rentalType == 1 and rentals[0] == "WholeRental" : 
            rentalInfo += rentals[1].displayRental() + "\n"
           
      if rentalType == 2 and rentals[0] == "RoomRental" : 
            rentalInfo += rentals[1].displayRental() + "\n"

      if rentalType == 3: 
         rentalInfo += rentals[1].displayRental() + "\n"
   
   return rentalInfo 

      
#MARK: Edit and Update Details of Rental Properties 
def updateRentals(rental_ID : int, update_element, ): 
   pass 




#MARK: Delete Rentals          

def deleteRentals(rentalid : int): 
   pass 




#MARK: Display 





#MARK: Back Up




#MARK: Main
def main(): 

   #Test Cases 

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

   rentalProperty_Objects.append(["WholeRental",whole_rental])
   rentalProperty_Objects.append(["RoomRental",room_rental])
   
   while True: 
      print(" \n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
      print("             Student Accommodation Monash (SAM)             " ) 
      print( " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " )
      print("[1] Enter Rental Property Details \n[2] Retrieve details of Rental Properties \n[3] Edit and Update details of Rental Properties \n[4] Delete Rental Properties  \n[5] Display Avalaible Rental Properties\n[6] Output Avalaible Rental Properties to a File \n[7] Exit! ")

      while True: 
         userChoice = int(input("Select option : "))
         if userChoice in [1,2,3,4,5,6,7]: 
            break
         else: 
            print("Invalid Input Please Try Again!")

      match userChoice:
         case 1: 
            
            while True: 
               rentalType = int(input("Enter the Type of Rental Property: \n[1]Whole Rental Property \n[2]Room Rental Property\n"))
               if rentalType == 1 or rentalType == 2: 
                  break
               else: 
                  print("Invalid Input Please Try Again!")

            enterRentals(rentalType)
               
         case 2: 

            if len(rentalProperty_Objects) == 0:
               print("No Rental Propertires Created!")
            else:
               while True: 
                  rentalType = int(input("Enter the Type of Rentals do be Retreived: \n[1]Whole Rental Property \n[2]Room Rental Property\n[3]All Rental Properties \n"))
                  if rentalType == 1 or rentalType == 2 or rentalType == 3: 
                     break
                  else: 
                     print("Invalid Input Please Try Again!")
                  
               print(retreiveRentals(rentalType))
               
         
         case 3:

            #User input to determine what type of property is to be edited/updated 
            while True: 
               rentalType = int(input("Enter the Type of Rentals do be updated/edited: \n[1]Whole Rental Property \n[2]Room Rental Property\n"))
               if rentalType == 1 or rentalType == 2: 
                  break
               else: 
                  print("Invalid Input Please Try Again!")
            
            print("These are the Existing Rental Properties and their IDs \n")
            for index in range(len(rentalProperty_Objects)): 
               print(f" Rental Type :  {rentalProperty_Objects[index][0]} Rental ID : {rentalProperty_Objects[index][1].getRental_ID()}") 
            

         case 4 : 
            pass 

         case 5 : 
            pass 

         case 6 : 
            pass 

         case 7 :
            exit()   
         
         case _:
            print("Invalid action, try again.")


if __name__ == "__main__":
    main()