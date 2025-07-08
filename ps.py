n1=15
n2=20
big=0
small=0
if n1>n2:
    big=n1
    small=n2
else:
    big=n2
    small=n1
if big % small ==0:
    print(big,"is the LCM")
else:
    lcm_not_found=True
    temp_lcm=big+big
    while lcm_not_found==True:
        if temp_lcm % n1==0 and temp_lcm%n2==0:
            print(temp_lcm,"is the lcm")
            break
        else:
            temp_lcm+=big