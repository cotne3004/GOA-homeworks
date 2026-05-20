# 7) შექმენით ლისტი: ["apple", "banana", "orange", "kiwi"]. for ციკლის გამოყენებით მოძებნეთ "banana" და remove() ფუნქციით წაშალეთ,
#  შემდეგ for ციკლით დაბეჭდეთ დარჩენილი ელემენტები.

fruits = ["apple", "banana", "orange", "kiwi"]

for fruit in fruits:
    if fruit == "banana":
        fruits.remove("banana")

for fruit in fruits:
    print(fruit)
    