class aaa():
    def __init__(self):
        self.a = 6
        self.b = self.a
        print(self.a)
        print(self.b)

        self.b = 77
        print(self.a)
        print(self.b)

aaa = aaa()
