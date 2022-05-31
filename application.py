from window import Window
from event import Event


class Application:
    def __init__(self):
        self.windows = []
        self.events = []
        self.is_running = False

    def event_loop(self):
        for event in self.events:
            event.emit()

    def run(self):
        self.is_running = True
        while self.is_running:
            self.event_loop()
            for window in self.windows:
                window.render()

    def create_window(self, title):
        window = Window(title, self)
        self.windows.append(window)
