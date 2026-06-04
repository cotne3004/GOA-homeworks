# 1) შექმენით ფუნქცია სახელად len_manual რომელსაც გადაეცემა რაიმე data, ამ ფუნქციამ უნდა დააბრუნოს სიმბოლოების რაოდენობა data - ში (len ფუნქციის გამოყენება არ შეიძლება)


def len_manual(data):
    count = 0
    
    for i in data:
        count += 1
        
    return count

pasuxi = len_manual("ცოტნე")
print(pasuxi)