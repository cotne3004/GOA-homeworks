# 3) მომხმარებელს შემოატანინეთ რიცხვი და while loop - ის გამოყენებით გამოიტანეთ რიცხვები (1 - იდან მომხმარებლის რიცხვის ჩათვლით) შემდეგი სახით:
# 1 this number is odd.
# 2 this number is even.
# 3 this number is odd.

# ანუ უნდა შეამოწმოთ რიცხვი ლუწია თუ კენტი.

num = int(input('enter number here:'))

count = 1

while count <= num:
    if count % 2 == 0:
        print('this number is even', count)
    else:
        print('this number is odd', count)

    count += 1