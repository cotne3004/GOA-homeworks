# 4) შექმენით ფუნქცია სახელად sum_manual რომელსაც გადაეცემა რიცხვების მასივი, ამ ფუნქციის დავალლება არის ის,
#  რომ დააბრუნოს ყველა რიცხვის ჯამი ამ მასივიდან. (sum ფუნქციის გამოყენება არ შეიძლება)


def sum_manual(masive):
    sum = 0
    
    for num in masive:
        sum += num
        
    return sum


masive = [14, 5, 23, -3, 8, 0, 11]
result = sum_manual(masive)

print(f"მასივის რიცხვების ჯამია: {result}")