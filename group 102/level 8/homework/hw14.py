# 14) შექმენით პროგრამა, სადაც მომხმარებელი შეიყვანს რამდენი რიცხვის დამატება უნდა ლისტში.
#  for ციკლით იმდენჯერ შემოატანინეთ რიცხვი, დაამატეთ append() ფუნქციით და ბოლოს for ციკლით დაბეჭდეთ ყველა ელემენტი და len() ფუნქციით ლისტის სიგრძე.

listt = []

count = int(input('ჩაწერეთ რამდენი რიცხვის ჩამატება გსურთ:'))

for i in range(count):
    num = int(input('enter number:'))
    listt.append(num)

for element in listt:
    print(element)

print(len(listt))