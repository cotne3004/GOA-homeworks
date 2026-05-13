#4) შექმენით შერეული სია (ყველა მონაცემთა ტიპით), შემდგომ მომხმარებელს მიეცით ამ სიიდან ელემენტის წაშლის შესაძლებლობა,
#  რასაც შემოიტანს ის წაშალეთ, თუ შემოიტანა არარსებული ელემენტი - "Invalid Choice" გამოიტანეთ ტერმინალში.

my_list = [10,'cotne',31.2,False]

remove_element = input('remove element: ')


if remove_element == '10':
    my_list.remove(10)
    print(my_list)

elif remove_element == 'cotne':
    my_list.remove('cotne')
    print(my_list)

elif remove_element == '31.2':
    my_list.remove(31.2)
    print(my_list)

elif remove_element == 'False':
    my_list.remove(False)
    print(my_list)
else:
    print('Invalid Choice')