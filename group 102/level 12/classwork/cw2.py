# 2) შექმენით ფუნქცია სახელად is_positive რომელსაც გადაეცემა რაიმე რიცხვი, მისი დავალებაა: თუ რიცხვი დადებითია (ნულზე მეტი)
#  მაშინ უნდა დაბრუნდეს ფუნქციიდან True, ყველა სხვა შემთხვევაში False.

def is_positive(num):
    if num > 0:
        return True
    else:
        return False
    
print(is_positive(5))
print(is_positive(-3))
print(is_positive(0))