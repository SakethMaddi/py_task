# # Write a function to add two numbers
# def add(a,b):
#     sum=a+b
#     return sum
# print(add(3,4))

# # Write a function to return the square of a number
# def square(n):
#     square=n*n
#     return square
# print(square(3))

# # Write a function to find the factorial of a number
# def factorial(n):
#     fact=1
#     for i in range(1,n,1):
#         fact=fact*i
#     return fact
# print(factorial(6))

# # Write a function to find the greatest of two numbers
# def greatest(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# print(greatest(9,3))

# # Write a function that returns whether a number is even or odd
# def odd_even(n):
#     if n%2==0:
#         return 1
#     else:
#         return 0
# print(odd_even(23))

# # Write a function to check if a number is prime
# def prime(n):
#     for i in range(2,n+1,1):
#         if n%i==0:
#             return False
#     return True
# print(prime(23))

# # Write a function to return the sum of first n natural numbers
# def sum(n):
#     sum=0 
#     for i  in range(n+1):
#         sum=sum+i
#     return sum
# print(sum(6))

# # Write a function to return maximum of three numbers
# def max_num(a,b,c):
#     if a>b and a>c:
#         print("a")
#     elif b>a and b>c:
#         print("b")
#     else:
#         print("c")
# max_num(2,3,34)

# # Write a function to reverse a number.
# def reverse_num(n):
#     rev=0
#     while n>0:
#         rev=(rev*10)+(n%10)
#         n//=10
#     return rev
# print(reverse_num(1342))

# # Write a function to count digits in a number.
# def count_digits(n):
#     count=0
#     while n!=0:
#         count+=1
#         n//=10
#     print(count)
# count_digits(123452)

# # Write a function to convert Celsius to Fahrenheit.
# def c_to_f(f):
#     c=0
#     c=5/9*(f-32)
#     return c
# print(c_to_f(35))


# # Write a function to find power of a number (base, exponent)

    
    
# # Write a function to check if a year is a leap year
# def leap_year(n):
#     if n%4==0 or n%100==0:
#         return True
#     return False
# print(leap_year(2005))

# # Write a function to check whether a number is palindrome.
# def palindrome(n):
#     temp=0
#     rev=0
#     n == temp
#     while temp>0:
#         rev=(rev*10)+(temp%10)
#         temp//=10
#     if rev == n :
#         print("palindrome")
#     else:
#         print("not palindrome")
# rev= palindrome(121)

# # Write a function to calculate simple interest.
# def Simple_interst(p,t,r):
#     si=0
#     si=(p*t*r)/100
#     return si
# print(Simple_interst(2000,24,5))

# # Write a function that accepts a number and returns its absolute value.
# def absolute_num(n):
#     if n>=0:
#         return n
#     else:
#         return -n
# print(absolute_num(-3122234))   

# # Write a function to return the area of a circle.
# def area(r):
#     area=0
#     area= 3.14*(r*r)
#     return area
# print(area(4))

# # Write a function to convert minutes to hours and minutes.
# def time(n):
#     hours=0
#     minutes=0
#     hours=n//60
#     minutes=n%60
#     print(hours,"hours",minutes,"minutes")
# time(90)

# # Write a function to calculate compound interest.
# def compound_intrest(p,r,n,t):    
#     ci=p*(1 + r/n)**(n*t)
#     return ci
# print(compound_intrest(p=10000,n=3,r=4,t=18))

# # Write a function to return all factors of a number
# def factorial(n):
#     for i in range(1,n+1,1):
#         if i%n==0:
#             print(i)           
# factorial(10)

# # Write a function to print multiplication table of a number.
# def mul_table(n):
#     for i in range(1,11):
#         print(n,"*",i,"=",(n*i))
# mul_table(5)

# # Write a function that takes name and age and prints a message.
# def message(name,age):
#     print(" Hi my name is ",name,"and my age is ",age)
# message("saketh",21)

# # Write a function to calculate BMI and return category
# def bmi(weight,height):
#     bmi=0
#     bmi=weight // (height**2)
#     return bmi
# print(bmi(weight=48,height=1.5))

# Write a function to convert decimal to binary



# # Write a function to return the nth Fibonacci number.
# def fibo(n):
#     li=[0,1]
#     for i in range(2,n):
#         z=li[i-1]+li[i-2]
#         li.append(z)
#     return li[-1]
# print(fibo(8))

# # Write a function that returns whether a number is Armstrong or no
# def armstrong(n):
#     c=count(n)
#     num1=0
#     temp=n
#     while n!=0:
#         num1 = (n%10)**c + num1
#         n=n//10
#     if num1 == temp:
#         return True
#     else:
#         return False    
# def count(n):
#     count=0
#     while n!=0:
#         count+=1
#         n=n//10
#     return count
# print(armstrong(153))

# # Write a function that returns True if a number is perfect.
# def perfect_num(n):
#     divsors_sum=0
#     if n<=0:
#         return False
#     for i in range(1,n):
#         if n%i==0:
#             divsors_sum+=i
#     if divsors_sum == n :
#         return True
#     else:
#         return False
# print(perfect_num(28))    

# # Write a function to return max digit in a number.
# def max_digit(n):
#     max=0
#     while n!=0:
#         rem=n%10
#         if max < rem:
#             max=rem
#         n=n//10
#     return max
# print(max_digit(4172))

# # Write a function to return number of digits in an integer.
# def no_of_digits(n):
#     count=0
#     while n!=0:
#         count+=1
#         n//=10
#     return count
# print(no_of_digits(123412))

# 
# def upper_lower_count(str):
#     upper_count=0
#     lower_count=0
#     for i in range(len(str)):
#         c=str[i]
#         if c==c.upper() and c!=" ":
#             upper_count+=1
#         else:
#             lower_count+=1
#     print(lower_count)
#     print(upper_count)

# upper_lower_count("i Am leaning PythON")

# # Write a function to return max digit in a number.
# def max_digit(n):
#     max=0
#     while n>0:
#         digit=n%10
#         if digit > max:
#             max=n%10
#         n//=10
#     return max
# print(max_digit(3425))