from typing import List


class Observer:
    def update(self, temp: float, humidity: float, pressure: float):
        pass


class Subject:
    def registerObserver(self, o: Observer):
        pass

    def removeObserver(self, o: Observer):
        pass

    def notifyObservers(self):
        pass


class DisplayElement:
    def display(self):
        pass


class WeatherData(Subject):
    def __init__(self):
        self.changed = True
        self.observers: List[Observer] = []
        self.temperature: float = None
        self.humidity: float = None
        self.pressure: float = None

    def registerObserver(self, o: Observer):
        self.observers.append(o)

    def removeObserver(self, o: Observer):
        try:
            self.observers.remove(o)
        except ValueError:
            print("observer is not registered")
            pass

    def notifyObservers(self):
        if self.changed:
            for observer in self.observers:
                observer.update(self.temperature, self.humidity, self.pressure)
            self.changed = False

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()

    def setChanged(self):
        self.changed = True


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weatherData: WeatherData):
        self.temperature: float = None
        self.humidity: float = None
        self.weatherData: WeatherData = weatherData
        self.weatherData.registerObserver(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.temperature = temp
        self.humidity = humidity
        self.display()

    def display(self):
        print("Current conditions: " + str(self.temperature) + "F degrees and " + str(self.humidity) + "% humidity")


if __name__ == '__main__':
    weatherData = WeatherData()
    currentDisplay = CurrentConditionsDisplay(weatherData)
    weatherData.setMeasurements(80, 65, 30.4)
