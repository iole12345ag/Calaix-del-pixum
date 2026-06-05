while True:

    print("What operation do you want to do?")
    print("1. + ")
    print("2. - ")
    print("3. * ")
    print("4. / ")    

    option = input("What's your choice?(type the number of the command): ")
   
    firstNumber = float(input("What's your first number?: "))

    SecondNumber = float(input("What's your second number?: "))
 
    if option == ("1"):
        result =(firstNumber + SecondNumber)
       
        print(f"The result of the ecuation is {result}")
    if option == ("2"):
        result =(firstNumber - SecondNumber)
        print(f"The result of the ecuation is {result}")
       
    if option == ("3"):
        result =(firstNumber * SecondNumber)
        print(f"The result of the ecuation is {result}")
       
    if option == ("4"):
        result =(firstNumber / SecondNumber)
        print(f"The result of the ecuation is {result}")
