
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QWidget
from .tr import LocationsWidgetTranslate as tr


class LocationsWidget(QWidget):

    __locale = None
    __profile_db = None

    def __init__(self, parent, locale, profile_db) -> None:
        super().__init__(parent)
        self.__locale = locale
        self.__profile_db = profile_db

        self.setWindowTitle(tr.LOCATION_WINDOW_TITLE(self))
        ccd_group_box_layout = QVBoxLayout(self)
        self.setLayout(ccd_group_box_layout)

class LocationsDialog(QDialog):

    def __init__(self, parent, locale, profile_db) -> None:
        super().__init__(parent)

        self.setWindowTitle(tr.LOCATION_WINDOW_TITLE(self))
        widget = LocationsWidget(self, locale, profile_db)
        layout = QVBoxLayout(self)
        layout.addWidget(widget)

        self.setLayout(layout)
