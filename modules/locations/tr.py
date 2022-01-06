from PyQt5.QtCore import QObject

class LocationsWidgetTranslate:

    @staticmethod
    def LOCATION_WINDOW_TITLE(parent: QObject) -> str:
        return parent.tr("Locations management")