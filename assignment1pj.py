#question 1
a = int(input("enter number 1:"))
b = int(input("enter number 2:"))
c = a+b
print(c)

#q2
a= int(input("Enter a number"))
if a%2 ==0:
    print("The number is even")
else:
    print("The number is odd")

#q3
def factorial(n):
    if n< 0 :
        return 0
    elif n==0 or n==1:
        return 1
    else:
        f = 1
        while(n>1):
            f *= n
            n -= 1
        return f

num = int(input("Enter the number :"))
print("factorial of",num,"is",factorial(num))

#q4
a = input("Enter Your name")
print("Hi",a,"Welcome to your laptop")

#q5
user = input("Please enter a string: ")
filename = "output.txt"
with open(filename, "w") as file:
    file.write(user)

print(f"The string has been written to {filename}")

#q6
filename = "output.txt"
with open(filename, "r") as file:
    content = file.read()

print(content)

#q7
a = input("Enter the string ")
print(len(a))

#q8
a = input("Enter the string ")
b = input("enter string number 2 :")
c = a+b
print(c)

#q9
a = input("Enter the string ")
b = input("enter substring :")
if b in a:
  print(f"The substring '{b}' is present in the main string.")
else:
    print(f"The substring {b}is not present in the main string ")

#q10
a = input("Enter a string: ")
b = a.upper()
print(b)

#q11
def generate_fibonacci(n):
    fib_sequence = [0, 1]
    
    if n == 1:
        return [0]
    
    for i in range(2, n):
        next_number = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_number)
    
    return fib_sequence

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_sequence = generate_fibonacci(n)
print(f"Fibonacci sequence (first {n} numbers): {fibonacci_sequence}")

#q12
def sum_of_digits(number):

    total_sum = 0
    
    for digit in str(number):
        total_sum += int(digit)
    
    return total_sum

number = int(input("Enter a number: "))

result = sum_of_digits(number)
print(f"The sum of the digits of {number} is: {result}")

#q13
from datetime import datetime
current_year = datetime.now().year
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year
print(f"You are {age} years old.")

#q14
lines = []
print("Enter your lines of text (enter an empty line to finish):")

while True:
    line = input()
    
    if line == "":
        break
    
    lines.append(line)

print("\nYou entered:")
for line in lines:
    print(line)

#q15
import csv
file_name = input("Enter the name of the CSV file (including .csv extension): ")

try:
    with open(file_name, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(', '.join(row))
except FileNotFoundError:
    print(f"The file {file_name} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

#q16
input_string = input("Enter a string: ")
char_frequency = {}
for char in input_string:
    char_frequency[char] = char_frequency.get(char, 0) + 1

print("Character frequencies:")
for char, frequency in char_frequency.items():
    print(f"'{char}': {frequency}")

#q17
a = input("Enter a string: ")
b = a.title()
print("String in title case:", b)

#q18
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()
if sorted(string1) == sorted(string2):
    print("The strings are anagrams of each other.")
else:
    print("The strings are not anagrams of each other.")

#q19
import string
a = input("Enter a string: ")
b = a.translate(str.maketrans('', '', string.punctuation))
print("String without punctuation:", b)

#q20
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
sum_of_numbers = 0
for num in numbers:
    sum_of_numbers += num
print("Sum of the numbers:", sum_of_numbers)

#q21
my_list = [1, 2, 3, 4, 2, 2, 3, 1, 5, 2]
element_to_count = 2
count = my_list.count(element_to_count)
print(f"The element {element_to_count} occurs {count} times in the list.")

#q22
numbers = [10, 5, 7, 3, 15, 20, 8]
minimum_value = min(numbers)
maximum_value = max(numbers)
print("Minimum value in the list:", minimum_value)
print("Maximum value in the list:", maximum_value)

#q23

temperature = float(input("Enter the temperature value: "))
unit = input("Enter the temperature unit (C for Celsius, F for Fahrenheit): ")

if unit.upper() == 'C':
    converted_temperature = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {converted_temperature}°F")
elif unit.upper() == 'F':
    converted_temperature = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {converted_temperature}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

#q24
num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero!")
        result = None
else:
    print("Invalid operator. Please enter one of the following: +, -, *, /")
    result = None

if result is not None:
    print(f"The result of {num1} {operator} {num2} is:", result)

#q25
# Source file name
source_file_name = input("Enter the name of the source text file: ")

# Destination file name
destination_file_name = input("Enter the name of the destination text file: ")

try:
    # Open the source file in read mode
    with open(source_file_name, 'r') as source_file:
        # Read the contents of the source file
        contents = source_file.read()

    # Open the destination file in write mode
    with open(destination_file_name, 'w') as destination_file:
        # Write the contents to the destination file
        destination_file.write(contents)

    print("Contents copied successfully from", source_file_name, "to", destination_file_name)

except FileNotFoundError:
    print("Error: One or both files not found.")
except IOError:
    print("Error: Unable to read/write files.")

#q26

string = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")
if string.startswith(prefix):
    print(f"The string '{string}' starts with the prefix '{prefix}'.")
else:
    print(f"The string '{string}' does not start with the prefix '{prefix}'.")

if string.endswith(suffix):
    print(f"The string '{string}' ends with the suffix '{suffix}'.")
else:
    print(f"The string '{string}' does not end with the suffix '{suffix}'.")

#q27
string = input("Enter a string: ")
characters_list = list(string)
print("List of characters:", characters_list)
