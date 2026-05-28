# 4) while loop გამოყენებით გამოიტანეთ მხოლოდ ლუწი რიცხვები. 

num1 = 0
num2 = 30
nums = []

while num1 <= num2:
    if num1 % 2 == 0:
        nums.append(num1)

    num1 += 1

print(nums)