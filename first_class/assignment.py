import math

username = str(input("Enter your username : "))
age = int(input("Enter your age : "))

#valid users list
#validUsers = ['Janet','Faith','Alex']
#check if the username is valid
#if username in validUsers :
if username == 'Janet' or username == 'Faith' or username =='Alex':
    #check if age is  greater than 20
    if age > 20 :
        #ask for input variables a and b
        a = int(input("Enter the first number (a) :"))
        b = int(input("Enter the second number (b) :"))
        #ask for desired operation
        operation = input("Enter the operation you want to perform(add/subtract/multiply/divide) : ")
        #perform the selected operation
        if operation == "add" :
            result = a+b
            print(a+b)
        elif operation == "subtract" :
            result = a-b
            print(a-b)
        elif operation == "multiply" :
            result = a*b
            print(a*b)
        elif operation == "divide" : 
            result = a/b
            print(a/b)
        else :
            result = none 
            #operation not supported

            #print the result
            if result is not none :
                print("The result is " + result)
            else :
                print("invalid operation")
    else :
        print("Sorry,you must be 20 years or older to use this calculator.")
else :
    print("Sorry,you are not allowed to use this calculator.")

            




    
