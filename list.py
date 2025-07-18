# # Get last element of a list.
# list=[1,2,3,4,5]
# print(list[-1])

# # Print elements from index 2 to 5.
# list=[1,2,3,4,5]
# print(list[2:6])

# # Check if all elements are positive.
# list=[1,2,3,-4,5]
# for i in range(len(list)):
#     if list[i]>0:
#         print(list[i])

# # Convert list to a string with commas.
# str="hi my name is Saketh"
# print(str.split())
    
# # Find the max element.
# list=[53,435,3,53,3423,53,536]
# print(max(list))

# # Find the min element.
# list=[321,41,41,5,1,412,521]
# print(min(list))

# # Sum all numbers in a list
# list=[123,124,213,1,23]
# sum=0
# for i in list:
#     sum+=i
# print(sum)

# # Square every number in a list
# list=[1,2,3,4,5,6]
# for i in list:
#     print(i*i)

# # Insert an element at index 1.
# list=[1,23,4,5,23]
# list.insert(1,"34")
# print(list)
# list.sort()
# print(list)

# # Sort list of strings by length.
# list=["abcd","defg","jagsdu","abce"]
# list.sort()
# print(list)

# # # Get common elements from two lists.
# list1=[1,312,4,21,45,214,53,32]
# list2=[12,41,45,32,21,214]
# for i in range(len(list2)):
#     if list1[i]==list2[i]:
#         print(list2[i])

# # Find second largest element.
# list=[2 ,3,421,312,21,412,12]
# list.sort()
# print(list[3])

# # Check if list contains all unique items.
# list=[23,421,4,521,232,32,2,3,4]
# list1=[]
# for i in list:
#     if i not in list1:
#         list1.append(i)
# print(list1)

# Get all prime numbers from a list.
# list=[21,312,43,2,41,4,24,5,6,3]
# list1=[]
# def prime(n):
#     not_prime=False
#     for i in range(2,n-1):
#         if n%i==0:
#             not_prime=False
#             break
#     if not_prime==True:
#         return True
# for i in list:
#     if prime(i)==True:
#         list1.append(i)
# print(list1)

# Group by even and odd
# list=[13,42,4,4,214,243,2,13,43]
# even=[]
# odd=[]
# for i in list:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even ,odd)

# Move all zeros to end of list
# list=[12,31,0,23,0,213,0,13,0]
# list1=[]
# for i in list:
#     if i!=0:
#         list1.append(i)
# for i in list:
#     if i==0:
#         list1.append(i)
# print(list1)

# # Get elements only in the first list.
# list1=[1,2,3,4,5,6]
# list2=[3,4,5,6,3,7]
# for i in list1:
#     if i in list2:
#         print(i)

# Merge and remove duplicates from two lists.
# list1=[1,2,3,4,5,6]
# list2=[3,4,5,6,7,8]
# for i in list2:
#     if i not in list1:
#         list1.append(i)
# print(list1)

# # Rotate list to the right by 2.
# list=[1,2,3,4,5,6]
# list1=[]
# for i in range(3,len(list)+1):
#    list1.append(i)
# for i in list:
#     if i not in list1:
#         list1.append(i) 
# print(list1)

# # Check if list is palindrome.
# list=[1,2,3,2,1]
# palindorm=True
# for i in range(len(list)):
#     if list[i]!=list[-1-i]:
#         palindorm=False
# if palindorm:
#     print("palindrome")
# else:
#     print("Not palindnrome")

# mat1=[[1,2],[4,5]]
# mat2=[[7,8],[3,6]]
# rows=len(mat1)
# possible=True
# if len(mat1)==len(mat2):
#     for i in range(len(mat1)):
#         if len(mat1[i])!= len(mat2[i]):
#             possible=False
#             break
# else:
#     possible=False
# if possible:
#     print("Both are same dimensions")
# else:
#     print("Both are of not same dimensions")
    
# add of two matrices
# mat1=[[1,2,3],[4,5,6]]
# mat2=[[7,8,9],[10,11,12]]
# out=[]
# if len(mat1)== len(mat2):
#     for i in range(len(mat1)):
#         row=[]
#         for j in range(len(mat1[i])):
#             sum=mat1[i][j]+mat2[i][j]
#             row.append(sum)
#         out.append(row)
#     print(out)
# else:
#     print("Addition not possible")

