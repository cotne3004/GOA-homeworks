# 1) შექმენი ცვლადი secret  რომელიც უდრის რაღაც რიცხვს და ასევე num უდრის 0 და while loop უნდა
#  იმუშავოს მაქამდე სანამ num != secret და while შიგნით num უნდა უდრიდეს input რომ მომხმარებელმა
#  შეიყვანოს რიცხვი და თუ გამოიცნობს მაშინ გამოიტანოს "you win".

secret_num = 7

num = 0

while num != secret_num:
    num = int(input('enter number here:'))
    
    if num == secret_num:
        print('you win')
    else:
        print('try again')