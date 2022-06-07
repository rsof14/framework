import pygame


class Window:
    DEFAULT_SCREEN_WIDTH = 800
    DEFAULT_SCREEN_HEIGHT = 800
    DEFAULT_BACKGROUND_COLOR = (0, 0, 0)

    def __init__(self, title, parent):
        self.widgets = []
        self.parent = parent
        self.title = title
        self.window = pygame.display.set_mode((Window.DEFAULT_SCREEN_WIDTH, Window.DEFAULT_SCREEN_HEIGHT))

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title
        pygame.display.set_caption(self.__title)

    def render(self):
        self.window.fill(Window.DEFAULT_BACKGROUND_COLOR)
        for widget in self.widgets:
            widget.render()
        pygame.display.flip()

    def handle_event(self):
        pass
