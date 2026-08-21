print("Welcome to the Interactive Personal Data Collector!")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favourite_number = int(input("Please enter your favourite number: "))
print("Thank you! Here is the information we collected:")
# Displaying information
print("Name:", name)
print("Type:", type(name))
print("Memory Address:", id(name))

print("Age:", age)
print("Type:", type(age))
print("Memory Address:", id(age))

print("Height:", height)
print("Type:", type(height))
print("Memory Address:", id(height))

print("Favourite Number:", favourite_number)
print("Type:", type(favourite_number))
print("Memory Address:", id(favourite_number))

# Birth year calculation
birth_year = 2026 - age
print("Your approximate birth year is:", birth_year)
print("Keep learning Python. Goodbye!")