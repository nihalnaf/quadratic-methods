import math

class Quadratic:
    """ Quadratic class for second-degree polynomial and some methods associated with it. """
    #constructor
    def __init__(self, a, b, c):
        """ Create a second-degree polynomial with the given coefficient values. """
        self.a = a
        self.b = b
        self.c = c
    #define string method for Quadratic class
    def __str__(self):
        a = self.a
        b = self.b
        c = self.c
        #define how to display objects of Quadratic type in string format
        return "f(x) = " + str(a) + "x^2 + " + str(b) + "x + " + str(c)
    #define roots method for Quadratic class
    def roots(self):
        a = self.a
        b = self.b
        c = self.c
        #decision structure that determines how to calculate the roots as negative value inside radical means imaginary roots, equal 0 means one real root, and positive means two real roots
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
    #define derivative method for Quadratic class      
    def derivative(self):
        a = self.a * 2
        b = self.b
        return str(a) + "x + " + str(b)
    #define integral method for Quadratic class
    def integral(self):
        a = self.a / 3
        b = self.b / 2
        c = self.c
        return str(a) + "x^3 + " + str(b) + "x^2 + " + str(c) + "x + C"
    #define solveForY method for Quadratic class
    def solveForY(self, x):
        a = self.a
        b = self.b
        c = self.c
        y = (a * (x ** 2)) + (b * x) + c
        return y
    #define solveForX method for Quadratic class
    def solveForX(self, y):
        a = self.a
        b = self.b
        c = self.c - y
        #decision structure similar to roots method
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
#define the main function       
def main():
    end = ""
    print("A second-degree polynomial is of the form f(x) = ax^2 + bx + c")
    #emulate a do-while loop to keep asking user for the polynomial values until they quit
    while end.lower() != "q":
        #ask user for inputs for values of second-degre polynomial
        print("Enter the values of your polynomial below.")
        a = float(input("Enter the value for a: "))
        b = float(input("Enter the value for b: "))
        c = float(input("Enter the value for c: "))
        #create an object that has the type Quadratic based on what values the user entered
        quadratic = Quadratic(a, b, c)
        #display the second-degree polynomial based on what values the user entered
        print("\nYour second-degree polynomial is: " + str(quadratic))
        #create an array of the options that the user can select from
        options = ["Roots", "Derivative", "Integral", "Find f(x) given x", "Find x given f(x)"]
        #print all 5 options using a for loop and index of the list of options
        for i in range(1, len(options) + 1):
            print(str(i) + ". " + options[i - 1])

        choice = int(input("What would you like to calculate for your second-degree polynomial?\n"))
        #decision structure for which method to execute and display results depending on user choice
        if choice == 1:
            print("x = " + str(quadratic.roots()))
        if choice == 2:
            print("f'(x) = " + quadratic.derivative())
        if choice == 3:
            print("F(x) = " + quadratic.integral())
        if choice == 4:
            x = float(input("Enter the value for x: "))
            print("f(" + str(x) + ") = " + str(quadratic.solveForY(x)))
        if choice == 5:
            y = float(input("Enter the value for f(x): "))
            print("x = " + str(quadratic.solveForX(y)))
        #ask user if they want to quit
        end = input("Would you like to continue? Enter 'Q' or 'q' to quit: ")
main()
