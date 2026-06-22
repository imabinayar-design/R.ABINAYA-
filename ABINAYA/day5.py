'''
count=11
while count>=1:
    print(count)
    count-=1

count=1
print("odd numbers are,")
while count<=20:
    print(count)
    count+=2


count=2
print("even numbers are;")
while count<=20:
  print(count)
  count+=2
print("loop finished")
'''
'''
ip=int(input("choose your number to display:\n1.two table\n2 three table\n3 four table\n4 five table\n5 ten table\n"))
if ip==1:
    count=1
    while count<=10:
        print(count,'*2=',count*2)
        count+=1
elif ip==2:
    count=1
    while count<=10:
        print(count,'*3=',count*3)
        count+=1
elif ip==3:
    count=1
    while count<=10:
        print(count,'*4=',count*4)
        count+=1
elif ip==4:
    count=1
    while count<=10:
        print(count,'*5=',count*5)
        count+=1
elif ip==5:
    count=1
    while count<=10:
        print(count,'*10=',count*10)
        count+=1
else:
    print("invalid")
'''
'''
num=int(input("enter the number:"))
i=1
while num>0:
    i=i*num
    num=num-1
print("factorial of is",i)
'''
'''
i=20
for i in range(10,1,-1):
 print (i)
 '''
'''
print("even numbers are")
for i in range(2,20,2):
 print(i)
print("odd numbers are")
for i in range(1,20,2):
 print(i)
'''
'''
n=int(input("choose your choice to dispaly tables:"))
i=1
for i in range(1,11,1):
 print(i,'*',n,'=',n*i)
 i+=1     
'''
num =int(input("enter the number:"))
i=1
for i range(i*num*num-1,n-1,1):
    print("factorial of", num,"is",i)
 

         
       
