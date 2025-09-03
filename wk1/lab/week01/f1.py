class Grade:
    def __int__(self, percentage):
        self.percentage = percentage

        @property
        def percentage(self):
            return self.__percentage

        @percentage.setter
        def percentage(self, value: int) -> None:
            if isinstance(value, int) and 0 <= value <= 100:
                self.__percentage = value
            else:
                raise ValueError("Invalid percentage")


class PassingGrade(Grade):

    def __init__(self, percentage):
        super().__init__(percentage)
        self.__percentage = None

    @property
    def percentage(self):
        return self.__percentage

    @percentage.setter
    def percentage(self, value):
        super.percentage = value
        if isinstance(value, int)and value < 50:
            raise ValueError("This is not a passing grade")
        self.__percentage = value

my_Grade = Grade(100)
print(my_Grade.percentage)

pg = PassingGrade(40)