# Создадим тест в виде словаря умных музыкальных слов
# составлено в подленьком стиле ЗНО
def verification():
    note = {
    "1.Лист": ["наружный орган растения", "композитор", "кусочек бумаги"],
    "2.Камертон": ["уголовный стиль общения", "инструмент для обработки камня", "инструмент для воспроизведения эталонных звуков"],
    "3.Каприччио ": ["свободное музыкальное произведение", "вид пиццы", "друг Педруччио"],
    "4.Аккомпанемент": ["отсутствие компа", "важный милиционер", "музыкальное сопровождение"],
    "5.Аччелерандо": ["сицилийский мафиози", "блюдо из макарон", "ускорение темпа музыки"],
    }
    return note

questList = verification()

for key in questList:
    print(key, '->', questList[key])

def check():
    mark = 0
    answer1 = input("Введите номер правильного на Ваш взгляд ответа на вопрос 1: ")
    if answer1 == '2':
        mark += 1
    answer2 = input("Введите номер правильного на Ваш взгляд ответа на вопрос 2: ")
    if answer2 == '3':
        mark += 1
    answer3 = input("Введите номер правильного на Ваш взгляд ответа на вопрос 3: ")
    if answer3 == '1':
        mark += 1
    answer4 = input("Введите номер правильного на Ваш взгляд ответа на вопрос 4: ")
    if answer4 == '3':
        mark += 1
    answer5 = input("Введите номер правильного на Ваш взгляд ответа на вопрос 5: ")
    if answer5 == '3':
        mark += 1

    return str(mark)

allAnswers = check()
print('У вас ' + allAnswers + ' баллов')

choZaTest = str('Your Music score is ' + allAnswers + ' points')

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
