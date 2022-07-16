names = ["Кбубудущее", "Ктиффлор", "Ведророл", "Гарпирия"]

while True:

    name = input("Кто ты? :")
    if name not in names:
        print("Тут вообще ничего нет. Есть вопросы?")
    else:
        print(f"Ты - свой. Приветствую тебя, {name}! Пароль: 123456")
        break