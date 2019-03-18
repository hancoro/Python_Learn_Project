

# Dictionary uses key value pairs
example_dictionary = {
    "key1": "This is the paired value for key1",
    "key2": "This is the paired value for key2",
    "key3": "This is the paired value for key3",
    "key4": "This is the paired value for key4",
    76: "keys can be other data types"
}


# How to access dictionary entries

print(example_dictionary["key2"])  # use the key
print(example_dictionary.get("key4"))  # use .get and the key
print(example_dictionary.get("non existent key", "This is a default return where not key exists in the dictionary"))
print(example_dictionary.get(76))  # This uses a number as the key rather than a string

