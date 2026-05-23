# ვქმნით ცვლადებს მომხმარებლის მონაცემების შესანახად
reg_username = ""
reg_email = ""
reg_password = ""

# while ციკლი, რომელიც მუდმივად აჩვენებს მენიუს
while True:
    # გამოვაქვთ მთავარი მენიუ
    print("1. Registration")
    print("2. Login")
    print("3. Stop Programm")
    
    # მომხმარებელს შემოაქვს არჩევანი
    choice = input("Choose option: ")
    
    # თუ მომხმარებელმა აირჩია რეგისტრაცია
    if choice == "1":
        reg_username = input("Enter user name: ")
        reg_email = input("Enter email: ")
        reg_password = input("Enter password: ")
        
        print("Registration successfully!")
        # აქ ციკლი ჩვეულებრივ გრძელდება და ბრუნდება მენიუში
        
    # თუ მომხმარებელმა აირჩია ლოგინი
    elif choice == "2":
        login_email = input("Enter email: ")
        login_password = input("Enter password: ")
        
        # ვამოწმებთ, ემთხვევა თუ არა შემოტანილი მონაცემები რეგისტრაციის დროს შენახულს
        if login_email == reg_email and login_password == reg_password:
            print("Login successfully!")
            break  # წარმატებული ლოგინის შემთხვევაში ვთიშავთ პროგრამას
        else:
            print("Incorrect email or password!")
            
    # თუ მომხმარებელმა აირჩია პროგრამის გაჩერება
    elif choice == "3":
        break  # break ბრძანებით ვთიშავთ პროგრამას