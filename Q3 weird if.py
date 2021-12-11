



#if n is odd                       weird
#n is even and in range (2,5)      not weired
#n is even and in range(6,20)      weired
#n is even greater than 20         not weired


num=int(input("Enter a number:"))
if num % 2 != 0 :
    print("Weird")
else:
    if num>=2 and num<=5:
        print("not weired")
    elif num>=6 and num<=20:
        print("Weired")
    else:
        print("not weired")
