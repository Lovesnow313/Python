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
