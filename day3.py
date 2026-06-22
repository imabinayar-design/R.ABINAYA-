'''
name=input("user name :")
password=int(input("password :"))
if name=="ABINAYA" and password==1234:
 print("login sucessfully")
 main=input("choose any option: \n1.debit \n2.withdrawal \n3.balance \n4.exit")
 ip=int(input("enter your choice :"))
 balance=5000 
 if ip==1:
   amount=int(input("enter amount to debit :"))
   if amount > 5000:
    print("you cannot debit amount")
   elif amount <= 5000:
    print("amount debited successfully")
    print("your available balance is Rs.",balance+amount)
 elif ip==2:
  amt = int(input("enter amount to withdraw :"))
  if amt > 5000:
   print("you cannot withdraw amount")
  elif amt <= 5000:
   print("withdraw sucessfully")
   print("your available balance is Rs.",balance-amt)
 elif ip==3:
  print("your availabe balance is Rs.",balance)
 elif ip==4:
  print("welcome visit us again")
else:
 print("incorrect username or password")
 print("try again!")
'''
name=input("user name:")
password=int(input("password:")
if name=="abi" and password==1234
 print("login successfully")
 hot=("choose any hotel: \n1.hotel1 \n2.hotel2 \n3.hotel3")
 ch=int(input("enter your choice :"))
 if hot==1:
  tm=input("choose your meal time: \na)breakfast \nb)launch \nc)dinner)
  if tm==a:
    mb=("choose breakfast as available are, \n1.idly \n2.dosa \n3.poori")
    idly=10
    dosa=50
    poori=40
    if mb==1:
     amount1=idly
    elif mb==2:
     amount2=50
    elif mb==3:
     amount3=40
    elif mb==1 and 2:
     amt1=amount1+amount2
    elif mb==1 and 3:
     amt2=amount1+amount3
    elif mb==2 and 3:
     amt3=amount2+amount3
  elif tm==b:
      ml=("choose available launch are,\n1.meals \n2.chiken \n3 bryani")
      meals=100
      chicken=150
      bryani=250
 elif hot==2:
     tm=input("choose your meal time: \na)breakfast \nb)launch \nc)dinner)
  if tm==a:
    mb=("choose breakfast as available are \n1.aapam \n2.dosa \n3.chapathi")
    idly=10
    dosa=50
    poori=40
    if mb==1:
     amount1=idly
    elif mb==2:
     amount2=50
    elif mb==3:
     amount3=40
    elif mb==1 and 2:
     amt1=amount1+amount2
    elif mb==1 and 3:
     amt2=amount1+amount3
    elif mb==2 and 3:
     amt3=amount2+amount3
  else:
    print("invalid input,no meals avilable")
else:
 print("incorrect username or password")
 print("try again!") 
    
