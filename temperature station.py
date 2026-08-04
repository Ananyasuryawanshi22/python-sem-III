class Display:
    def update(self, temperature):
        print("Display updated: Temperature =", temperature, "°C")


class WeatherStation:
    def __init__(self):
        self.temperature = 0
        self.displays = []

    def add_display(self, display):
        self.displays.append(display)

    def set_temperature(self, temperature):
        self.temperature = temperature
        print("\nTemperature changed to", temperature, "°C")
        self.notify()

    def notify(self):
        for display in self.displays:
            display.update(self.temperature)


station = WeatherStation()

display1 = Display()
display2 = Display()

station.add_display(display1)
station.add_display(display2)

station.set_temperature(30)
station.set_temperature(35)