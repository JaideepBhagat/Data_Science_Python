try:
    person = {"Name": "Jaideep", "age": 43, "email": "jaideep.bhagat@outlook.com"}
    print(person["phone"])
except KeyError:
    print("Error: No data was found for the key specified")
