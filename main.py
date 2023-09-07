# # Week  
# # This week we will work on :
# # Working With Strings

# # 1.   Working With Numbers
# # 2.   Getting Input From Users
# # 3.   mathematical operations
# # 4.   Getting Input From Users
# # 5.   string formatting
# # 6.   data type conversions

# # 1.   Building a Basic Calculator
# # 2.   Mad Libs Game





# # Review
# create variables for the following :
# 1. age
age1="16"
# 2. name
name1="Valeria"
# 3. song
song="Bullet Hell"
# 4. food
food="rice"
# 5. number
num="729"

# #now include the variables you just made print in the following...

# Once upon a time, there was a [age] old coder named [name]. 
print(f"Once upon a time, there was a {age1} year old coder named {name1}")

# [name] liked to hum the song [song] while coding. It was so annoying that their teammates would throw [food] until [name] would stop singing.
print(f"{name1} liked to hum the song {song} while cooding. It was so annoying that their teammates would throw {food} until {name1} would stop singing.")

# Still, [name] was the best coder on the team and could write [number] lines of code every day. Maybe [song] was [name]’s secret power?
print(f"Still, {name1} was the best coder on the team and could write {num} lines of code every day. Maybe {song} was {name1}'s secret power?")

##########################################################################################









##########################################################################################
# The names you use when creating these labels need to follow a few rules:
# 1. Names can not start with a number.
# 2. There can be no spaces in the name, use _ instead.
# 3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
# 4. It's considered best practice (PEP8) that names are lowercase.
# 5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), 
#    or 'I' (uppercase letter eye) as single character variable names.
# 6. Avoid using words that have special meaning in Python like "list" and "str"

# Here are some exercises to practice the rules:

# Correcting Invalid Names: Below are some invalid names. Correct them according to the rules:

# 1st_name --> name_1st
# last name --> last_name
# email@address --> email_address
# percent% --> percent
# variable#name --> varible_name
# O --> zero
# list --> list1

# Creating Valid Names: Create valid names for the following descriptions:

# The first name of a person --> first_name
# The last name of a person --> last_name
# The email address of a person --> emaial_adress
# The percentage of marks obtained by a student --> percentage
# A variable to store the number of items in a shopping cart --> cart_items


# Identify Valid and Invalid Names: Identify which of the following names are valid or invalid according to the rules:

# first_name --> valid
# lastName --> valid
# email_address --> valid
# percentage --> valid
# variable_name --> valid
# 1_variable --> invalid
# email@address --> invalid
# percentage% --> invalid
# i --> valid




# Declare two variables, called name and age.
# Set the name variable value to "Tony Soprano" and the age value to 51.
name="Tony Soprano"
age="51"

# Variables Practice #2
# Create three variables:
# first_name
first_name="Julia"
# last_name
last_name="Roberts"
# full_name
full_name="Julia Roberts"
# Assign the value "Julia" to first_name, and for last_name, assign the value "Roberts". Finally, build the variable full_name by concatenating these two variables (remember to add a space in between)


# Variables Practice #3
# Declare the variable course, assign it the value "Python", and print the following sentence:
course="Python"
# You are taking a course course
print(f"You are taking a {course} course.")
# To do this, you must concatenate the first and last parts of the sentence with the variable. Remember to add spaces before and after concatenating the variable to the rest of the text.



################ # **Working with** **numbers** **bold text**######### dont work yet

# We'll learn about the following topics:
# 1. Types of Numbers in Python
# 2. Basic Arithmetic
# 3. Differences between classic division and floor division

# Python has various "types" of numbers (numeric literals). 
# 1. We'll mainly focus on integers and floating point numbers.
# Integers are just whole numbers, positive or negative. For example: 2 and -2 are examples of integers.
# 2. Floating point numbers in Python are notable because they have a decimal point in them, or use an exponential (e) to define the number. For example 2.0 and -2.1 are examples of floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of a floating point number in Python.

# slides 10 -12
int_num=5.7
print(type(int_num))
#type() identifies the type of data of type
name2="Tony"
print(type(name2))
classInSession= True
print(type(classInSession))

#floating point numbers
dollars = 50.25
price_of_book= 39.99
print(dollars)
total= dollars + price_of_book
print(total)
print(type(total))
print(dollars + price_of_book)

money_for_movie= float(input("How much money do you have for the movie? "))
money_for_dinner= float(input("How much money do you have for dinner? "))
total_cost= money_for_dinner + money_for_movie
print(f'You have ${total_cost} for the movie and dinner') 



# Integers Practice
# Declare a numeric variable named int_num that contains a value of integer type of your choice.
int_num1=11036
# Print the data type of that variable.
print(type(int_num1))

# Floats Practice
# Declare a numeric variable named decimal_num that contains a value of float type of your choice.
decimal_num=81943.82 #implicit is inferred by the program
decimal_num= float(81943.82) #explicit is that its explicityly stated
#Python allows for implicit or explicit conversion

# Print the data type of that variable.
print(type(decimal_num))

# ata Types Practice
# What type is the result of the sum of 7.5 + 2.5? Write the code to verify it.
num12=7.5
num13=2.5
# To do this, create two variables:
# num1 = 7.5
# num2 = 2.5
# Next, print on the screen the data type that results from the sum of both numbers.

#################################Data Type conversions####################
# slides 12 -19
# Data Type Conversions Practice #1
# Convert the value of num1 to an integer and print the resulting data type.
num1= 20
#   Data Type Conversions Practice #2
# Convert the value of num2 to a float and print the resulting data type.

#   Data Type Conversions Practice #3
# Add the values of num1 and num2.
# Do not modify the value of variables already declared, but apply the necessary conversions within the print() function.

#################################formatting strings####################
# slide 19 -22


# Strings Formatting Practice #1
# We need to print the associate name and number within the following sentence:
# "Dear (associate_name), your associate number is: (associate_number)"
# Remember that the precision of your answer (spaces, spelling and punctuation) is very important to arrive at the correct result.


# associate_name = "Jesse Pinkman"
# associate_number = 399058

# Dear (associate_name), your associate number is: (associate_number)

# Strings Formatting Practice #2
# Tell the user the amount of points earned within the following phrase:
# "You have earned (new_points) points! In total, you have accumulated (total_points) points"
# Remember that the precision of your answer (spaces, spelling and punctuation) is very important to arrive at the correct result


# Strings Formatting Practice #3
# Tell the user the amount of points earned within the following phrase:
# "You have earned (new_points) points! In total, you have accumulated (total_points) points"
# This time, the amount of points accumulated (total_points) will be equal to the previous_points plus the new_points.
# Remember that the precision of your answer (spaces, spelling and punctuation) is very important to arrive at the correct result.

# previous_points = 875
# new_points = 350

#################################Mathematical operations####################
# slides 20 -24
# #addition
# #multiplication
# #division
# #modulo
# #powers
# #get the max and min of a number
# #round a number
# # absolute value
# # order of operations
# #to do more you need to import special math libraries from python
# #from math import *     
# #this goes out and grabs some different math functions we can use
# #floor method
# #ceil method
# #sqrt method

# Here are some practice problems for students based on the operations :

# ### Addition
# 1. Add the numbers 145 and 256.
# 2. What is the sum of 873 and 1,287?

# ### Multiplication
# 3. Multiply 13 by 24.
# 4. What is the product of 17 and 19?

# ### Division
# 5. Divide 528 by 6.
# 6. What is the result when 1,234 is divided by 4?

# ### Modulo
# 7. What is the remainder when 200 is divided by 7?
# 8. If \( x = 145 \) modulo 12, find the value of \( x \).

# ### Powers
# 9. Calculate \( 7^3 \).
# 10. Find the value of \( 5^4 \).

# ### Get the max and min of a number
# 11. Which is greater: 345 or 453?
# 12. Out of 1,002 and 1,020, which is the lesser number?

# ### Round a number
# 13. Round 17.56 to the nearest whole number.
# 14. Round 123.789 to the nearest tenth.

# ### Absolute Value
# 15. Find the absolute value of -134.
# 16. What is the absolute value of -15.7?

# ### Order of Operations
# 17. Evaluate the expression: \( 5 + 3 \times 4 - 2^2 \).
# 18. Calculate \( 12 \div 4 + 7 - 2 \times 3 \).

# ### Special Math Libraries
# **Floor Method**
# 19. Round down the number 17.89 to the nearest whole number.
# 20. What is the floor value of 45.01?

# **Ceil Method**
# 21. Round up the number 23.01 to the nearest whole number.
# 22. What is the ceiling value of 67.67?

# **Sqrt Method**
# 23. Find the square root of 144.
# 24. Calculate the square root of 169.

# Note: For the problems involving floor, ceil, and sqrt, students will need to use the `math` library functions in Python.


# Print on the screen the floor division of the following two numbers: 874 divided by 27



# Print on the screen the modulus of 456 divided by 33



# Calculate and print the square root of 783






##########################################################################################
# So what have we learned? We learned some of the basics of numbers in Python. We also learned how to do arithmetic and use Python as a basic calculator. We then wrapped it up with learning about Variable Assignment in Python.
# # **Getting Input from users**
# #how do we get input from users?
# input("what is your name?")
# # basic math calculator
# #ask the user for 2 numbers
# # print out a statement where you:
# # add them together
# #multiply
# # find the max number
# # find the remainder of the numbers
# #round one number








######### on to the last slide for your challenge-- work on this with another person .

# 1) create a new repl for the challenge
# 2) name it challenge week 3
# 3) invite the other person to your repl.
# 4) you now have a mind partner in collaborating on solving this challenge





