my_dictionary = {}
my_dictionary['name'] = input("Enter your name: ")
my_dictionary['age'] = int(input("Enter your age: "))
my_dictionary['city'] = input("Enter your city: ")
my_dictionary['salary'] = float(input("Enter your salary: "))
print("\n1) Dictionary Elements:")
print(my_dictionary)
print("\n2) Accessing Dictionary Elements:")
print("Name:", my_dictionary['name'])
print("Age:", my_dictionary['age'])
print("City:", my_dictionary['city'])
print("Salary:", my_dictionary['salary'])
print("\n3) Changing Values of the Dictionary:")
my_dictionary['age'] = int(input("Enter a new age: "))
my_dictionary['salary'] = float(input("Enter a new salary: "))
print("Updated Dictionary:", my_dictionary)
print("\n4) Length of the Dictionary:", len(my_dictionary))