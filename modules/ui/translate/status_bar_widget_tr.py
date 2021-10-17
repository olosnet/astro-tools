from PyQt5.QtCore import QObject

class StatusBarWidgetTranslate:

    @staticmethod
    def TIP_COPY_JD_TO_CLIPBOARD(parent : QObject) -> str:
        return parent.tr("Copy Julian Date to Clipboard")

    @staticmethod
    def STATUS_COPIED(parent: QObject) -> str:
        return parent.tr("Copied!")
