# Python program to identify common items in two lists

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_items = []

for item in list1:
    if item in list2:
        common_items.append(item)

print("Common items are:", common_items)