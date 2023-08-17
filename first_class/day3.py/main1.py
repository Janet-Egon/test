def arithmetic(a,b, operation):
    if operation == "add" :
        result = a+b

    elif operation == "subtract":
        result = a-b

    elif operation == "multiply":
        result =a*b

    elif operation == "divide":
        if b != 0:
            result = a/b
            
        else:
         result = None
        return print("error:cannot be divide by zero")
    else :
        result=None
        return print("invalid")
    
    return print("Result:",result)

arithmetic(3,0,"subtract")

    