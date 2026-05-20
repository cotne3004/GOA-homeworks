# 10) შექმენით პროგრამა, რომელიც მომხმარებელს for ციკლის გამოყენებით 5-ჯერ შემოატანინებს სახელს, დაამატებს ლისტში და შემდეგ for ციკლით ყველა სახელს დაბეჭდავს.

name_list = []

for name in range(5):
    names = input('enter name:')
    name_list.append(names)

for name in name_list:
    print(name)