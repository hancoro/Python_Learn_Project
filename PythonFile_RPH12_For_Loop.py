
# for anything in something do something
# for example in a string
for rph_letter in "Robin is Awesome":
    print(rph_letter)

# for example list 1

# create a list
friends = ["Rita", "Sue", "Bob"]
for friend in friends:
    print(friend)


# for example in a in array

# create an empty list
rph_list = []

# populate list by adding each letter in a string
for string_letter in "Each letter of this string will be added to the list":
    rph_list.append(string_letter)

# read out each entry in list
for list_entry in rph_list:
    print(list_entry)

# read out range from a set random number
for index in range(14):
    print(index)

# read out a range from the list
for rph_index in range(len(rph_list) - 5):
    print(rph_list[rph_index])

# read out range from a set random number
for index in range(14):
    print(index)

# read out range from range within a random number
# this will read fro 5 to 16
for index2 in range(5, 17):
    print(index2)
