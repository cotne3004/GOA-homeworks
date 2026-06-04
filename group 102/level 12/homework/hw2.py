# 2) შექმენით ფუნქცია სახელად minimum რომელსაც გადაეცემა მასივი, ამ ფუნქციის დავალება არის ის, რომ იპოვოს ყველაზე პატარა რიცხვი მასივიდან. (min ფუნქციის გამოყენება არ შეიძლება)

def minimum(arr):
  smallest = arr[0] 

  for i in arr:
    if smallest > i:
      smallest = i 

  return smallest

print(minimum([5,4,5,7,4,5,2,9,6,4]))