# 11) შექმენით ლისტი 5 რიცხვით. for ციკლის გამოყენებით იპოვეთ ყველაზე დიდი რიცხვი.

nums = [11,43,21,54,232,432,12,54,65]

highest_num = nums[0]

for number in nums:
    if number > highest_num:
        highest_num = number

print (highest_num)