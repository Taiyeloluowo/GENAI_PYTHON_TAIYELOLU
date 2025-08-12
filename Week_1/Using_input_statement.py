# Step 1 I created a variable named "name" to collect input which will be displayed to the customer
# Step 2 I created another variable named "age" to collect the age of the customer
# Step 3 I created a third variable to collect the order of the customer



name = input("Enter your name: ")
print("Hello,", name)

age = int(input("Enter your age: "))
print(f"You will be {age + 1} years old next year.")

order = input("Welcome, What would you like to order: ")
print("Here is your order,", order)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}.")

