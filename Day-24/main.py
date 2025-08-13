# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()


with open("new_file.txt", mode = "a") as file:
    # contents = file.read()
    file.write("\nNew text")
