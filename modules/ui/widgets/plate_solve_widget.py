from PyQt5.QtWidgets import QVBoxLayout, QWidget
from modules.ui.translate import Translate


class PlateSolveWidget(QWidget):

    __tr = Translate()
    __locale = None

    def __init__(self, parent, locale) -> None:
        super().__init__(parent)
        self.__locale = locale
        layout = QVBoxLayout(self)
        self.setLayout(layout)
