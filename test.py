
class A:
    def __init__(self):
        self.k = 2

class TestClass(A):
    def __init__(self, start):
        super().__init__()
        print(self.k)

x =TestClass(1)

