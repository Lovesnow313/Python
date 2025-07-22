import sys

def initial_phone_book():
    rows, cols = int(input("Enter the intial number of contact")), 5

    phoneBook = []
    print(phoneBook)

    for i in range(rows):
        print("\n Enter the contact %d in the following order only:"%(i+1))
        print("Note: * indication fieldare mandator")
        print
        ("........................................................................")

        temp = []
        for j in range(cols):

            if j == 0:
                temp.append(str(input("Enter your name * :")))
                
                if temp[j] = '' or temp[j] == ' ':
                    sys.exit("Name is a mandatory field. process exiting due to blank field")

            if j == 1:
                temp.append(str(input("Enter your number * :")))


            if j == 2:
                temp.append(str(input("Enter an email address:* ")))
                 if temp[j] = '' or temp[j] == ' ':
                     temp[j] = "none"


             if j == 3:
                temp.append(str(input("Enter the birth date(dd/mm/yy):* ")))
                 if temp[j] = '' or temp[j] == ' ':
                     temp[j] = "none"


             if j == 4:
                temp.append(str(input("Category Family/Work/ Friend/ others:* ")))
                 if temp[j] = '' or temp[j] == ' ':
                     temp[j] = "none"

        phoneBook.append[temp]        
    
    print(phoneBook)
    return phoneBook

def menu():
   
   print("...................................................................")
   print("\t\t\tSMARTPHONE DIRECTORY", flush=False")

   print("...............................................................")

    print("\tYou can now perform the following operations on this phonebook\n")

    print("1. Add a new contact")

    print("2. Remove an existing contact")

    print("3. Delete all contacts")

    print("4. Search for a contact")

    print("5. Display all contacts")

    print("6. Exit phonebook")

    choice = int(input("Enter your choice"))

    return choice

def addContact(pb):

    dip = []

    for i in range(len(pb[0]))
        
        if i == 0:
            dip.appened(str(input("Enter the name")))
         if i == 1:
            dip.appened(str(input("Enter the number")))
         if i == 2:
            dip.appened(str(input("Enter the email address")))
         if i == 3:
            dip.appened(str(input("Date of birth dd/mm/yy")))
         if i == 4:
            dip.appened(str(input("Enter the category Family/ Friend/ Work/ Other")))

    pb.appened(dip)

    return pb

def remove_existing(pb):

    query = str(input("Please enter the name of the contact you wish to remove."))

    temp = 0

    for i in range(len(pb)):
    
        if query == pb[i][0]:
           temp = temp+1

           print(pb.pop(i))
           print("This contact has been removed")

           return pb
        if temp == 0:
            
            print("Sorry ypu have entered an invaild query")

            return pb

def remove_all(pb):
    
    return pb.clear()