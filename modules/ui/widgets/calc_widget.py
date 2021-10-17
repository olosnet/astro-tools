from PyQt5.QtWidgets import QComboBox, QHBoxLayout, QLabel, QVBoxLayout, QWidget

from modules.ui.translate import CalcWidgetTranslate as tr
from modules.ui.widgets.calc_ccd_widget import CalcCCDWidget


class CalcWidget(QWidget):

    __calc_selector = None
    __calc_ccd_widget = None
    __locale = None

    def __init__(self, parent, locale) -> None:
        super().__init__(parent)

        self.__locale = locale
        layout = QVBoxLayout(self)

        # Selector
        selector_widget = self.__make_calc_selector(self)

        self.__calc_ccd_widget = CalcCCDWidget(self, self.__locale)
        self.__calc_ccd_widget.setVisible(True)

        layout.addWidget(selector_widget, 0)
        layout.addWidget(self.__calc_ccd_widget, 1)
        self.setLayout(layout)

    def __make_calc_selector(self, widget) -> QWidget:
        selector_widget = QWidget(widget)
        selector_layout = QHBoxLayout(selector_widget)
        selector_layout.addStretch()
        self.__calc_selector = QComboBox()
        self.__calc_selector.currentIndexChanged.connect(self.on_calc_selector_change)
        self.__calc_selector.addItem("CCD")
        selector_layout.addWidget(QLabel(tr.CALC_SELECTOR(selector_widget), selector_widget), 0)
        selector_layout.addWidget(self.__calc_selector, 0)
        selector_widget.setLayout(selector_layout)
        return selector_widget

    def on_calc_selector_change(self) -> None:
        ccd_visible = self.__calc_selector.currentIndex() == 0
        self.__calc_selector.setVisible(ccd_visible)
