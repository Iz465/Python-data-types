
# An empty Dictionary
Dictionary = {}
print("Empty Dictionary")
print(Dictionary)

# A dictonary with integer keys
Dictionary={1:"greek", 2:"For",3:"Geeks"}
print("\n Dictionary with the use of integer keys")
print(Dictionary)

# A dictionary with mixed keys

Dictionary={"Name": "Geeks", 1: [1,2,3,4]} # use [ when doing multiple numbers, so you can separate them with commas]
print("\n Dictionary with int and string keys (mixed)")
print(Dictionary)

# A dictionary with a dict method
Dictionary = dict({1:"Geeks",2:"For",3:"Geeks"})
print("\n A Dictionary using a dict()")

# Creating a dictionary with each item as a pair
Dictionary = dict([(1,"geeks"),(2,"for")])
print("\n A Dictionary with each item as a pair")
print(Dictionary)