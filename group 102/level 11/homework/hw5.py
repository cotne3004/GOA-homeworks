# 5) while lopp გამოყენებით გამოიტანეთ მხოლოდ კენტი რიცხვები.

num1 = 0
num2 = 30
nums = []

while num1 <= num2:
    if num1 % 2 == 1:
        nums.append(num1)

    num1 += 1

print(nums)