# This is a simple Python script that prints "Hello, World!" to the console.
print("Hello, World!")


# Taking user name as input and printing a greeting message

user_name = input("Enter your name: ")
print(f"Hello, {user_name}! Welcome to the Python world.")

"""
There are four major data types in Python:
1. String (str): Used to represent text. Strings are enclosed in single or double quotes
2. Integer (int): Used to represent whole numbers without a decimal point.
3. Float (float): Used to represent numbers with a decimal point.
4. Boolean (bool): Used to represent truth values, either True or False.
"""


name="jagadish" # expected out string
age=26 # expected out integer
is_active=True # expected out boolean
percentage=75.6 # expected out float

# printing the data types of the variables

print("Name type:", type(name))
print("Age type:", type(age))
print("Is Active type:", type(is_active))
print("Percentage type:", type(percentage)) 


"""
this is multiline comment
the below is the dummy text to examine the multiline comment
svavdh
savdhvs
asdvhjdvsahd
asdbdhsab
asvgxavjdd
xvvaV
"""

#type coversion example

# cnverting float to integer and 75.6 --> 75

new_perentage=int(percentage) # converting float to integer and 75.6 --> 75

print("New Percentage type:", type(new_perentage), new_perentage)

#coverting int to string

new_age=str(age) # converting integer to string and 26 --> "26"

print("New Age type:", type(new_age), new_age)









