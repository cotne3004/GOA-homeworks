# 3) შექმენით ფუნქცია სახელად maximum რომელსაც გადაეცემა მასივი, ამ ფუნქციის დავალება არის ის, რომ იპოვოს ყველაზე დიდი რიცხვი მასივიდან. (max ფუნქციის გამოყენება არ შეიძლება)

def maximum(arr):
  biggest = arr[0] 

  for i in arr:
    if biggest < i:
      biggest = i 

  return biggest

print(maximum([5,4,5,7,4,5,2,9,6,4]))