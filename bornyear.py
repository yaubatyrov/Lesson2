# Запрашиваем у пользователя год рождения А.С. Пушкина
year = input("Введите год рождения А.С. Пушкина: ")

# Устанавливаем правильный год рождения
correct_year = "1799"

# Проверяем, правильно ли пользователь ввел год
if year == correct_year:
    print("Верно")
else:
    print("Неверно")