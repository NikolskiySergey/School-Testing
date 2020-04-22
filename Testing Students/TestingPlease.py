class InviteToTest:
    def __init__(self):
        self.invitation = None
        # self.repack = None

    def input_examination(self):
        self.invitation = input("Выберите тест и нажмите соответствующую ему цифру: "
                   "английский - 1, литература - 2, география - 3, музыка - 4, медицина - 5."
                   "Сделайте свой выбор: ")

        if self.invitation == '1':
            from test_eng import verification, check
        elif self.invitation == '2':
            from test_liter import verification, check
        elif self.invitation == '3':
            from test_geogr import verification, check
        elif self.invitation == '4':
            from test_musi import verification, check
        elif self.invitation == '5':
            from test_medic import verification, check

control = InviteToTest()
control.__init__()
control.input_examination()