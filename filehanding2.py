file_read = open("sample.txt", "r")

print(file_read.read())

file_read.close()

file_write = open("sample.txt", "w")

file_write.write("Hello, I love to travel a lot. I like ocean and forest very much")

file_write.close()

file_appened = open("sample.txt", "a")
file_appened.write("Hello, I love to travel a lot. I like ocean and forest very much")

file_appened.close()