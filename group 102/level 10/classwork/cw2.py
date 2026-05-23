# 2) თქვენს კოდს დაუმატეთ შეზღუდვა (სიცოცხლეები), მომხმარებელს არ უნდა შეეძლოს პაროლის უსასრულოდ შემოყვანა

correct_password = "python123"

password_input = input('enter password here:')

Lives = 2

while password_input != correct_password and Lives !=0:
    password_input = input('wrong, try again:')
    Lives -= 1

if password_input == correct_password and Lives != -1:
    print ('acces granted')

else:
    print('lives expired')