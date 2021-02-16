class Constant:
    def __init__(self, value):
        self.value = value

    def calculate(self):
        return self
    
    def calculate(self):
        return self

    def __str__(self):
        return str(self.value)

class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def calculate(self):
        return Constant(self.value)
    
    def simplify(self):
        return Constant(self.value)

    def __str__(self):
        return str(self.name) + " = " + str(self.value)

class Sum:
    def __init__(self, v1, v2):
        if type(v1) == int:
            self.v1 = v1
        else:
            self.v1 = int(str(v1.value))
        if type(v2) == int:
            self.v2 = v2
        else:
            self.v2 = int(str(v2.value))
        self.result = self.v1 + self.v2

    def calculate(self):
        return Constant(self.result)

    def simplify(self):
        if self.v1 == 0:
            return Constant(self.v2)
        elif self.v2 == 0:
            return Constant(self.v1)
        else:
            return self

    def __str__(self):
        return str(self.v1) + " + " + str(self.v2) + " = " + str(self.result)

class Product:
    def __init__(self, v1, v2):
        if type(v1) == int:
            self.v1 = v1
        else:
            self.v1 = int(str(v1.value))
        if type(v2) == int:
            self.v2 = v2
        else:
            self.v2 = int(str(v2.value))
        self.result = self.v1 * self.v2

    def calculate(self):
        return Constant(self.result)

    def simplify(self):
        if self.v1 == 0 or self.v2 == 0:
            return Constant(0)
        elif self.v1 == 1:
            return Constant(self.v2)
        elif self.v2 == 1:
            return Constant(self.v1)

    def __str__(self):
        return str(self.v1) + " * " + str(self.v2) + " = " + str(self.result)

if __name__ == "__main__":
    
    const_seventy_three = Constant(73)
    print(const_seventy_three)

    varx = Variable("x", 2)
    print(varx.name)

    const_three = Constant(3)
    const_four = Constant(4)
    const_seven = Constant(7)
    p1 = Product(const_four,const_seven)
    s1 = Sum(const_three, p1.result)
    print(s1)

    const_two = Constant(2)
    const_one = Constant(1)
    p2 = Product(const_two,Sum(varx,const_one).result)
    print(p2)

    s2 = Sum(const_two,Product(varx,Sum(varx,const_one).result).result)
    print(s2)