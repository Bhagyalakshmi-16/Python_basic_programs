#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Addition
num1 = float(input("Enter the first number for addition: "))
num2 = float(input("Enter the second number for addition: "))
sum_result = num1+num2
print(f"sum: {num1} + {num2} = {sum_result}")


# In[11]:


# Division
numerator= float(input("Enter the numerator for division: "))
denomenator = float(input("Enter the denomenator for division: "))
if denomenator == 0:
    print("Error: Division by zero is not allowed.")
else:
    div_result = numerator/denomenator
    print(f" Division: {numerator} / {denomenator} = {div_result}")
          


# In[13]:


# Area of triangle
base = float(input("Enter the base of triangle: "))
height = float(input("Enter the height of triangle: "))
area = 0.5 * base * height
print(f" The area of traingle is: {area}")


# In[14]:


# Swapping two variables
a=input("Enter the value of a: ")
b=input("Enter the value of b: ")
print(f" Before Swapping: a={a}, b={b}")
temp=a
a=b
b=temp
print(f" After Swapping: a={a}, b={b}")


# In[35]:


# calender
import calendar
year=int(input("Enter year: "))
month=int(input("Enter month: "))
cal=calendar.month(year, month,)
print(cal)


# In[36]:


# Check number is +ve, -ve or zero
num=int(input("Enter a number: "))
if num>0:
    print("Positive number")
elif num==0:
    print("Zero")
else: 
    print("Negative")


# In[39]:


limit=int(input("Enter the limit: "))
sum=0
for i in range(1, limit + 1):
    sum +=i
print("The sum of natural numbers upto", limit, "is:", sum)


# In[41]:


# Convesion of kilometers to miles
kilometers=int(input("Enter the distance in kilometers: "))
# Conversion factor 1km=0.621371
conversion_factor = 0.621371
miles=kilometers*conversion_factor
print(f"{kilometers} kilometers is equal to {miles} miles")


# In[43]:


# conversion celsius to fahrenheit
celsius=float(input("Enter the temperature in celsius: "))
#conversion formula fahrenhiet = (celsius * 9/5) + 32
fahrenheit = (celsius * 9/5)+32
print(f" {celsius} degress celsius is equal to {fahrenheit} degrees fahrenhet")


# In[48]:


# Check if the given number is prime or not
# Function to check if a number is prime
def is_prime(num):
    # Prime numbers are greater than 1
    if num <= 1:
        return False
    # Check for factors from 2 to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Input from the user
number = int(input("Enter a number: "))

# Check if the number is prime and display the result
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
    


# In[55]:


# Factorial of a number
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
number=int(input("Enter a number: "))
result=factorial(number)
print(f"The factorial of {number} is {result}")


# In[4]:


# Quadratic equation
import math
# input coefficients
a=float(input("Enter coefficients a: "))
b=float(input("Enter coefficients b: "))
c=float(input("Enter coefficients c: "))
# calculate the discriminant
discriminant=b**2-4*a*c
#check if the discriminant is +ve, -ve or zero
if discriminant>0:
    #Two real and distinct roots
    root1=(-b+math.sqrt(discriminant)/(2*a))
    root2=(-b-math.sqrt(discriminant)/(2*a))
    print(f" Root1: {root1}")
    print(f" Root2: {root2}")
elif discriminant==0:
    root=-b/(2*a)        #one real root (repeated)
    print(f" Root: {root}")
else:
    real_part=-b/(2*a)
    imaginary_part=math.sqrt(abs(discriminant))/(2*a)
    print(f" Root1: {real_part} + {imaginary_part}i")
    print(f" Root2: {real_part} - {imaginary_part}i")


# In[ ]:


# simple calculator with 4 basic maths operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # Take input from the user
    choice = input("Enter choice (1/2/3/4): ")
    
    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue
        
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        
        # Ask user if they want to perform another calculation
        next_calculation = input("Do you want to do another calculation? (yes/no): ")
        if next_calculation.lower() == "no":
            break
    else:
        print("Invalid input. Please enter a valid option.")


# In[ ]:


#Calculate Body mass Index
def calculate_bmi(weight, height)
# bmi formula: weight(kg)/(height**2)
     bmi=weight/(height**2)
    return bmi
def bmi_category(bmi):
    if bmi<18.5:
        return "underweight"
    elif 18.5<=bmi<24.9:
        return "normal weight"
    elif 24.9<=bmi<29.9:
        return "overweight"
    else:
        return "obese"
weight=float(input("Enter your weight in kg's: "))
height=float(input("Enter your height in mt's: "))
bmi=calculate_bmi(weight, height)
print(f" your BMI is: {bmi: .2f}")
print(f" category: {bmi_category(bmi)}")


# In[ ]:


# calculate natural logarithm of any number
import math
num=float(input("Enter a number: "))
if num<=0:
    print("please enter a positive number.")
else:
    result=math.log(num)
    print(f" The natural logarithm of {num} is: {result}")


# In[ ]:


# cube sum of first n natural numbers
def cube_of_sum(n):
    #calculate the sum of first n natural numbers
    sum_n=(n*(n-1))//2
    #calculate the cube of the sum
    cube=sum_n**3
    return cube
n=int(input("Enter the value of n: "))
result=cube_of_sum(n)
print(f"cube of sum of first {n} natural numbers is {result}")


# In[ ]:




