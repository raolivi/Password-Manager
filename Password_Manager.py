pwd = input("What is the master password? ")


while pwd != "Santino":
    pwd = input("Wrong password. Please re-enter: ")

if pwd == "Santino":

    mode = input("Would you like to add a new password or view existing ones? (view, add) press q to quit: ")

    def view():
        
        with open("paswords.txt", "r") as f:
            for line in f.readlines():
                print(line.rstrip())

    def add():
        name = input("Account Name: ")
        pwd = input("Password: ")

        with open("paswords.txt", "a") as f:
            f.write(name + " | " + pwd + "\n") 

    while True:

        if mode == "q":
            break
        
        if mode == "view":
            view()
            mode = input("Would you like to add a new password or view existing ones? (view, add) press q to quit: ")

        elif mode == "add":
            add() 
            mode = input("Would you like to add a new password or view existing ones? (view, add) press q to quit: ")
        else:
            print("Invalid mode.")
            continue

    
    