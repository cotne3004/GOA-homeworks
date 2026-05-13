# 3) შექმენით 2 სია რომლებშიც მომავალში მოათავსებთ ლუწ რიცხვებს და კენტ რიცხვებს, მომხმარებელს შემოაყვანინეთ 10 რიცხვი,
#  ლუწი რიცხვები ჩაამატეთ ლუწი რიცხვების სიაში, კენტი რიცხვები - კენტი რიცხვების სიაში. (კენტ / ლუქზე შემოწმება - n % 2 == 0)

even = []
odd = []

num1 = int(input("enter your first number:"))
num2 = int(input("enter your second number:"))
num3 = int(input("enter your third number:"))
num4 = int(input("enter your fourth number:"))
num5 = int(input("enter your fifth number:"))
num6 = int(input("enter your sixth number:"))
num7 = int(input("enter your seventh number:"))
num8 = int(input("enter your eighth number:"))
num9 = int(input("enter your ninth number:"))
num10 = int(input("enter your 10 number:"))

if num1 % 2 ==0:
    even.append(num1)
else:
    odd.append(num1)

if num2 % 2 ==0:
    even.append(num2)
else:
    odd.append(num2)

if num3 % 2 ==0:
    even.append(num3)
else:
    odd.append(num3)

if num4 % 2 ==0:
    even.append(num4)
else:
    odd.append(num4)

if num5 % 2 ==0:
    even.append(num5)
else:
    odd.append(num5)

if num6 % 2 ==0:
    even.append(num6)
else:
    odd.append(num6)

if num7 % 2 ==0:
    even.append(num7)
else:
    odd.append(7)

if num8 % 2 ==0:
    even.append(num8)
else:
    odd.append(num8)

if num9 % 2 ==0:
    even.append(num9)
else:
    odd.append(num9)

if num10 % 2 ==0:
    even.append(num10)
else:
    odd.append(num10)

print(odd)
print(even)