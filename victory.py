def run_quiz():
    # Словарь известных личностей и их годов рождения
    celebrities = {
        'Альберт Эйнштейн': '1879',   # Подсказка: 1879
        'Исаак Ньютон': '1643',       # Подсказка: 1643
        'Мари Кюри': '1867',          # Подсказка: 1867
        'Леонардо да Винчи': '1452',  # Подсказка: 1452
        'Стив Джобс': '1955'          # Подсказка: 1955
    }

    correct_answers = 0
    total_questions = len(celebrities)

    # Запрашиваем у пользователя годы рождения знаменитостей
    for celebrity, birth_year in celebrities.items():
        user_answer = input(f"Введите год рождения {celebrity}: ")
        if user_answer == birth_year:
            correct_answers += 1
            print("Верно!")
        else:
            print("Неверно!")

    # Рассчитываем результаты
    incorrect_answers = total_questions - correct_answers
    correct_percentage = correct_answers * 100 / total_questions
    incorrect_percentage = incorrect_answers * 100 / total_questions

    # Выводим результаты
    print("\nРезультаты викторины:")
    print(f"Правильных ответов: {correct_answers}")
    print(f"Ошибок: {incorrect_answers}")
    print(f"Процент правильных ответов: {correct_percentage:.2f}%")
    print(f"Процент неправильных ответов: {incorrect_percentage:.2f}%")

    # Предлагаем пользователю повторить игру
    restart = input("Хотите начать игру сначала? (да/нет): ").lower()
    if restart == "да":
        run_quiz()
    else:
        print("Спасибо за игру!")


# Запускаем викторину
run_quiz()
