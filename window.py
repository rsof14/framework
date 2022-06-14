import pygame
from pygame._sdl2 import Window as SdlWindow, Renderer


class Window:
    DEFAULT_SCREEN_WIDTH = 800
    DEFAULT_SCREEN_HEIGHT = 800
    DEFAULT_BACKGROUND_COLOR = (0, 0, 0)

    def __init__(self, title, parent):
        self.window = SdlWindow(title, size=(Window.DEFAULT_SCREEN_WIDTH, Window.DEFAULT_SCREEN_HEIGHT), resizable=True)
        self.renderer = Renderer(self.window)
        self.widgets = []
        self.parent = parent
        self.title = title
        self.active_widget = None
        # self.window = pygame.display.set_mode((Window.DEFAULT_SCREEN_WIDTH, Window.DEFAULT_SCREEN_HEIGHT))

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title
        pygame.display.set_caption(self.__title)

    def render(self):
        self.renderer.clear()
        for widget in self.widgets:
            widget.render()
        self.renderer.present()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                widgets = self.return_widget(event.pos)
                for widget in widgets:
                    widget.handle_click(event)
                    self.active_widget = widget
        if event.type == pygame.MOUSEMOTION:
            widgets = self.return_widget(event.pos)
            for widget in widgets:
                widget.handle_mouse_enter(event)
        if event.type == pygame.KEYDOWN:
            self.active_widget.handle_keydown(event.key)


    def return_widget(self, coord):
        widgets = []
        for widget in self.widgets:
            x, y = widget.parent_to_global(0, 0) # сделать преобразование наоборот global to parent передавать координаты щелчка мышки
            if x <= coord[0] <= x + widget.width and y <= coord[1] <= y + widget.height:
                widgets.append(widget)
        return widgets

    # def handle_keydown(self, key):
    #     if key == pygame.K_BACKSPACE:
    #         return self.handle_backspace  # ???
    #
    # def handle_backspace(self, str):
    #     return str[0:len(str) - 2]
