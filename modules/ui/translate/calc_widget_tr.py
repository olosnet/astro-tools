from PyQt5.QtCore import QObject

class CalcWidgetTranslate:

    @staticmethod
    def CALC_SELECTOR(parent : QObject) -> str:
        return parent.tr("Calculation type:")
