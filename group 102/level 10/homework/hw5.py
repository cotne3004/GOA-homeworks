# Bonus:
# 5) გააკეთეთ რეგისტრაციის და ავტორიზაციის შესახებ CLI (Command Line Interface):
# როდესაც პროგრამა გაეშვება მომხმარებელს უნდა გამოუვიდეს მსგავსი რაღაცა:
# 1. Registration
# 2. Login
# 3. Stop Programm

# როდესაც მომხმარებელი აირჩევს რეგისტრაციას:
# მოსთხოვეთ მისი user name, email და password, შემდგომ ეს ინფორმაცია შეინახეთ user სიაში ან შექმენით შესაბამისი ცვლადები და გამოუტანეთ შეტყობინება "Registration successfully!", ასევე გადაიყვანეთ მომხმარებელი საწყის menu - ში ანუ  ისევ გამოუტანეთ:
# 1. Registration
# 2. Login
# 3. Stop Programm

# როდესაც მომხმარებელი აირჩევს ლოგინს:
# მოსთხოვეთ მისი email - ი და password - ი, თუ არასწორი იქნება რაიმე გამოუტანეთ შესაბამისი შეტყობინება, თუ სწორია იქნება ინფორმაცია მაშინ გამოუტანეთ "Login successfully!" და გათიშეთ პროგრამა.

# თუ აირჩია Stop Programm მაშინ გათიშეთ პროგრამა.

# როდესაც გააკეთებთ დავალებას აუცილებლად ახსენით მთლიანი კოდი კომენტარებით.

#ცვლადები რომ შევინახოთ მომხმარებლის მონაცემები
reg_user = []
reg_email = []
reg_pass = []

#ვაილ ციკლი რომ მენიუ ვაჩვენოთ სულ
while True:
#გამოგვაქ მენიუ
    print('1. registration')
    print('2. login')
    print('3. stop program')
#მომხმარებელი აკეთებს არჩევანს
    user_choice = input('enter your choice:')
#თუ მომხმარებელი ირჩევს რეგისტრაციას
    if user_choice == '1':
        print('Registration')
        reg_user = input('enter your username:')
        reg_email = input('enter your email:')
        reg_pass = input('enter your password:')
        print('registration succesfully')
#გვაბრუნებს მენიუში

#თუ მომხმარებელი აირჩევს ლოგინს
    elif user_choice == '2':
        print('login')
        login_email = input('enter your email:')
        login_password = input('enter your password:')
#ვამოწმებთ ემთხვევა თუარა შემოტანილი მონაცემები რეგისტრაციის მონაცემებს
        if login_email == reg_email and login_password == reg_pass:
            print('login succesfully')
            break #თუ სწორად შეიყვანა ყველაფერი ჩერდება ციკლი
        else:
            print('something went wrong try again later:')
#თუ აირჩია მომხმარებელმა პროგრამის გაჩერება
    elif user_choice == "3":
        break #ვთიშავტ პროგრამას

    