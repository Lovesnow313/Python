with open('Coding.txt.txt', 'w') as file:
    file.write("Hello this Jessica. i love to do coding and enjoy the teaching of coding.")
file.close


with open('Coding.txt.txt', 'r') as file:
    data = file.readlines()

    print("Splitting the lines with split() function")

    for line in data:
        word = line.split()
        print(word)

file.close()