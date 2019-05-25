class Duck:
    def quack(self):
        pass

    def fly(self):
        pass


class MallardDuck(Duck):
    def quack(self):
        print("Quack")

    def fly(self):
        print("I'm flying")


class Turkey:
    def gobble(self):
        pass

    def fly(self):
        pass


class WildTurkey(Turkey):
    def gobble(self):
        print("Gobble gobble")

    def fly(self):
        print("I'm flying a short distance")


class TurkeyAdapter(Duck):
    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for i in range(5):
            self.turkey.fly()


def duckTest(duck: Duck):
    duck.quack()
    duck.fly()


if __name__ == '__main__':
    duck: MallardDuck = MallardDuck()
    turkey: WildTurkey = WildTurkey()
    turkeyAdapter = TurkeyAdapter(turkey)
    print("The Turkey says...")
    turkey.gobble()
    turkey.fly()

    print("\nThe Duck says...")
    duckTest(duck)
    print("\nThe TurkeyAdapter says...")
    duckTest(turkeyAdapter)
