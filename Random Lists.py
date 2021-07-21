# This is a random weighted list

import random

user_input = int(input("Enter a number: "))

list_1 = ["red", "blue", "green", "yellow"]
list_2 = ["one", "two", "three", "four"]
list_3 = ["up", "down", "left", "right"]
list_4 = ["hi", "low", "middle"]
compiled_lists = [list_1, list_2, list_3, list_4]


def get_random_number():
    random_list = random.choices(compiled_lists, cum_weights=(25, 50, 75, 100), k=1)
    list_length = len(random_list[0])
    random_item = random.choice(random_list)[random.randrange(list_length)]
    print(random_item)


for i in range(user_input):
    get_random_number()
