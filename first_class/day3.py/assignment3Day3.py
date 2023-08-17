rows = 3
columns = 3
#create an empty list to store matrix
matrix = []
#loop through each row
for i in range(rows):
    row = []
    #create an empty list for each row
    for j in range(columns):
    #prompt user to input a value for the current element
        value = float(input("Enter value for row" + str(i+1) + ",column" + str(j+1) + ":"))
        row.append(value) 
    #add the value to the current row
    matrix.append(row)
    #add the current row to the matrix
    #display the entered matrix 
    matrix:()
for row in matrix:
        print(row)
        #print each row of the matrix
