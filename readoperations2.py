file1 = open("Codingal.txt.txt", "r")
file2 = open("sample.txt", "w")

for x in file1.readlines():
    if not (x.startswith("Codingal")):
        print("\n the line without coding. \n")
        print(x)


   



file1.close()
file2.close()