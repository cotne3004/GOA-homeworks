# 5) Hard - შექმენი სია სადაც გექნება ეს ელემენტები [1,2,3,True,False,"hello","python"] და შექმენი 3 ცარიელი სია integer,
#  bool, string და for loop გამოყენებით გაუყვები თავდაპირველ სიას და if statment-ით გადაანაწილებს ტიპებს თავის სიებში მაგ:
#  თუ ელემენტი integer მაშინ დაამატებ სიაში რომელსაც ჰქვია integer და ბოლოს

mixed_list = [1, 2, 3, True, False, "hello", "python"]

int_list = []
bool_list = []
string_list = []

for i in mixed_list:
    
    if type(i) == bool:
        bool_list.append(i)
    
    elif type(i) == int:
        int_list.append(i)
    
    elif type(i) == str:
        string_list.append(i)

print(int_list)
print(bool_list)
print(string_list)

tup_int = tuple(int_list)
tup_bool = tuple(bool_list)
tup_string = tuple(string_list)

print(tup_int)
print(tup_bool)
print(tup_string)