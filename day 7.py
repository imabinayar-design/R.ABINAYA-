'''
usrname='ABI'
username=input("username:")
while username!=usrname:
    print("incorrect username,try again")
    username=input("username:")
print ("usertname is correct")
 
'''
num=int(input("enter a number:"))
if num<1:
    print("its not a prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print("its not a prime")
            break;
    else:
         print("it is prime")
