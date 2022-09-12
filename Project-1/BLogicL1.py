import DbAccessL1

class Employee:
 """Here is Employee Table"""
 
 def __init__(self,fName,mName,lName,	designation,joinDate,salary,address_,city):
  self.fName = fName.capitalize()
  self.mName = mName.capitalize()
  self.lName = lName.capitalize()
  self.designation = designation.capitalize()
  self.joinDate = joinDate
  self.salary = salary
  self.address_ = address_.capitalize()
  self.city = city.capitalize()
 
 @staticmethod
 def getAllEmployee(num = -1):
   employee = DbAccessL1.fetchAllEmployee(num)
   return employee

 def insertEmployee(self):
   insertFlag = DbAccessL1.insertRecord(self)
   return insertFlag

 @staticmethod
 def deleteEmployee(num):
   desiredRow = DbAccessL1.deleteRecord(num)
   return desiredRow

 @staticmethod
 def updateEmployee(x,y,z):
   updateFlag = DbAccessL1.updateRecord(x,y,z)
   return updateFlag