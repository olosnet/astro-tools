from PyQt5.QtCore import QObject

class CalcWidgetTranslate:

    @staticmethod
    def CALC_SELECTOR(parent : QObject) -> str:
        return parent.tr("Calculation type:")

    @staticmethod
    def TIME_SELECTOR_ENTRY(parent: QObject) -> str:
        return parent.tr("TIME")

    @staticmethod
    def CCD_SELECTOR_ENTRY(parent: QObject) -> str:
        return parent.tr("CCD")
