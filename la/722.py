class DZ72:
    def __init__(self, number: str):
        self.number = number

    def isP(self):
        number = str(self.number)
        for i in range(len(self.number) // 2):
            if self.number[i] != self.number[len(number) - 1 - i]:
                return False
        return True

    def __str__(self):
        return f"Number: {self.number}\n"


num = DZ72(number="343")
print(num)
print(num.isP())
