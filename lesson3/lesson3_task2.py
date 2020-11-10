# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_info(name, surname, birthday_year, location, email, phone_number):
    print(f"user name is {name} {surname}, born in {birthday_year}, living in {location}, contacts: {email} and {phone_number}")


name = input("enter name.. ")
surname = input("enter surname.. ")
year = input("enter year.. ")
location = input("enter location.. ")
email = input("enter email.. ")
phone_number = input("enter phone number.. ")

user_info(name=name, surname=surname, birthday_year=year, location=location, email=email, phone_number=phone_number)
