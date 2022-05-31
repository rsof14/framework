class Event:
    def __init__(self):
        self.__subscribers = []

    def connect(self, subscriber):
        self.__subscribers.append(subscriber)

    def disconnect(self, subscriber):
        self.__subscribers.remove(subscriber)

    def emit(self, *args, **kwargs):
        for subscriber in self.__subscribers:
            subscriber(*args, **kwargs)
