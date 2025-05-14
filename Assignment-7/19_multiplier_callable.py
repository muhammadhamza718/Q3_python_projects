class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value
    
m = Multiplier(2)
print(callable(m))
print(m(5))