# ------------------------------------------------- BUSINESS LOGIC LAYER -------------------------------------------------------- #

import dbAccessLayer

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
   employee = dbAccessLayer.fetchAllEmployee(num)
   return employee

 def insertEmployee(self):
   insertFlag = dbAccessLayer.insertRecord(self)
   return insertFlag

 @staticmethod
 def deleteEmployee(num):
   desiredRow = dbAccessLayer.deleteRecord(num)
   return desiredRow

 @staticmethod
 def updateEmployee(x,y,z):
   updateFlag = dbAccessLayer.updateRecord(x,y,z)
   return updateFlag