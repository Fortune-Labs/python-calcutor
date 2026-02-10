number1 = 200

numnber2 = 100

def add(a, b):
    return a + b

def subtract(a,b):
    return a-b

def divide(a,b):
    if b == 0:
        print("Error : divison by zero error!!")

    return a/b

def multiply(a,b):
    return a*b



while True:

    print("Option 1 : ADDITON")
    print("Option 2 : SUBTRACTION")
    print("Option 3 : DIVISION")
    print("Option 4 : MULTIPLICATION")
    print("Option 5 : EXIT")


   
    while True :

        option = input("Dear user input the Option you want :")

        if option in ("1","2","3","4","5"):
            break
        
        else :
            print(f"Invalid input !!! , Type in a valid input")


    
    if option == "5":
            print("You can safely exit the calculator then !!! ")       
            break

    if option in ("1","2","3","4"):

        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number:"))

    
        if option == "1":
            print("result: " ,add(num1,num2))

        elif option == "2":
            print("result: " ,subtract(num1,num2))

        elif option == "3":
            print("result: " ,divide(num1,num2))
        
        elif option == "4":
            print("result: " ,multiply(num1,num2))


    break
            
