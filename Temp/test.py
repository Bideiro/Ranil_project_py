# Example multi-dimensional list
multi_dimensional_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Value to find
value_to_find = 5

# Flag to check if value is found
value_found = False

# Iterate through the multi-dimensional list
for sublist in multi_dimensional_list:
    for item in sublist:
        if item == value_to_find:
            print(f"Element found: {item}")
            value_found = True
            break
    if value_found:
        break

if not value_found:
    print("Value not found in the list.")
