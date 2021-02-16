class Constant:
    def __init__(self, value):
        self.value = value

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
    
    c = Constant(5)
    print("str(c): ")
    print(c)
    print("c.value: ")
    print(c.value)
    print("c.calculate(): ")
    print(c.calculate())

    print()

    var = Variable("var", 2)
    print("str(var): ")
    print(var)
    print("var.name: ")
    print(var.name)
    print("var.value: ")
    print(var.value)
    print("var.calculate(): ")
    print(var.calculate())

    print()
    
    car = Variable("car", c)
    print("str(car): ")
    print(car)
    print("car.name: ")
    print(car.name)
    print("car.value: ")
    print(car.value)
    print("car.calculate(): ")
    print(car.calculate())

    print()
    
    sum_vals = Sum(3, 1)
    print("str(sum_vals): ")
    print(sum_vals)
    print("sum_vals.v1: ")
    print(sum_vals.v1)
    print("sum_vals.v2: ")
    print(sum_vals.v2)
    print("sum_vals.calculate(): ")
    print(sum_vals.calculate())
    print("sum_vals.simplify(): ")
    print(sum_vals.simplify())


    print()

    sum_const = Sum(c, 0)
    print("str(sum_const): ")
    print(sum_const)
    print("sum_const.v1: ")
    print(sum_const.v1)
    print("sum_const.v2: ")
    print(sum_const.v2)
    print("sum_const.calculate(): ")
    print(sum_const.calculate())
    print("sum_const.simplify(): ")
    print(sum_const.simplify())

    print()

    sum_cvar = Sum(c, car)
    print("str(sum_cvar): ")
    print(sum_cvar)
    print("sum_cvar.v1: ")
    print(sum_cvar.v1)
    print("sum_cvar.v2: ")
    print(sum_cvar.v2)
    print("sum_cvar.calculate(): ")
    print(sum_cvar.calculate())
    print("sum_cvar.simplify(): ")
    print(sum_cvar.simplify())
    
    print()
    
    prod_vals = Product(3, 4)
    print("str(prod_vals): ")
    print(prod_vals)
    print("prod_vals.v1: ")
    print(prod_vals.v1)
    print("prod_vals.v2: ")
    print(prod_vals.v2)
    print("prod_vals.calculate(): ")
    print(prod_vals.calculate())
    print("prod_vals.simplify(): ")
    print(prod_vals.simplify())


    print()

    prod_const = Product(c, 1)
    print("str(prod_const): ")
    print(prod_const)
    print("prod_const.v1: ")
    print(prod_const.v1)
    print("prod_const.v2: ")
    print(prod_const.v2)
    print("prod_const.calculate(): ")
    print(prod_const.calculate())
    print("prod_const.simplify(): ")
    print(prod_const.simplify())

    print()

    prod_cvar = Product(0, car)
    print("str(prod_cvar): ")
    print(prod_cvar)
    print("prod_cvar.v1: ")
    print(prod_cvar.v1)
    print("prod_cvar.v2: ")
    print(prod_cvar.v2)
    print("prod_cvar.calculate(): ")
    print(prod_cvar.calculate())
    print("prod_cvar.simplify(): ")
    print(prod_cvar.simplify())