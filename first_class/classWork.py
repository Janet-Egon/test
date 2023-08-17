cars = ['hilux','toyota','lexus']
userChoice = str(input("do you want to add or remove from the list :"))
if userChoice =="add" :
 newCars1 = str(input("Enter your first car :"))
 newCars2 = str(input("enter your second car :"))
 cars.append(2)
if userChoice == "add" :
 cars.append(newCars1)

#if remove
cars.remove(1)
#print(newCars1,newCars2)
print(cars)

#print(type(cars))