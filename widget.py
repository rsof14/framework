from __future__ import annotations


class Widget:
    def __init__(self, height: float, width: float, parent: Widget):
        self.__x = 0
        self.__y = 0
        self.height = height
        self.width = width
        self.__parent = parent
        self.children_list = []

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def global_to_parent(self, global_x: float, global_y: float):
        x = global_x - self.__parent.x
        y = global_y - self.__parent.y
        return x, y

    def parent_to_global(self, x: float, y: float):
        global_x = x + self.__parent.x
        global_y = y + self.__parent.y
        return global_x, global_y

    def handle_mouse_enter(self, event):
        pass

    def handle_click(self, event):
        pass

    def render(self):
        pass

    def add_child(self, child: Widget):
        self.children_list.append(child)
