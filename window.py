import pygame


class Window:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    Color = (0, 0, 0)

    def __init__(self, title, parent):
        self.widgets = []
        self.parent = parent
        self.window = pygame.display.set_mode((Window.SCREEN_WIDTH, Window.SCREEN_HEIGHT))
        pygame.display.set_caption(title)

    def render(self):
        self.window.fill(Window.Color)
        pygame.display.flip()
        for widget in self.widgets:
            widget.render()
