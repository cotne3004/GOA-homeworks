#8)დაწერეთ პროგრამა, რათა შეამოწმოთ იყოფა თუ არა რიცხვი სხვა რიცხვზე.

num1=int(input("enter first number:"))
num2=int(input("enter second number"))

if num1%num2==0:
    print("იყოფა")

elif num1%num2<0 or num1%num2>0:
    print("არიყოფა")