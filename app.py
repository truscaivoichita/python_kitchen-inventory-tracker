# Step 1
# Welcome to the kitchen! Just like a chef relies on recipes to prepare a meal, you will rely on functions to build software. In this workshop, you'll learn how to write reusable Python functions and master scope, understanding exactly which ingredients (variables) are available in your code at any given time.

# To get started, you should define some basic data for your kitchen inventory. Create three variables: available_eggs, available_flour, and available_sugar, and assign them the values 1, 2, and 3, respectively.
available_eggs = 1
available_flour = 2
available_sugar = 3

# Step 2
# Time to create a function to check what you have in your kitchen. In Python, you define functions using the def keyword, followed by the function name, parentheses (), and a colon :.

# Here is an example of how to define a simple function:

# Example Code
# def my_function():
    # pass
# Define an empty function named check_kitchen_stock. Use the pass keyword inside the function body for now so that Python does not raise a SyntaxError.

# Remember that Python relies on indentation to define code blocks. So make sure to indent the function body.
def check_kitchen_stock():
    total_items = available_eggs + available_flour + available_sugar
    print(f'The kitchen has {total_items} total items:')
    print(f'- {available_eggs} eggs')
    print(f'- {available_flour} flour')
    print(f'- {available_sugar} sugar')
check_kitchen_stock()
    # Step 3
    # Functions have their own local scope. This means variables created inside a function are like ingredients kept in that kitchen's pantry: they can only be accessed inside that specific function.

    # However, functions are not completely isolated. They can read global variables defined outside their scope. They can use those variables to perform calculations, make decisions, or create new local variables.

    # Inside your check_kitchen_stock function, replace the pass keyword with a new variable named total_items and assign it the sum of available_eggs, available_flour, and available_sugar.

# Step 4
# Now that you have calculated your total, you should display the inventory. Recall from prior lessons that you can use the print() function with f-strings to include variables in your output.

# Inside your check_kitchen_stock function, below your total_items variable, add these exact four print statements:

# print(f'The kitchen has {total_items} total items:')
# print(f'- {available_eggs} eggs')
# print(f'- {available_flour} flour')
# print(f'- {available_sugar} sugar')

# Step 5
# Python reads the def block and remembers the function, but it does not run the code inside it immediately.

# To execute the code and see your output, you need to call (or invoke) the function. Do this by typing the function's name followed by parentheses.

# For example:

# Example Code
# my_function()
# At the bottom of your code, outside of the function, call your check_kitchen_stock function.

# Step 6
# Now that you know what's in your kitchen, you can use those items to cook. To do this, create a new function that accepts parameters. Think of parameters as placeholders for the data you pass into the function when calling it.

# Here is a function that accepts two parameters, a and b, and prints their sum to the terminal.

# Example Code
# def calculate_sum(a, b):
    # print(a + b)

# calculate_sum(3, 1) # Output: 4
# Below your check_kitchen_stock function, define an empty function named use_eggs that accepts two parameters: available_eggs and eggs_to_use, in that order.

# Note that if you give a parameter the exact same name as a global variable (like available_eggs), the function will use its own local parameter available_eggs instead of the global one. This is known as name shadowing since the local variable "shadows" the global one.

# Use the pass keyword inside the body for now.
def use_eggs(available_eggs, eggs_to_use):
    if eggs_to_use > available_eggs:
            print("The kitchen does not have enough eggs.")
            return available_eggs
    print(f'{eggs_to_use} egg(s) used out of {available_eggs} available.')
    return available_eggs - eggs_to_use
print(use_eggs(6, 5))
    # Step 7
    # Inside your use_eggs function, you need to check if you have enough eggs to cook with. You can do this using an if statement.

    # Replace the pass keyword with an if statement that checks if eggs_to_use is greater than (>) available_eggs. Inside the if block, print the string The kitchen does not have enough eggs..

# Step 8
# If you don't have enough eggs, you shouldn't try to cook! You need a way to stop the function from running any further.

# You can use the return keyword for this. When a function hits a return statement, it stops executing immediately and passes the returned value back to where it was called.

# For example:

# Example Code
# def cook_dish():
    # message = "The dish is ready to serve!"
    # return message
    # print("This line will never run.")

# print(cook_dish())  # Output: The dish is ready to serve!
# Inside your if block, below the print statement, use the return keyword to return the value of available_eggs.

# Step 9
# If the if condition evaluates to False (meaning you do have enough eggs), the function will skip the if block and continue running the rest of the code.

# Now you need to process your data and return a new computed value.

# Outside of your if block (at the same indentation level as the if keyword), use a print() call and an f-string to print f'{eggs_to_use} egg(s) used out of {available_eggs} available.'.

# Then, on the next line, return the remaining number of eggs by subtracting eggs_to_use from available_eggs.
