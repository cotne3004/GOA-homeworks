# 6) მომხმარებელს for ციკლის გამოყენებით 5-ჯერ შემოატანინეთ რიცხვი, დაამატეთ ისინი ლისტში
#  და ბოლოს for ციკლით დაბეჭდეთ თითოეული ელემენტი და len() ფუნქციის გამოყენებით ლისტის სიგრძე.

liist = []

for i in range(5):
    num = int(input('enter your number:'))
    liist.append(num)

for num in liist:
    print(num)
    print(len(liist))