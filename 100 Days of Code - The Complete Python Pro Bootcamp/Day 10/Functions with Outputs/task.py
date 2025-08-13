#
# def format_name(first_name, last_name):
#     result_first = ''
#     result_last = ''
#     j = 0
#     for i in first_name:
#         if j == 0:
#             result_first+=i.upper()
#             j+=1
#         else:
#             result_first+=i
#     j = 0
#     for i in last_name:
#         if j == 0:
#             result_last+=i.upper()
#             j+=1
#         else:
#             result_last+=i
#     return result_first + ' ' + result_last
#
# f_name=input("firstname")
# l_name=input("lastname")
# full_name=format_name(first_name= f_name, last_name= l_name)
# print(str(full_name))

def format_name(f_name, l_name):

    tmp_first=f_name.title()
    tmp_last=l_name.title()
    return tmp_first + ' ' + tmp_last

first=input("first name\n")
last=input("last name\n")

print(format_name(f_name=first, l_name=last))

