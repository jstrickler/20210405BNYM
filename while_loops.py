while True:
    user_name = input("Enter name: ")
    if user_name == 'q':
        break
    if user_name == '':
        continue
    print("Welcome,", user_name)

