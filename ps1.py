# Write a program that takes a string, string should be of even length. Divide the string into two equals parts, check the number of vowels in both the parts of the string. If both parts of string have same number of vowels then return true otherwise return false.
# str="applee"
# n=len(str)//2
# if len(str)%2==0:
#     str1=str[:n]
#     str2=str[n::]
# c1=0
# for i in str1:
#     if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#         c1+=1
# c2=0
# for i in str2:
#     if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#         c2+=1
# if c1==c2:
#     print("True")
# else:
#     print("False")

# Write a program that takes array of numbers as input, among the numbers in array, check how many numbers starts with the same digit and ends with the same digits. Print the count of such kind of numbers in the given array.
# arr=[ 34, 88, 423, 121, 2382, 10]
# c=0
# for i in arr:
#     j=str(i)
#     if j[0]==j[-1]:
#         c+=1
# print(c)

# Write a program that takes array of numbers as input, among the numbers in array, print the numbers which forms a prime number by adding one to it. Print such numbers in the given array separated b spaces.
# arr=[ 7, 4, 7, 23, 10 ]
# def prime(i):
#     k=i+1
#     c=0
#     for j in range(2,k//2+1):
#         if k%j==0:
#             c+=1
#     if c==0:
#         print(i)
# for i in arr:
#     prime(i)

# Write a program that takes array of numbers as input and a number as second input. Check the position of the factorial of the second input number in the given array. Print the position of it. If the factorial of given second input number is not presented in the array then print factorial of  the number is not presented.
# arr=[ 61, 4, 6, 7, 120 , 10 ]
# n=5
# def factorial(n):
#     if n<1:
#         return 1
#     else:
#         return n * factorial(n-1)
# a=factorial(n)
# for i in range(len(arr)):
#     if a==arr[i]:
#         print(i)

# Write a program that takes array of numbers are input, print the second duplicate number and it’s occurrence.
# arr= [ 64, 1, 2, 7, 79, 7, 7, 1, 22]
# arr1=[]
# c=0
# for i in arr:
#     if i not in arr1:
#         arr1.append(i)
#     else:
#         c+=1
#         arr1.append(i)
# print(c)




# Write a function that rotates an array to the right by a given number of steps.
# arr=[1, 2, 3, 4, 5]
# print(arr[2:]+arr[:2])

# Write a function that returns the common elements between two arrays.
# arr1= [1, 2, 3]
# arr2=[2,3,4]
# for i in arr1:
#     if i in arr2:
#         print(i)

# Write a function to find the maximum product of two elements in an array.
# arr=[3, 5, -2, 8, 11]
# arr.sort()
# print(arr[-2]*arr[-1])

# Write a function that moves all zeros in an array to the end while maintaining the order of other elements.
# arr=[0, 1, 0, 3, 12]
# arr1=[]
# for i in arr:
#     if i!=0:
#         arr1.append(i)
# for i in arr:
#     if i==0:
#         arr1.append(i)
# print(arr1)

# Write a function to find all pairs in an array whose sum is equal to a given target.
# arr=[2, 4, 3, 5, 7, 8, 9]
# sum=7
# arr1=[]
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         if arr[i]+arr[j]==sum:
#             arr1.append()

