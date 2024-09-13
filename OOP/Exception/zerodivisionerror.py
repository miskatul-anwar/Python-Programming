class Funcions:
    def div(self, x, y):
        if y == 0:
            raise ZeroDivisionError("You're dividing the number by zero")
        else:
            print(x / y)


funcions_instance = Funcions()

funcions_instance.div(10, 2)  # This will print 5.0
funcions_instance.div(10, 0)  # This will raise a ZeroDivisionError
