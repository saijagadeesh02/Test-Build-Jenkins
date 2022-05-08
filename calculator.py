

class Calculator:

    def __init__(self):
        pass

    def add(self, *params):
        return sum(params)

    def multiply(self, *params):
        result = 1
        for n in params:
            result *= n
        return result
