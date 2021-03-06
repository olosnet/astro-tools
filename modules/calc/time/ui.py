
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDoubleSpinBox, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QMenuBar, QMenu, \
    QPushButton, QSpinBox, QVBoxLayout, QWidget, QGroupBox

import modules.base.res
from .tr import CalcTimeWidgetTranslate as tr


from .logic import CalcTime

class CalcTimeWidget(QGroupBox):

    __locale = None
    __icon_clipboard = None

    def __init__(self, parent, locale):
        super().__init__(parent)

        self.__locale = locale
        self.__icon_clipboard = QtGui.QIcon(":/icons/clipboard")
