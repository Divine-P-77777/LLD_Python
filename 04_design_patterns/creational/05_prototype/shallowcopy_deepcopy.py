import copy

list1 = [1, 4, 5, 2, [65, 43, 21, 54], 99, 76, 54]

# Shallow Copy
list2 = copy.copy(list1)

# Deep Copy
list3 = copy.deepcopy(list1)

list2[4][1] = 1000
list3[4][1] = 2000

print("Original:", list1)
print("Shallow:", list2)
print("Deep:", list3)

print(id(list1[4]))
print(id(list2[4]))
print(id(list3[4]))


# Original: [1, 4, 5, 2, [65, 1000, 21, 54], 99, 76, 54]
# Shallow:  [1, 4, 5, 2, [65, 1000, 21, 54], 99, 76, 54]
# Deep:     [1, 4, 5, 2, [65, 2000, 21, 54], 99, 76, 54]


# Notice:
# - Shallow copy shares the nested list with the original.
# - Deep copy creates an independent nested list.