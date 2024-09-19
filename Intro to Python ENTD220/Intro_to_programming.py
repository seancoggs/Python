"""
Introduction to programming
What is programming?
Programming is a set of rules/instrunctions to be applied to any task

To understand programming, you need to learn the following:-
1) what are comments
2) How to print
3) How to store data (creating variables)
4) How to branch (creating if-then)
5) How to repeat commands (looping)

go to www.pythontutor.com to practice

"""

"""
1) Comments are comments/notes you write for you or others.
   Comments are not part of the code. It can be instructions
   or form of help.

   Python has two type comments:-
   1) Comment Block like this one; it starts and ends with triple double quotations
      or triple single quotations. Any text between the triple quotations is not 
      part of the code.

   2) Line comment; putting '#' pound sign infront of any code will make it a comment
      and it will not execute.
         
"""

"""
2) print() function is used to display/print a message to the user.
"""
# Printing a message
print("Hello Folks, I am learning programming")
print('Hello World!')
print("Hello World")
print('\nHello students and Python')  # \n = new line

# the following two lines will print on one line
print("My Name is prof Ymmas Azaba ", end="")
print("and I will be your instructor for this course ")
print("\nThis line is printing with an empty line before it ")


"""
3) Varaibles, a variable is a name of stored data.
You can store string (characters), numeric or other data type in
a varable. You can store another variable in a variable too. 

Variables; must contain only letters, underscores, and numbers.
They must start with a letter or underscore.

Variable names should be short, descriptive and related to the task
"""

# storing string in a variable
my_name="Bond"                # name in double quotations
my_full_name='James Bond'     # name in single quotations is ok too
my_age=35                     # note for numbers, there are no quotations
my_age_next_year=my_age+1     # store my_age+1 to my_age_next_year

# --- printing the content of the variables
print(my_name)                # this will print Bond

# --- print multiple variables. (separated by ,)
print(my_name, my_full_name, my_age, my_age_next_year)

# --- adding a label to the variable
print("May name is",my_name)

# --- you can do this too
print(f"May name is, {my_name}")

# --- another way
print("May name is, {}".format(my_name))

# --- combine two variables
print("May name is, {} and I am {} years old".format(my_name, my_age))

# let's do some math
# print("doing math")
a = 8
b = 2
print ('Addition:\t' , a , '+', b , '=' , a + b) 
print ('Subtraction:\t' , a , '-', b , '=' , a - b) 
print ('Multiplication:\t' , a , 'x', b , '=' , a * b) 
print ('Division:\t' , a , '/', b , '=' , a / b) 
print ('Floor Division:\t' , a , '//', b , '=' , a // b) 
print ('Modulus:\t' , a , '%', b , '=' , a % b)




"""
4) Branching or if-then-else. If-then-else of If-else in Python is a 
structure/statement allows you to go to another code based on a condition

the if statement checks/tests the expression for true or false before 
executing the statment.

valid comparison operators
> greater than, < less than, == equal, != not equal, >= greater than or equal,
<= less that or equal
"""

# simple if
car_budget=10000
car_price=500

if (car_price > car_budget):
   print("That is too much")

# let us create a simple application from the above
# input() is Ptyhon function that will take the 
# user input as string
car_info=input("Enter car name and year ")

# float() function will convert numbers entered
# as string to numbers. You need this conversion to
# be able to do any calculations on these numbers
car_budget=float(input("Enter car buget "))
car_price=float(input("Enter car price "))

if (car_price > car_budget):
   print("The car", car_info, "is over budget, please select another car")
else:
   print("The car", car_info, "is suitable, let's test drive it")   


"""
5) Looping is structure of the code runs multiple times.
In Python there are two main types of loops
 1) while loop
 2) for loop
"""

# while loop run as long as the condition is true
num = 1
while num < 7:
   print(num)
   num = num + 1  # increase num by 1, or add 1 to num and add it back to num
                  # if you do not change the value, the loop will run forever
                  # and may crash your computer.
print("Done printing\n")
# using break to get out the loop
num = 1
while True:       # run forever
   print(num)
   num = num + 1
   if num >=5:
      break
   else:
      continue
print("That's all folks")

# let's modify the car example using while loop
print("\nPrice check\n")
while True:
   car_info=input("Enter car name and year ")
   car_budget=float(input("Enter car buget "))
   car_price=float(input("Enter car price "))

   if (car_price > car_budget):
      print("The car", car_info, "is over budget, please select another car")
      continue
   else:
      print("The car", car_info, "is suitable, let's test drive it") 
      break

# A for loop is used for iterating over a sequence 
# that is either a list, a tuple, a dictionary, a set, or a string

# Let is loop in this string
my_full_name='My name is Bond, James Bond'
for l in my_full_name:
   print(l, end="")





