from base.clock_observer import ClockObserver


class TimeSourceImplementation:
    def __init__(self):
        self.__its_observer = list()

    def register_observer(self, observer: ClockObserver):
        self.__its_observer.append(observer)

    def notify(self, hours: int, minutes: int, seconds: int):
        for observer in self.__its_observer:
            observer.update(hours, minutes, seconds)