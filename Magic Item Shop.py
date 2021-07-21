import random

print("1: village")
print("2: town")
print("3: city")
settlement_size = int(input("Enter a number: "))

if settlement_size == 1:
    settlement_size = 'village'
elif settlement_size == 2:
    settlement_size = 'town'
elif settlement_size == 3:
    settlement_size = 'city'
else:
    print("Invalid input!")


def calculate_number_of_magic_items(settlement):
    if settlement == 'village':
        magic_items = random.randrange(5, 10)
    elif settlement == 'town':
        magic_items = random.randrange(5, 15)
    elif settlement == 'city':
        magic_items = random.randrange(10, 20)
    else:
        magic_items = 0
    return magic_items


magic_item_count = calculate_number_of_magic_items(settlement_size)
print(f"Number of magical items: {magic_item_count}")

armor_list = ["Padded", "Leather", "Studded leather", "Hide", "Chain shirt", "Scale mail", "Breastplate", "Half plate",
              "Ring mail", "Chain mail", "Splint", "Plate", "Shield"]
weapon_list = ["shortsword", "longsword", "longbow", "mace", "dagger"]
potion_list = ["potion of healing", "potion of giant strength", "potion of invisibility"]
wand_list = ["wand of fireballs", "wand of magic missiles", "wand of detect magic"]
store_item_list = [armor_list, weapon_list, potion_list, wand_list]


def generate_store_list():
    store_item_category = random.choices(store_item_list, cum_weights=(25, 55, 85, 100), k=1)
    list_length = len(store_item_category[0])
    random_item = random.choice(store_item_category)[random.randrange(list_length)]
    print(random_item)


print("Items in your shop: ")

for i in range(magic_item_count):
    generate_store_list()
