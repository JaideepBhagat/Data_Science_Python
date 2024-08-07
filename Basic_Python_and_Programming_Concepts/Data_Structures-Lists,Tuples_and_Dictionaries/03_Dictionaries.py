# Creating an address book
address_book = {
    "Jaideep Bhagat": "Kharghar, Navi Mumbai, India",
    "Swati Bhagat": "Ravet, Pune, India",
    "Suresh Bhagat": "Roha, Raigad, India",
}

# Printing the address book
print(address_book)

# Accessing individual values
print(address_book["Jaideep Bhagat"])

# Changing values
address_book["Swati Bhagat"] = "Ravet, Pune, Maharashtra, India"

# Adding a new entry
address_book["Aaryan Bhagat"] = "Roha, Raigad, India"

# Printing the address book
print(address_book)

# Looping through all the entries
for name, address in address_book.items():
    print(f"{name} lives at {address}")

# Length of the address book
print(len(address_book))

# Sorting the address book
sorted_address_book = sorted(address_book.items())
print(sorted_address_book)

# Reversing the address book
reversed_address_book = sorted(address_book.items(), reverse=True)
print(reversed_address_book)

# Clearing the address book
address_book.clear()
print(address_book)

# Deleting the address book
del address_book
print(address_book)
