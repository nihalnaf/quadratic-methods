import math

class Quadratic:
    """ Quadratic class for second-degree polynomial and some methods associated with it. """

    def __init__(self, a, b, c):
        """ Create a second-degree polynomial with the given coefficient values. """
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        a = self.a
        b = self.b
        c = self.c
        return "f(x) = " + str(a) + "x^2 + " + str(b) + "x + " + str(c)

    def roots(self):
        a = self.a
        b = self.b
        c = self.c
        radical_contents = (b ** 2 - 4 * a * c)
        if radical_contents < 0:
            return "There are no real roots."
        elif radical_contents == 0:
            if b == 0:
                return 0
            else:
                return ((-b) / (2 * a))
        else:
            first_root = ((-b) + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
            second_root = ((-b) - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
            return (first_root, second_root)
          
    def derivative(self):
        a = self.a * 2
        b = self.b
        return str(a) + "x + " + str(b)

    def integral(self):
        a = self.a / 3
        b = self.b / 2
        c = self.c
        return str(a) + "x^3 + " + str(b) + "x^2 + " + str(c) + "x + C"

    def solveForY(self, x):
        a = self.a
        b = self.b
        c = self.c
        y = (a * (x ** 2)) + (b * x) + c
        return y

    def solveForX(self, y):
        a = self.a
        b = self.b
        c = self.c - y
        radical_contents = (b ** 2 - 4 * a * c)
        if radical_contents < 0:
            return "There are no real solutions."
        elif radical_contents == 0:
            if b == 0:
                return 0
            else:
                return ((-b) / (2 * a))
        else:
            first_solution = ((-b) + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
            second_solution = ((-b) - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
            return (first_solution, second_solution)
        

def main():
    end = ""
    print("A second-degree polynomial is of the form f(x) = ax^2 + bx + c")
    while end.lower() != "q":
        print("Enter the values of your polynomial below.")
        a = float(input("Enter the value for a: "))
        b = float(input("Enter the value for b: "))
        c = float(input("Enter the value for c: "))
        quadratic = Quadratic(a, b, c)
        print("\nYour second-degree polynomial is: " + str(quadratic))
        options = ["Roots", "Derivative", "Integral", "Find f(x) given x", "Find x given f(x)"]
        for i in range(1, len(options) + 1):
            print(str(i) + ". " + options[i - 1])

        choice = int(input("What would you like to calculate for your second-degree polynomial?\n"))
        if choice == 1:
            print("x = " + str(quadratic.roots()))
        if choice == 2:
            print("f'(x) = " + quadratic.derivative())
        if choice == 3:
            print("F(x) = " + quadratic.integral())
        if choice == 4:
            x = float(input("Enter the value for x: "))
            print("f(x) = " + str(quadratic.solveForY(x)))
        if choice == 5:
            y = float(input("Enter the value for f(x): "))
            print("x = " + str(quadratic.solveForX(y)))
        end = input("Would you like to continue? Enter 'Q' or 'q' to quit: ")
main()
