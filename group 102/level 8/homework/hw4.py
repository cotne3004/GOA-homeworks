# 4) შექმენით ცარიელი ლისტი. მომხმარებელს for ციკლის გამოყენებით 5-ჯერ შემოატანინეთ სიტყვა და თითოეული append() ფუნქციის გამოყენებით დაამატეთ ლისტში.
#  ბოლოს for ციკლით დაბეჭდეთ ყველა ელემენტი.

listt = []

for i in range(5):
    word = input('enter word:')
    listt.append(word)

for element in listt:
    print (element)