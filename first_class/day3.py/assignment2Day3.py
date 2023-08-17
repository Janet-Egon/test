class User :
    def ___init___(self, username, fullname, location, password, stateOfOrigin, dateOfBirth ) :
        self.username = username
        self.fullname = fullname
        self.location = location
        self.password = password
        self.stateOfOrigin = stateOfOrigin
        self.dateOfBirth = dateOfBirth
        #create empty list to store user info
    users = []
    #allowing the user to input user information
    username = input("username:")
    fullname = input("fullname:")
    location = input("location:")
    password = input("password:")
    stateOfOrigin = input("stateOfOrigin:")
    dateOfBirth = input("dateOfBirth:")
    #creating an instance of the User class with the provided inputs
    user = (username,fullname,location,password,stateOfOrigin,dateOfBirth)
    #appending the user instance to the list
    users.append(user)
    #printing the list of user instances
    for user in users :
        print(user)
        #printing the attributes of the user instance

        

