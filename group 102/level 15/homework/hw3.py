# 3) შექმენი სეტი სადაც გექნება მოცემული რიცხვები 1-დან 10-მდე და შექმენი ცარიელი სია სადაც დაამატებ მხოლო ლუწ რიცხვებს სეტიდან.

listt = {1,2,3,4,5,6,7,8,9,}
odd = []
even = []
for i in listt:
    if i % 2 == 1:
        odd.append(i)
    else:
        even.append(i)

print(odd)
print(even)