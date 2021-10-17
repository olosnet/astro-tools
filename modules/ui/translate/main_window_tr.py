from PyQt5.QtCore import QObject

class MainWindowTranslate:

    @staticmethod
    def TAB_TITLE_CALC(parent : QObject) -> str:
        return parent.tr("Calculators")

    @staticmethod
    def TAB_TITLE_PS(parent : QObject) -> str:
        return parent.tr("Plate solving")

    @staticmethod
    def MENU_FILE_S(parent : QObject) -> str:
        return parent.tr("&File")

    @staticmethod
    def MENU_HELP_S(parent : QObject) -> str:
        return parent.tr("&Help")

    @staticmethod
    def ACTION_EXIT_S(parent : QObject) -> str:
        return parent.tr("&Exit")

    @staticmethod
    def ACTION_ABOUT_S(parent : QObject) -> str:
        return parent.tr("About")

    @staticmethod
    def TIP_EXIT_S(parent : QObject) -> str:
        return parent.tr("Close the application.")

