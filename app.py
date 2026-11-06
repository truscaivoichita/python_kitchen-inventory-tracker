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
    print(total_items)
check_kitchen_stock()
    # Step 3
    # Functions have their own local scope. This means variables created inside a function are like ingredients kept in that kitchen's pantry: they can only be accessed inside that specific function.

    # However, functions are not completely isolated. They can read global variables defined outside their scope. They can use those variables to perform calculations, make decisions, or create new local variables.

    # Inside your check_kitchen_stock function, replace the pass keyword with a new variable named total_items and assign it the sum of available_eggs, available_flour, and available_sugar.
