users = [] 

#allowing the user to input username and password
username = str(input("Enter username : "))
password = int(input("Enter password : "))
#creating a dictionary using the input variables
user = {"username": username, "password" : password}

#appending the user dictionary to the list 
users.append(user)

#printing the list of user instances
print(users)