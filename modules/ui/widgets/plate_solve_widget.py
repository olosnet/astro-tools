from PyQt5.QtWidgets import QVBoxLayout, QWidget


class PlateSolveWidget(QWidget):

    __locale = None

    def __init__(self, parent, locale) -> None:
        super().__init__(parent)
        self.__locale = locale
        layout = QVBoxLayout(self)
        self.setLayout(layout)
