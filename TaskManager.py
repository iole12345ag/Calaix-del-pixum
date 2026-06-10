nombreDelArchivo = "TasksManager.txt"

with open(nombreDelArchivo,"a",encoding="utf-8") as file:
    pass

while True:
     
    print("This is a task manager, what do you want to do?")
    print("1. Add tasks")
    print("2. See my tasks")
    print("3. Delete task")
    print("4. Exit")



    option = float(input("Choose the action do you want to perform (the number): "))

    if option == 1:

            taskAdded = str(input("Type the task that do you want to save: "))
            with open(nombreDelArchivo,"a",encoding="utf8") as pepe:
                pepe.write(taskAdded + "\n")



    if option == 2:
        
        with open(nombreDelArchivo,"r", encoding="utf8") as pepe:
            contenido=pepe.read()
            print("HERE ARE YOUR TASKS \n")
            print(contenido)
            print("-------------------------------")
            
    if option == 3:
        
        with open(nombreDelArchivo,"r", encoding="utf8") as pepe:
            lineas = pepe.readlines() # readlines() saves each line as an element of a list

        print("Select the action do that you want to delete")

        for i, linea in enumerate(lineas):
            print(f"{i+1}. {linea.strip()}")

        numberToDelete= int(input("Type the number of the task do you want to delete:  "    ))

        RealNumberToDelete = numberToDelete - 1    

        if 0 <= RealNumberToDelete < len(lineas):
            TaskDeletet = lineas.pop(RealNumberToDelete)
            print(f"has eliminado la linea {numberToDelete}")
            
            with open(nombreDelArchivo,"w", encoding="utf8") as pepe:
                pepe.writelines(lineas)
        else:
            print("The number typed isn't valid")

    if option == 4:
        break

    else:
        print("Invalid option, choose a number between 1 and 4")