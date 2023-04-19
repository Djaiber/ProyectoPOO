import datetime

class User:

    def __init__(self,userID,name,password,date) -> None:
        self.userID = userID
        self.name = name
        self.password = password
        self.date = date

    def verifylogin():
        pass

class Cliente(User):

    def __init__(self, userID, name, password, date,email,phone) -> None:
        super().__init__(userID, name, password, date)

        self.email = email
        self.phone = phone

    def register():
        pass 

    def login():
        pass

class Admin(User):

    def __init__(self, userID, name, password, date,adminname,adminemail) -> None:
        super().__init__(userID, name, password, date)

        self.adminname = adminname
        self.adminemail = adminemail

    def checksales():
        pass

class Shopping(Cliente):

    def __init__(self, userID, name, password, date, email, phone,shoppingcode,shoppingdate,value,bonopoints) -> None:
        super().__init__(userID, name, password, date, email, phone)

        self.shoppingcode = shoppingcode
        self.shoppingdate = shoppingdate
        self.value = value
        self.bonopoints = bonopoints

    def registerbuy():
        pass

    def convertpoints():
        pass 

    def deletebuy():
        pass 

    def showhistorial():
        pass

class Bonification(Shopping):

    def __init__(self, userID, name, password, date, email, phone, shoppingcode, shoppingdate, value, bonopoints,redeemedpoints,pointsbalance,bonotype) -> None:
        super().__init__(userID, name, password, date, email, phone, shoppingcode, shoppingdate, value, bonopoints)

        self.redeemedpoints = redeemedpoints
        self.pointsbalance = pointsbalance
        self.bonotype = bonotype

    def pickup():
        pass

administrador = Admin("1619135","Martadmin","distripizza@gmail.com","000","Martha","password","date")
customer1 = Cliente("123","Juan","***","18/04","juandiego@gmail.com",310461)
shopping1 = Shopping(customer1.userID,customer1.name,customer1.password,customer1.date,customer1.email,customer1.phone,"EBX474","19/04",12000,1200)


print(customer1.userID)
    

