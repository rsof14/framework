class Window:
    def __init__(self, title, parent):
        self.widgets = []
        self.parent = parent
        self.title = title

    def render(self):
        for widget in self.widgets:
            widget.render()
