class Tap:
    def __init__(self):
        self.is_on = False
    def turn_on(self):
        if not self.is_on:
            self.is_on=True
            print("The tap is now ON, water is flowing!")
        else:
            print("The tap is already ON")

    def turn_off(self):
        if self.is_on:
            self.is_on=False
            print("The tap is now OFF. Water has stopped")
        else:
            print("The tap already OFF")

my_tap = Tap()
my_tap.turn_on()
my_tap.turn_off()
my_tap.turn_off()
my_tap.turn_on()
