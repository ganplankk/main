import os

#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

file_path = r"C:\Users\USER\PycharmProjects\Days-25\Mail Merge Project Start\Input\Letters\starting_letter.txt"
name_path = r"C:\Users\USER\PycharmProjects\Days-25\Mail Merge Project Start\Input\Names\invited_names.txt"
# send_path = r"C:\Users\USER\PycharmProjects\Days-25\Mail Merge Project Start\Output\{name[i]}"

HOLDER = "[name]"

with open(name_path, "r") as n:
    name = n.readlines()
    for i in range(len(name)):
        with open(file_path, "r") as f:
            content = f.read()
            letter = content.replace(HOLDER, name[i].strip())
            send_path = f"Input\\{name[i].strip()}.txt"
            with open(send_path, "w") as x:
                print(os.getcwd())
                x.write(letter)




# print(content)
# for name in name_path:
# with open("Mail Merge Project Start\Input\Letters\starting_letter.txt", "rw") as f:
#     f.read()
