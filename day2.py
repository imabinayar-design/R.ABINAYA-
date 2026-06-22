'''a = int(input("enter a number :"))
if a%2==0:
 print("it it is even number")
else:
 print("it is odd number")'''

'''a = input("enter a day:")
if a == "sunday":
    print("holiday")
else:
    print("working day")
           

age= int(input("enter your age:"))
wt= int(input("enter your weight:"))
if (age >=18 and wt >=50):
 print("you're eligible to blood donation")
else:
 print("you're not eligible to blood donation") 

a=int(input("enter a number:"))
if a%4==0:
 print("this is leap year")
else:
 print("this is not leap year")

a= int(input("enter a number:"))
if(a>0):
 print("it is positive number")
else:
 print("it is negative number")


traffic=input("enter your signal:")
if traffic=="red":
 print("stop")
elif traffic=="yellow":
 print("get ready")
elif traffic =="green":
 print("go")
else:
 print("error")

a=input("student name:")
tam1=int(input("tamil :"))
eng1=int(input("english :"))
mat1=int(input("maths :"))
tot1=tam1+eng1+mat1
print(tot1)
avg1=tot1/3
print(avg1)

b=input("student name:")
tam2=int(input("tamil :"))
eng2=int(input("english :"))
mat2=int(input("maths :"))
tot2=tam2+eng2+mat2
avg2=tot2/3
print(avg2)


c=input("student name:")
tam3=int(input("tamil :"))
eng3=int(input("english :"))
mat3=int(input("maths :"))
tot3=tam3+eng3+mat3
avg3=tot3/3
print(avg3)


if (avg1>avg2 and avg1>avg3):
 print("student got 1st rank is",a)
elif (avg2>avg1 and avg2>avg3):
 print("student got 1st rank is",b)
elif (avg3>avg1 and avg3>avg2):
  print("student got 1st rank is",c)
elif(avg1<avg2 and avg1>avg3):
  print("student got 2nd rank is",a)
elif(avg2<avg1 and avg2>avg3):
  print("student got 2nd rank is",b)
elif(avg3<avg1 and avg3>avg2):
  print("student got 2nd rank is",c)
elif(avg1<avg2 and avg1<avg3):
  print("student got 3rd rank is",a)
elif(avg2<avg1 and avg2<avg3):
  print("student got 3rd rank is",b)
elif(avg3<avg1 and avg3<avg2):
  print("student got 3rd rank is",c)
else:
 print("inalid input")
     
'''

a=input("enter food:")
qty=int(input("quantity:"))
rate=int(input("rate:"))
tot=qty*rate
print("total :",tot)
if tot>=500 and tot<100:
 discount=tot*0.25
 print("you got 25% discout offer,you have to pay Rs ",discount)
elif tot> 1000:
 discount=tot*0.5 
 print("you got 50% discount offer,you have to pay Rs",discount)
else:
 print("no offer")
         
     

