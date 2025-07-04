# # Print numbers from 1 to 10 using a for loop.
# for i in range(1,11,1):
#     print(i)

# ⁠Print numbers from 10 to 1 in reverse order using a for loop.
# # for i in range(10,0,-1):
# #     print(i)

# Print all even numbers from 1 to 20.
# # for i in range(0,21,2):
# #     print(i)

# Print all odd numbers from 1 to 15.
# for i in range(1,16,2):
# #     print(i)

# ⁠ ⁠Print the square of numbers from 1 to 10.
# # for i in range(1,11,1):
# #     print(i*i)

# # Print the cube of numbers from 1 to 5.
# for i in range(1,6):
#     print(i*i*i)

# ⁠Print the multiplication table of 5 (from 5×1 to 5×10).
# num=5
# for i in range(1,11):
#     print(f"{num}x{i}={num*1}")






# # *       *
# # *       *
# # * * * * *
# # *       *
# # *       *

# row=5
# for i in range(row):
#     pattern=""
#     for j in range(row):
#         if j==0 or j==row-1 or i==(row//2):
#             pattern+="*"+" "
#         else:
#             pattern+=" "+" "
#     print(pattern)
    
# #  * * * * *
# #      *
# #      *
# #      *
# #      *

# row=5
# for i in range(row):
#     pattern=""
#     for j in range(row):
#         if i==0 or  j==(row//2):
#             pattern+="*"+" "
#         else:
#             pattern+=" "+" "
#     print(pattern)

# # *       *
# # * *     *
# # *   *   *
# # *     * *
# # *       *

# row=5
# for i in range(row):
#     pattern=""
#     for j in range(row):
#         if j==0 or j==row-1 or i==j:
#             pattern+="*"+" "
#         else:
#             pattern+=" "+" "
#     print(pattern)

# * * * * *
#       *
#     * 
#   *   
# * * * * * * 

# row=5
# for i in range(row):
#     pattern=""
#     for j in range(row):
#         if i==0 or i==row-1 or i+j==row-1:
#             pattern+="*"+" "
#         else:
#             pattern+=" "+" "
#     print(pattern)

