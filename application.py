from __future__ import annotations
import pygame
from window import Window
from event import Event


class Application:
    def __init__(self):
        pygame.init()
        self.windows = []
        self.events = []
        self.is_running = False
        self.active_window = None

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()
            else:
                pass

    def run(self):
        self.is_running = True
        while self.is_running:
            self.event_loop()
            for window in self.windows:
                window.render()

    def create_window(self, title):
        window = Window(title, self)
        self.windows.append(window)
        if self.active_window is None:
            self.active_window = window
        return window

    def stop(self):
        self.is_running = False
