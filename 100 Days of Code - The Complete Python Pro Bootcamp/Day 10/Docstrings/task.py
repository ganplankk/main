# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
#
# formatted_name = format_name("AnGeLa", "YU")
#
# length = len(formatted_name)
#

# def format_name(f_name, l_name):
#
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
# print(format_name(input("Your first name"), input("Your last name")))


def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if year % 4 == 0 and not year % 100 == 0 and not year % 400 == 0:
        print("leap")
        return True
    else:
        return False
print(is_leap_year(2400))



