class List_tests:
    def __init__(self):
        self.test_name = None
        self.test_number = None
        self.dict = None

    def input_test(self):
        self.test_name = input("Inpun NAME of your new test: "
                               "English, Literature, Geography, Music, Medicine. "
                               "Сделайте свой выбор: ")
        self.test_number = input("Inpun NUMBER of your new test: "
                                 "English - 1, Literature - 2, Geography - 3, Music - 4, Medicine - 5. "
                                 "Сделайте свой выбор: ")

    def input_dic(self):
        self.dict = {
            self.test_name: self.test_number
        }
        return dict


    # Создадим функцию сериализации этого Словаря в файл методом dump модуля json
    def save(self):
        import json
        # Вводим с клавиатуры имя файла для записи нашей сериализированной информации
        fylets = input("Введите имя файла: ")
        with open(fylets, "a") as f:
            json.dump(self.dict, f)
        f.close()
        # Создадим функцию десериализации данных из файла в Словарь методом load модуля json

    def load(self):
        import json
        # Создаём словарь для записи десериализированной из файла информации:
        tester = {}
        # Вводим с клавиатуры имя файла для записи нашей сериализированной информации
        fylets = input("Введите имя файла: ")
        # Указываем файл:
        with open(fylets, "r") as f:
            # Записываем инфу из этого файла в созданный словарь
            tester = json.load(f)
        f.close()
        return print(tester)


student = List_tests()
student.__init__()
student.input_test()
student.input_dic()
student.save()
# student.load()

class List_questions(List_tests):
    def __init__(self):
        super().__init__()
        self.subject = None
        self.dict_q = None
        self.filik = None

    def selectSubject(self):
        self.subject = input("Выберите имя теста и нажмите его цифру (она же - его номер при записи): "
                             "English - 1, Literature - 2, Geography - 3, Music - 4, Medicine - 5."
                             "Сделайте свой выбор: ")
        if self.subject == '1':
            from English_Questions import testAnswers
        elif self.subject == '2':
            from Literature_Questions import testAnswers
        elif self.subject == '3':
            from Geography_Questions import testAnswers
        elif self.subject == '4':
            from Music_Questions import testAnswers
        elif self.subject == '5':
            from Medicine_Questions import testAnswers

        self.dict_q = testAnswers()



    def input_test(self):
        super().input_test()
        self.filik = str(self.test_number + ".q")

    def save(self):
        import json
        with open(self.filik, "w") as f:
            json.dump(self.dict_q, f)

    # Создадим функцию десериализации данных из файла в Словарь методом load модуля json
    def load(self):
        import json
        # Создаём словарь для записи десериализированной из файла информации:
        questions = {}
        # Вводим с клавиатуры имя файла для записи нашей сериализированной информации
        # Указываем файл:
        with open(self.filik, "r") as f:
            # Записываем инфу из этого файла в созданный словарь
            questions = json.load(f)
        return print(questions)

quest = List_questions()
quest.input_test()
quest.selectSubject()
quest.save()
quest.load()

class List_answers(List_tests):
    def __init__(self):
        super().__init__()
        self.answer = None
        self.dict_a = None
        self.fylik = None

    def selectAnswer(self):
        self.answer = input("Выберите имя теста и нажмите его цифру (она же - его номер при записи): "
                             "English - 1, Literature - 2, Geography - 3, Music - 4, Medicine - 5."
                             "Сделайте свой выбор: ")
        if self.answer == '1':
            from English_Answers import trueAnswers
        elif self.answer == '2':
            from Literature_Answers import trueAnswers
        elif self.answer == '3':
            from Geography_Answers import trueAnswers
        elif self.answer == '4':
            from Music_Answers import trueAnswers
        elif self.answer == '5':
            from Medicine_Answers import trueAnswers

        self.dict_a = trueAnswers()

    def input_test(self):
        super().input_test()
        self.fylik = str(self.test_number + ".a")

    def save(self):
        import json
        with open(self.fylik, "w") as f:
            json.dump(self.dict_a, f)

    # Создадим функцию десериализации данных из файла в Словарь методом load модуля json
    def load(self):
        import json
        # Создаём словарь для записи десериализированной из файла информации:
        answers = {}
        # Вводим с клавиатуры имя файла для записи нашей сериализированной информации
        # Указываем файл:
        with open(self.fylik, "r") as f:
            # Записываем инфу из этого файла в созданный словарь
            answers = json.load(f)
        return print(answers)


reply = List_answers()
reply.input_test()
reply.selectAnswer()
reply.save()
reply.load()