def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
            
    return True    
#num = int(input("enter number"))

if is_prime(73):
    print("true")

else:
    print("false")
if is_prime(75):
    print("true")

else:
    print("false")
