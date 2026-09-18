#bogdan
Bogdan_pass = "123"
Bogdan_rating = [8, 4, 9, 11, 8, 2]
#mykola
Mykola_pass = "234"
Mykola_rating = [5, 7, 11, 10, 4, 8]
#gregory
Gregory_pass = "345"
Gregory_rating = [12, 8, 4, 10, 3, 7]

your_name = str(input("Введіть логін: "))
your_name = your_name.title()
password = input("Введіть пароль: ")

if your_name == "Bogdan" and password == Bogdan_pass:
    for rating in Bogdan_rating:
        if rating <= 4:
            print(rating, "- Не задовільно")
        else:
            print(rating, "- Задовільно")
elif your_name == "Mykola" and password == Mykola_pass:
    for rating in Mykola_rating:
        if rating <= 4:
            print(rating, "- Не задовільно")
        else:
            print(rating, "- Задовільно")
elif your_name == "Gregory" and password == Gregory_pass:
    for rating in Gregory_rating:
        if rating <= 4:
            print(rating, "- Не задовільно")
        else:
            print(rating, "- Задовільно")
else:
    print("Неправильний логін або пароль")