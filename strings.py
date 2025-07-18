# # Print the position of the vowels 
# name=input()
# for i in range(len(name)):
#     c= name[i]
#     if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
#         print("Position of vowel: ",i)
        
# # Count the no.of consonets
# name= input()
# count=0
# vowel=0
# for i in range(len(name)):
#     c= name[i]
#     if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
#         vowel+=1
#     else:
#         count+=1   
# print("Number of consonents are: ",count)

# Check whether the char is lower,upper,number using function 
# def upper_lower_count(str):
#     upper_count=0
#     lower_count=0
#     numeber_count=0
#     special_count=0
#     for i in range(len(str)):
#         code=ord(str[i])
#         if code>=65 and code<=90:
#             upper_count+=1
#         elif code>=97 and code<=122:
#             lower_count+=1
#         elif code>=48 and code<=57:
#             numeber_count+=1
#         else:
#             special_count+=1
#     print(lower_count,upper_count,numeber_count,special_count)
# upper_lower_count(str=input())


# (hello-hfllp)write function to convert vowel char into next char
# def vowel_conversion(str):
#     new_string=""
#     for i in range(len(str)):
#         if str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u':
#             new_string+=chr(ord(str[i])+1)
#         else:
#             new_string+=chr(ord(str[i]))
#     print(new_string)
# vowel_conversion(str=input())

# # Split a string by spaces
# str=input()
# print(str.split(" "))

# # Check if string starts with "Hello".
# str=input()
# print(str.startswith("hello"))

# # Check if two strings are anagrams.
# str1=input()
# str2=input()
# print("Anagrams" if sorted(str1)==sorted(str2) else "not anagrams")

# # Reverse each word in a sentence.
# str=input()
# word=str.split()
# rev=[word[::-1] for w in word]
# print(rev) 

# # Find longest word in a sentence.
# str="hi hello how"
# word=str.split()
# longest_word=""
# for w in word:
#     if len(longest_word) < len(w):
#         longest_word=w
# print(longest_word)

# # Remove duplicate characters.
# sentence=input()
# for i in range(len(sentence)):
#     if (sentence.count(sentence[i]))==1:
#         print(sentence[i])

# # Count frequency of characters
# str=input()
# for i in range(len(str)):
#     print(str.count(str[i]))

# # Replace multiple spaces with single space
# str=input()
# for i in range(len(str)):
#     str=str.replace("  "," ")
# print(str)

# # Convert string to list of characters.
# str="namaste"
# str=list(str)
# print(str)

# Remove duplicate characters.
str="abcdabefgh"
str1=""
for i in range(len(str)):
    if str[i].count==1:
        str1+=i
print(str1)