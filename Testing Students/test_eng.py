# Создадим тест в виде словаря интересных буржуйских слов
# составлено в подленьком стиле ЗНО
def verification():
    funnyWords = {
    "1. Cucumber - в переводе: ": ["1-весёлый человек", "2-почтительное обращение", "3-огурец"],
    "2. Cheap - в переводе: ": ["1-микросхема", "2-дешёвый", "3-имя бурундука"],
    "3. Expensive - в переводе: ": ["1-дорогой", "2-маниакальное настроение", "3-пуля со смещённым центром тяжести"],
    "4. Cookie - в переводе: ": ["1-фрагмент данных", "2-печенье", "3-весёлый человек"],
    "5. Mouse - в переводе: ": ["1-компьютерный манипулятор", "2-герой мультфильмов Микки", "3-подбитый глаз"]
    }
    return funnyWords

comic = verification()
# print(comic)

for key in comic:
    print(key, '->', comic[key])

def check():
    mark = 0
    answer1 = input("Введите номер правильного на Ваш взгляд ответа на вопрос 1: ")
    if answer1 == '3':
        mark += 1
    answer2 = input("Введите номер правильного на Ваш взгляд ответа на вопрос 2: ")
    if answer2 == '2':
        mark += 1
    answer3 = input("Введите номер правильного на Ваш взгляд ответа на вопрос 3: ")
    if answer3 == '1':
        mark += 1
    answer4 = input("Введите номер правильного на Ваш взгляд ответа на вопрос 4: ")
    if answer4 == '1':
        mark += 1
    answer5 = input("Введите номер правильного на Ваш взгляд ответа на вопрос 5: ")
    if answer5 == '1':
        mark += 1

    return str(mark)

allAnswers = check()
print('У вас ' + allAnswers + ' баллов')

choZaTest = str('Your English score is ' + allAnswers + ' points')

# Импортируем модуль json, сериализируем и сохраняем в файле результаты тестирования
import json
nana = input("Введите ПРОСТО ваш логин с номером (через тире) попытки тестирования ligin-1(2)(3) БЕЗ РАСШИРЕНИЯ: ")
nene = input("Введите ваш логин-номер С РАСШИРЕНИЕМ .txt для создания файла ваших результатов: ")
rezik = {
    nana: choZaTest
}
jdata = json.dumps(rezik)
# Записываем сериализированную инфу в файл (в виде словаря)
with open(nene, "w") as f:
    f.write(jdata)
