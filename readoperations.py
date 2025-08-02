file = open("sample.txt", "r")

print(file.read())
file.close()

file = open("sample.txt", "r")
print("\n read the first 12 character. \n")
print(file.read(12))

file.close()
file = open("sample.txt", "a")
file.write("All of the places are very beutiful and fresh.")
file.close()
