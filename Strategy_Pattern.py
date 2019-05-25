class Duck:
    def __init__(self):
        self.quackBehavior: QuackBehavior = None
        self.flyBehavior: FlyBehavior = None

    def performQuack(self):
        self.quackBehavior.quack()

    def perfomrFly(self):
        self.flyBehavior.fly()

    def swim(self):
        print("All ducks float,even decoys")

    def display(self):
        pass


class FlyBehavior:
    def fly(self):
        pass


class QuackBehavior:
    def quack(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!!")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")


class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.quackBehavior = Quack()
        self.flyBehavior = FlyWithWings()

    def display(self):
        print("I'm a real Mallard duck")


class ModelDuck(Duck):
    def __init__(self):
        super().__init__()
        self.flyBehavior = FlyNoWay()
        self.quackBehavior = Quack()

    def display(self):
        print("I'm a model duck")


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")


if __name__ == '__main__':
    mallard: Duck = MallardDuck()
    mallard.performQuack()
    mallard.perfomrFly()
    model: Duck = ModelDuck()
    model.perfomrFly()
    model.flyBehavior = FlyRocketPowered()
    model.perfomrFly()
