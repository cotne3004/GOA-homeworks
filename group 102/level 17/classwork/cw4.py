# 4) შექმენი ცარიელი სეტი და დაამატე რიცხვები 1-დან 20-მდე for loop გამოყენებით და შემდეგ როცა ყველა რიცხვს დაამატებ set გადააქციე tuple-ად და გამოიტანე იგი.

num_set = set()

for i in range(1, 21):
    num_set.add(i)

num_tuple = tuple(num_set)

print(num_tuple)