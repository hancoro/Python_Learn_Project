# The following are basic list functions

my_list = ["first_entry", "second_entry", "third_entry", "forth_entry", "fifth_entry", "sixth_entry"]
print(my_list)  # reads full list
print(my_list[1])  # reads list entry by index
print(my_list[-1])  # use negative index reads the list in reverse
print(my_list[1:])  # Use colon to read list after specified index
print(my_list[1:3])  # colon can be used to select a range from the list

# List entries can be modified
my_list[2] = "third_entry_modified"
print(my_list)  # read list following modification


# The following are further list functions
my_num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_string_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(my_string_list)

my_string_list.append("addition_to_string")  # This is how to add to a list
print(my_string_list)

my_string_list.insert(3, "insertion_to_string")  # This is how to insert into to a list
print(my_string_list)

my_string_list.sort() # This sorts the list
print(my_string_list)

my_string_list.extend(my_num_list)  # add lists together
print(my_string_list)

my_string_list.remove("insertion_to_string")  # This is how to remove from a list
print(my_string_list)

my_string_list.pop()  # This removes the last list entry from the list
print(my_string_list)

list_count = my_string_list.count("b")  # This counts the number or list entries = to 'b'
print(list_count)

my_string_list.reverse()  # This reverses the list
print(my_string_list)

my_copied_list = my_string_list.copy()
print("Copied list = " + str(my_copied_list))

my_string_list.clear()  # This is how to clear a list
print(my_string_list)
