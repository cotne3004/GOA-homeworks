# 5) შექმენით ფუნქცია სახელად even_or_odd რომელსაც გადაეცემა რიცხვი, მისი დავალება არის ის,
#  რომ შეამოწმოს რიცხვი, თუ რიცხვი ლუწია დააბრუნოს "This number is even" ყველა სხვა შემთხვევაში "This number is odd".

def even_or_odd(num):
    if num % 2 == 0:
        return 'this number is even'
    else:
        return 'this number is odd'
    
result = even_or_odd(8)
print(result)