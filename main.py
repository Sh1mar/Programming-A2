from rentalClass import *

"""
Questions : Do we have to generat the Rental ID ourselves 
Method to update and edit properties like same with deletign the records 
"""

rentalProperty_Objects : list = []

#MARK: Enter Rentals
def enterRentals():

   while True: 
      rentalType = int(input("Enter the Type of Rental Property: \n[1]Whole Rental Property \n[2]Room Rental Property\n"))
      if rentalType == 1 or rentalType == 2: 
         break
      else: 
         print("Invalid Input Please Try Again!")
   
   if rentalType == 1: 
     
      rental_ID = input("Enter rental ID: ")
      address = str(input("Enter address: "))
      weeklyPrice = float(input("Enter weekly price: "))
      furnished = input("Is the property furnished? (True/False): ").lower() == 'true'
      description = input("Enter property description: ")
      noofRooms = int(input("Enter number of rooms: "))
      garageSpace = int(input("Enter garage space (if any): "))
      petsAllowed = input("Are pets allowed? (True/False): ").lower() == 'true'
      
      rentalProperty_Objects.append(["WholeRental" ,WholeRental(rental_ID,address,weeklyPrice,furnished,description,noofRooms,garageSpace,petsAllowed)])
   
   else:
      rental_ID = input("Enter rental ID: ")
      address = str(input("Enter address: "))
      weeklyPrice = float(input("Enter weekly price: "))
      furnished = input("Is the property furnished? (True/False): ").lower() == "true"
      description = input("Enter property description: ")
      couplesAllowed = input("Are couples Allowed? (True/False): ").lower() == "true"
      attachedBathroom = input("Is there a Attached Bathroom? (True/False): ").lower() == "true"

      rentalProperty_Objects.append(["RoomRental",RoomRental(rental_ID,address,weeklyPrice,furnished,description,couplesAllowed,attachedBathroom)])

#MARK: Retreive Rentals 
def retreiveRentals(rentalType : int) -> str: 
   
   rentalInfo = ""

   for index in range(len(rentalProperty_Objects)):
      
      if rentalType == 1: 
         if rentalProperty_Objects[index][0] == "WholeRental":
            rentalInfo  = rentalProperty_Objects[index][1].displayRental()
      
      if rentalType == 2:
         if rentalProperty_Objects[index][0] == "RoomRental":
            rentalInfo  = rentalProperty_Objects[index][1].displayRental()
      
      if rentalType == 3:
         print("All Rental Properties") 
         rentalInfo = rentalProperty_Objects[index][1].displayRental()

   return rentalInfo
      
#MARK: Edit and Update Details of Rental Properties 




#MARK: Delete Rentals          

def deleteRentals(rentalid : int): 
   pass 




#MARK: Display 





#MARK: Back Up




#MARK: Main
def main(): 
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
            enterRentals()
            print(rentalProperty_Objects)
        
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
            pass 

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