class Car(object):
    def __init__(self):
        self._speed = 100

    @property
    def speed(self):
        print "speed is", self._speed
        return self._speed

    @speed.setter
    def speed(self, value):
        print "setting to", value
        self._speed = value

car = Car()
car.speed = 80

# x = car.speed


class TalkativeInt(int):
    """Every operator in Python is basically a method call “under the
    hood.” But while occasionally producing a more readable “domain
    specific language” (DSL), defining special callable meanings for
    operators adds no improvement to the underlying capabilities of
    function calls."""
    def __lshift__(self, other):
        print "shift", self, "by", other
        return int.__lshift__(self, other)
t = TalkativeInt(8)
t<<3
