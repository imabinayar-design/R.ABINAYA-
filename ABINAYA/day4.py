'''name=input("user name:")
password=int(input("password:"))
if name=="ABINAYA" and password==1234:
 print("login successfully")
 print("choose any hotel: \n1.grand inn \n2.royalglitz \n3.foodparadise")
 ch=int(input("enter your choice :"))
 if ch==1:
    print("***************************")
    print("{WELCOME TO GRAND INN")
    print("***************************")
    print("choose your meal time: \n1)breakfast \n2)launch \n3)dinner")
    tm=int(input("your option:"))
    if tm == 1:
       menu=int(input("choose breakfast as available are, \n1.idly \n2.dosa \n3.poori\n"))
       if menu==1:
        rate=10
       elif menu==2:
        rate=50
       elif menu==3:
        rate=60
       else:
        print("inavlid menu")
    elif tm==2:
     menu=int(input("choose available launch are,\n1.meals \n2.chicken \n3 bryani\n"))
     if menu==1:
          rate=100
     elif menu==2:
          rate=150
     elif menu==3:
          rate=200
     else:
        print("inavlid menu")
    elif tm==3:
     menu=int(input("choose available dinner are,\n1.chappathi\n2.noodles\n3.chicken\n"))
     if menu==1:
          rate==40
     elif menu==2:
          rate=125
     elif menu==3:
          rate=150
     else:
      print("invalid menu")
    else:
        print("invalid timing")
    if tm==1 or tm==2 or tm==3 :
        print("***************************")
        print("------BILL RECIEPT---------")
        print("***************************")
        quantity=int(input("quantity:"))
        total=rate*quantity
        print("***************************")
        print("you have to pay Rs.",total)
        print("***************************")
        print("welcome,visit us again")
    else:
        print("invalid")
 elif ch==2:
  print("***************************")
  print("WELCOME TO ROYALGLITZ")
  print("***************************")
  print("choose your meal time: \n1)breakfast \n2)launch \n3)dinner")
  tm=int(input("your option:"))
  if tm==1:
   menu=int(input("choose breakfast as available are \n1.aapam \n2.dosa \n3.chapathi\n"))
   if menu==1:
    rate=30
   elif menu==2:
    rate=50
   elif menu==3:
    rate=40
   else:
    print("inavlid menu")
  elif tm==2:
    menu=int(input("choose available launch are,\n1.sambar \n2.meals \n3 variety rice\n"))
    if menu==1:
     rate=60
    elif menu==2:
     rate=100
    elif menu==3:
     rate=90
    else:
     print("inavlid menu")
  elif tm==3:
    menu=int(input("choose available dinner are,\n1.veg noodelea\n2.chicken noodles\n3.fish fry\n"))
    if menu==1:
     rate==125
    elif menu==2:
     rate=140
    elif menu==3:
     rate=120
    else:
     print("invalid menu")
  else:
      print("invalid timing")
  if tm== 1 or tm==2 or tm==3:
    print("***************************")
    print("------BILL RECIEPT---------")
    print("***************************")
    quantity=int(input("quantity:"))
    total=rate*quantity
    print("***************************")
    print("you have to pay Rs.",total)
    print("***************************")
    print("welcome,visit us again")
  else:
      print("invalid")
 elif ch==3:
  print("***************************")
  print("{WELCOME TO FOODPARADISE")
  print("***************************")
  print("choose your meal time: \n1.breakfast \n2.launch \n3.dinner")
  tm=int(input("your option:"))
  if tm==1:
    menu=int(input("choose breakfast as available are, \n1.tea \n2.bradbutter jam \n3.dosa\n"))
    if menu==1:
      rate=30
    elif menu==2:
        rate=40
    elif menu==3:
        rate=60
    else:
        print("inavlid menu")
  elif tm==2:
    menu=int(input("choose available launch are,\n1.fried rice \n2.chicken rice \n3 mutton rice\n"))
    if menu==1:
     rate=100
    elif menu==2:
     rate=150
    elif menu==3:
     rate=200
    else:
     print("inavlid menu")
  elif tm==3:
    menu=int(input("choose available dinner are,\n1.chinese noodelea\n2.korean noodles\n3.sushi\n"))
    if menu==1:
     rate==150
    elif menu==2:
     rate=160
    elif menu==3:
     rate=120
    else:
     print("invalid menu")
  if tm==1 or tm==2 or tm==3:
      print("***************************")
      print("------BILL RECIEPT---------")
      print("***************************")
      quantity=int(input("quantity:"))
      total=rate*quantity
      print("***************************")
      print("you have to pay Rs.",total)
      print("***************************")
      print("welcome,visit us again")
  else:
      print("invalid")

 else:
      print("invalid input,no hotel found")
      print("try again!")
else:
 print("incorrect username or password")
 print("try again!")
'''
count=1
while count<=5:
    print(count)
    count+=1
for i in range(1,10+1):
    print(i)
   
