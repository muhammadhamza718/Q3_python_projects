class Counter:
    count = 0 

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_Count(cls):
        print(f"Total object created: {cls.count}")

c1 = Counter()
c2 = Counter()
c3 = Counter()
c4 = Counter()

Counter.show_Count()