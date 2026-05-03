#4) მომხმარებელს შემოაყვანინეთ მისი სახელი, გვარი, ასაკი, საყვარელი ფერი, საყვარელი რიცხვი, ქალაქი და შემდგომ გამოიტანეთ ყველაფერი შემდეგ ფორმატში:
#name: {name}
#last name: {last_name}
#age: {age}
#favorite color: {favorite_color}
#favorite number: {favorite_number}
#ciry: {ciry}

#ასევე მომხმარებილის მიერ შემოყვანილი რიცხვი გაამრავლეთ 2 - ზე და გამოიტანეთ შედეგი ასეთი სახით:
#მაგალითად მომხმარებლის რიცხვი არის 10

#10 * 2 = 20


name=input("whats your name?:")
lastname=input("whats your lastname?:")
age=int(input("whats your  age?:"))
favouritecolor=input("whats your favourite color?:")
favouritenumber=input("whats your favourite number?:")
city=input("in which city do you live?:")

print("my name is:" , name)
print("my lastname is:" , lastname)
print("my age is:" , age)
print("my favourite color is:" , favouritecolor)
print("my favourite number is:" , favouritenumber)
print("i live in:" , city)

print(favouritenumber*2)
