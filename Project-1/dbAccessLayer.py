import pyodbc

def cursor_():
        conStr = 'Driver={Sql server}; Server=SUPINEBOI\SQLEXPRESS; Database=Project1'
        conct = pyodbc.connect(conStr)
        cursor = conct.cursor()
        return cursor

def fetchAllEmployee(num):

        cur = cursor_()
        query = ""
        if num == -1:
         query = "Select * from tblEmployee;"
        else:
         query = f"Select * from tblEmployee where empNo = {num};"
         
        cur.execute(query)
        row = cur.fetchall()
        return row

def insertRecord(data):
        num = maxEmpNo()
        num += 1
        query = f"Insert tblEmployee values({num},'{data.fName}','{data.mName}','{data.lName}','{data.designation}','{data.joinDate}',{data.salary},'{data.address_}','{data.city}')"
        cur = cursor_()
        flag = True

        try : 
          cur.execute(query)
          cur.commit()

        except Exception as a:
                print(a)
                flag = False
        finally:
                return flag

def deleteRecord(num):
        
        query = f"Delete from tblEmployee where empNo = {num};"
        cur = cursor_()
        flag = True
        try : 
          cur.execute(query)
          cur.commit()

        except Exception as a:
                print(a)
                flag = False
        finally:
          return flag

def updateRecord(x,y,z):
        
        query = f"Update tblEmployee set {x} = '{y}' where empNo = {z};"
        cur = cursor_()
        flag = True
        try : 
          cur.execute(query)
          cur.commit()

        except Exception as a:
                print(a)
                flag = False
        finally:
          return flag

def maxEmpNo():
        query = "Select max(empNo) from tblEmployee"
        cur = cursor_()
        n = cur.execute(query)
        count = cur.fetchone()[0]
        return count
