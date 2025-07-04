# Check whether the char is lower,upper,number using function 
def upper_lower_count(str):
    upper_count=0
    lower_count=0
    numeber_count=0
    special_count=0
    for i in range(len(str)):
        code=ord(str[i])
        if code>=65 and code<=90:
            upper_count+=1
        elif code>=97 and code<=122:
            lower_count+=1
        elif code>=48 and code<=57:
            numeber_count+=1
        else:
            special_count+=1
    print(lower_count,upper_count,numeber_count,special_count)
upper_lower_count(str=input())


# (hello-hfllp)write function to convert vowel char into next char
def vowel_conversion(str):
    new_string=""
    for i in range(len(str)):
        if str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u':
            new_string+=chr(ord(str[i])+1)
        else:
            new_string+=chr(ord(str[i]))
    print(new_string)
vowel_conversion(str=input())