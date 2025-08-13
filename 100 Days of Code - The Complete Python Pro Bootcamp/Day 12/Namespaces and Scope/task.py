# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")
#
#
#


enemies = 1


def increase_enemies(enemy):
    print(f"enemies inside function: {enemy}")
    return enemy + 1



increase_enemies(enemies)
print(f"enemies outside function: {enemies}")



