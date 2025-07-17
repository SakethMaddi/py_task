# n1=15
# n2=20
# big=0
# small=0
# if n1>n2:
#     big=n1
#     small=n2
# else:
#     big=n2
#     small=n1
# if big % small ==0:
#     print(big,"is the LCM")
# else:
#     lcm_not_found=True
#     temp_lcm=big+big
#     while lcm_not_found==True:
#         if temp_lcm % n1==0 and temp_lcm%n2==0:
#             print(temp_lcm,"is the lcm")
#             break
#         else:
#             temp_lcm+=big

# # # prime number
# def prime_number(n):
#     factors=0
#     for i in range(2,n):
#         if n%i ==0:
#             factors+=1
#             break
#     if factors==0:
#         print("Prime Number")
#     else:
#         print("Not Prime Number")
# prime_number(59)

# # # next prime number
# def next_prime(n):
#     prime_not_found=True
#     while prime_not_found==True:
#         n+=1
#         factors=0
#         for i in range(2,n):
#             if n%i ==0:
#                 factors+=1
#                 break
#         if factors==0:
#             # print(n,"is next prime num")
#             next_num=n
#             prime_not_found=False
#     return next_num

# # previous prime number
# def pre_prime(n):
#     for i in range(n-1,1,-1):
#         factors=0
#         for j in range(2,i):
#             if i%j==0:
#                 factors+=1
#                 break
#         if factors==0:
#             # print(i,"is previous prime ")
#             pre_num=i
#             break
#     return pre_num
# n=59
# if (n-pre_prime(n))<(next_prime(n)-n):
#     print(pre_prime(n),"is nearst prime")
# elif (next_prime(n)-n)<(n-pre_prime(n)):
#     print(next_prime(n),"is nearst prime")
# else:
#     print("Both are at equal range")
    
    
    
# # anagram
# def anagram(str1,str2):
#     if len(str1)!= len(str2):
#         print("Not anagrams")
#     else:
#         is_anagram=True
#         for i in str1:
#             if str1.count(i) != str2.count(i):
#                 is_anagram=False
#                 break
#         if is_anagram==True:
#             print(str1,str2,"are anagrams")
#         else:
#             print(str1,str2,"are not anagrams")          
# anagram("listen","silent")

# # Count number of palindromic substrings in a string
# def palindrome(str):
#     count=0
#     for i in range(len(str)):
#         temp=""
#         for j in range(i,len(str)):
#             temp+=str[j]
#             if temp==temp[::-1] and len(temp)>=3:
#                 count+=1
#     print(count)
# palindrome("malayalam")

# # And find smallest palindromic substring
# def palindrome(str):
#     count=0
#     smallest=str
#     for i in range(len(str)):
#         temp=""
#         for j in range(i,len(str)):
#             temp+=str[j]
#             if temp==temp[::-1] and len(temp)<=len(smallest) and len(temp)>=3:
#                 smallest=temp              
#     print(smallest)
# palindrome("malayalam")

# positional prime number
# def prime():
#     pos=7
#     num=2 
#     count=0
#     prime=0
#     while count<pos:
#         factors=0
#         for i in range(2,num):
#             if num%i==0:
#                 factors+=1
#                 break
#             if factors==0:
#                 count+=1
#                 prime=num
#             num+=1  
#     print(f"{prime} is the {count} prime number")
# prime()

# chars=["A",1,"B",2,"a","z"]
# uc=[]
# lc=[]
# sum=0
# for i in chars:
#     a=str(i)
#     b=ord(a)
#     if b>=65 and b<=90:
#         uc.append(a)
#     elif b>=97 and b<123:
#         lc.append(a)
#     else:
#         sum+=int(a)
# u="".join(uc)
# l="".join(lc)
# print(f"{u} ,{l} ,{sum}")