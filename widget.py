from __future__ import annotations


class Widget:
    def __init__(self, x: int, y: int, height: float, width: float, parent_to: Widget):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.__parent_to = parent_to
        self.children_list = []

    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x

    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y

    def global_to_parent(self):
        self.set_x(self.get_x() - self.__parent_to.get_x())
        self.set_y(self.get_y() - self.__parent_to.get_y())

    def parent_to_global(self):
        self.set_x(self.get_x() + self.__parent_to.get_x())
        self.set_y(self.get_y() + self.__parent_to.get_y())

    def handle_mouse_enter(self, event):
        pass

    def handle_click(self, event):
        pass

    def render(self):
        pass

    def add_child(self, child: Widget):
        self.children_list.append(child)
