import businessLogicLayer
import re

#------------------------------------------------ IDENTITY FUNCTION -----------------------------------------<
# Identity the User as an Employee With the help of User ID
def identity():

 user_Id = input("Enter your User ID : ")
 user_Id = user_Id.strip()
 user_Id = user_Id.upper()
 idPAss = input("Enter your ID password : ")

# Pattern of UserID
 idPattern = re.compile(r"^\d{4}TKP$")

 if re.search(idPattern,user_Id):
  print("Access Granted!")
  return True
 else:
  print("Access Denied!")
  return False

#------------------------------------------------ SELECT FUNCTION -----------------------------------------<
def selectFunct():

# Calling Static Method
    data = businessLogicLayer.Employee.getAllEmployee()
    num = 1
    for row in data:
      print(f"Row {num}: ",row)
      num +=1
    else:
      print("Completed! :-)")

# Program Terminated  
    exit("Program Terminated!")

#------------------------------------------------ INSERT FUNCTION -----------------------------------------<
def insertFunct():

# all insert values (total 8)
    fName = input("Enter your First Name: ")
    mName = input("Enter your Middle Name (skip if not): ")
    lName = input("Enter your Last Name: ")
    designation = input("Enter your Designation: ")
    joinDate = input("Enter your Join Date (YYYY-MM-DD): ")
    salary = input("Enter your Salary: ")
    address_ = input("Enter your Address: ")
    city = input("Enter your City: ")

    aDataList = {'First Name': fName, 'Middle Name': mName, 'Last Name': lName, \
      'Designation': designation, 'Join Date': joinDate, 'Salary': salary, 'Address': address_, 'City': city }

    for k,v in aDataList.items():
      
      if k == 'Middle Name':
        continue

      elif v == '':
        print('******************************************************************')
        print('ALL FIELDs are MANDATORY')
        print('******************************************************************')
        insertFunct()

# Creating Instance
    insertInstance = businessLogicLayer.Employee(fName,mName,lName,designation,joinDate,salary,address_,city)
    flagValue = insertInstance.insertEmployee()
    
    if flagValue == True:
      print("Insertion Completed! :-)")
    else:
      print("Insertion Not Completed! :-(")

# Program Terminated  
    exit("Program Terminated!")

#------------------------------------------------ DELETE FUNCTION -----------------------------------------<
def deleteFunct():
    for i in range(3): 
     num = int(input("Please Enter Employe Number: "))

     if num > 0:
       row = businessLogicLayer.Employee.getAllEmployee(num)
       print(f"Employee Number {num} = ",row)

       print("\nConfirm to Delete :","YES or NO",sep="\n" )
       action = input("")

       action = action.lower()

       if action == 'yes':
        flagValue = businessLogicLayer.Employee.deleteEmployee(num)
        
        if flagValue == True:
          print("Deletion Completed :-)")
        else:
          print("Deletion Not Completed :-(")
        
        exit("Program Terminated!")

       elif action == 'no':
        print("Action Cancelled")
        exit("Program Terminated!")
       else:
        print("Unknown value Entered!")
        exit("Program Terminated!")

# Incorrect Keyword
     else:
       if i < 2:
        print("Employee Number can't be negative!")
# Program Terminated (3 try Only)  
       else:
        exit("Program Terminated!")

#------------------------------------------------ UPDATE FUNCTION -----------------------------------------<
def updateFunct():
  
  num = int(input("Please Enter the empNo you want to update :"))
  print("Please Choose below options you want to update : ")
  print("[1] for fName","[2] for mName","[3] for lName","[4] for designation","[5] for joinDate","[6] for salary","[7] for address_","[8] for city",sep="\n")
  
  for i in range(3): 
   action = int(input())

   if action > 0 and action < 9:
    dictOfCol = {1:"fName",2:"mName",3:"lName",4:"degination",5:"joinDate",6:"salary",7:"address_",8:"city"}
    changeData = input(f"Enter Update detail of {dictOfCol[action]} : ")
    changeData = changeData.capitalize()
    changeCol = dictOfCol[action]

# Calling Static Method
    flagValue = businessLogicLayer.Employee.updateEmployee(changeCol,changeData,num)

    if flagValue == True:
       print("Updation Completed! :-)")
    else:
       print("Updation Not Completed! :-(")

# Program Terminated
    exit("Program Terminated!")

# Incorrect Keyword
   else:
    if i < 2:
     print("Please Enter the correct Number!")
# Program Terminated (3 try Only)  
    else:
     exit("Program Terminated!")

#------------------------------------------------- MAIN FUNCTION ------------------------------------------<
def main():
 print("""
       ***************************************** WELCOME TO THE *****************************************
       **************************************************************************************************
                                                 The KHAN PYCODE  
       **************************************************************************************************""")

# Checking User Identity
 print("Identityfy Yourself as an Employee Please!")
 identifyFlag = identity()
  
# User is not an Employee
 if identifyFlag == False:
  exit("Program Terminated!")

# User is an Employee
 else:
  print("Kindly choose one option to move further : ")
  print("1. [F] to Fetch All the Employee Records.")
  print("2. [I] to Insert an Employee Record.")
  print("3. [D] to Delete an Employee Record.")
  print("4. [U] to Update an Employee Record.",end="\n\n")

  for i in range(3):
   action = input("")
   action = action.upper()

# Fetching All Records of Employee
   if action == "F":
    selectFunct()

# Inserting Record of Employee
   elif action == "I":
    insertFunct()

# Deleting Record of Employee
   elif action == "D":
    deleteFunct()

# Updating Record of Employee
   elif action == "U":
    updateFunct()

# Incorrect Keyword
   else:
    if i < 2:
     print("Please Enter the correct Key!")
# Program Terminated (3 try Only)  
    else:
     exit("Program Terminated!")


#------------------------------------------- PROGRAM START FROM HERE ------------------------------------------<
main()
#--------------------------------------------------------------------------------------------------------------<


