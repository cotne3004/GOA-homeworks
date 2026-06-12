# 5) შექმენი ცარიელი სეტი სადაც დაამატებ მხოლოდ კენტებს for loop გამოყენებით.

listt = set()

for i in range(1,20):
    if i % 2 == 1:
        listt.add(i)

print(listt)